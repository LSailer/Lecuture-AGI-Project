import sys
import unittest
from pathlib import Path

# Make src importable when running from project root
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from main import has_consensus, run_voting_batch  # noqa: E402


class DummyEnvironment:
    def __init__(self, state: int = 0) -> None:
        self.state = state

    def get_state(self) -> int:
        return self.state

    def apply_move(self, action: int) -> None:
        self.state += action

    def visualize(self) -> str:
        return str(self.state)


class DummyLLM:
    def __init__(self, response_ids: list[str]) -> None:
        self.response_ids = response_ids

    def generate_batch(self, batch_messages, do_sample=False, temperature=0.0, top_p=0.95):
        responses = []
        for response_id in self.response_ids[: len(batch_messages)]:
            responses.append([{"role": "assistant", "content": response_id}])
        self.response_ids = self.response_ids[len(batch_messages):]
        return responses


class DummyAgent:
    def __init__(
        self,
        parse_outputs: dict[str, tuple[int, int] | Exception],
        extra_outputs: list[tuple[int, int] | Exception] | None = None,
        initial_state: int = 0,
    ) -> None:
        self.environment = DummyEnvironment(initial_state)
        self.prompts = object()
        self.llm = DummyLLM(list(parse_outputs.keys()))
        self.parse_outputs = parse_outputs
        self.extra_outputs = extra_outputs or []
        self.system_prompt = "system"

    def build_prompt(self, previous_move, current_state, current_step):
        return (
            [
                {"role": "system", "content": "system"},
                {"role": "user", "content": f"state={current_state}"},
            ],
            f"state={current_state}",
        )

    def parse_response(self, content, current_state, current_step, agent_num):
        result = self.parse_outputs[content]
        if isinstance(result, Exception):
            raise result
        return result

    def execute_decompose_prompt(
        self,
        previous_move,
        current_state,
        step,
        agent_num,
        temperature=0.1,
        do_sample=True,
        top_p=0.95,
    ):
        if not self.extra_outputs:
            raise ValueError("No extra outputs configured.")
        result = self.extra_outputs.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


class TestVotingHelpers(unittest.TestCase):
    def test_has_consensus_true_when_margin_is_met(self) -> None:
        votes = {"a": 3, "b": 1}
        self.assertTrue(has_consensus(votes, margin_k=2))

    def test_has_consensus_false_when_margin_not_met(self) -> None:
        votes = {"a": 3, "b": 2}
        self.assertFalse(has_consensus(votes, margin_k=2))

    def test_has_consensus_true_with_single_candidate(self) -> None:
        votes = {"a": 2}
        self.assertTrue(has_consensus(votes, margin_k=1))

    def test_has_consensus_false_with_no_votes(self) -> None:
        self.assertFalse(has_consensus({}, margin_k=1))


class TestRunVotingBatch(unittest.TestCase):
    def test_returns_none_when_no_consensus_is_reached(self) -> None:
        agent = DummyAgent(
            parse_outputs={
                "r1": (1, 1),
                "r2": (2, 2),
            },
            extra_outputs=[],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=1,
            batch_size=2,
            margin_k=2,
            max_agents_total=2,
        )

        self.assertFalse(consensus_reached)
        self.assertIsNone(best_prediction)
        self.assertEqual(len(failed_predictions), 0)
        self.assertEqual(sum(candidate_voting.values()), 2)

    def test_reaches_consensus_after_additional_agent(self) -> None:
        agent = DummyAgent(
            parse_outputs={
                "r1": (1, 1),
                "r2": (2, 2),
            },
            extra_outputs=[(1, 1)],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=1,
            batch_size=2,
            margin_k=1,
            max_agents_total=3,
        )

        self.assertTrue(consensus_reached)
        self.assertIsNotNone(best_prediction)
        self.assertEqual(best_prediction["action"], 1)
        self.assertEqual(best_prediction["state"], 1)
        self.assertEqual(len(failed_predictions), 0)
        self.assertEqual(sum(candidate_voting.values()), 3)

    def test_inconsistent_same_action_different_state_is_rejected_before_voting(self) -> None:
        agent = DummyAgent(
            parse_outputs={
                "r1": (1, 1),
                "r2": (1, 99),
            },
            extra_outputs=[],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=1,
            batch_size=2,
            margin_k=1,
            max_agents_total=2,
        )

        # The inconsistent candidate is discarded before voting.
        self.assertTrue(consensus_reached)
        self.assertIsNotNone(best_prediction)
        self.assertEqual(best_prediction["action"], 1)
        self.assertEqual(best_prediction["state"], 1)
        self.assertEqual(len(failed_predictions), 1)
        self.assertEqual(sum(candidate_voting.values()), 1)

    def test_inconsistent_prediction_is_rejected(self) -> None:
        # action=1 from state=0 should produce next_state=1, not 5
        agent = DummyAgent(
            parse_outputs={
                "r1": (1, 5),
                "r2": (1, 1),
            },
            extra_outputs=[],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=1,
            batch_size=2,
            margin_k=1,
            max_agents_total=2,
        )

        self.assertTrue(consensus_reached)
        self.assertEqual(len(failed_predictions), 1)
        self.assertIsNotNone(best_prediction)
        self.assertEqual(best_prediction["action"], 1)
        self.assertEqual(best_prediction["state"], 1)

    def test_invalid_batch_predictions_and_valid_extra_vote(self) -> None:
        agent = DummyAgent(
            parse_outputs={
                "r1": ValueError("parse error"),
                "r2": (1, 1),
            },
            extra_outputs=[(1, 1)],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=2,
            batch_size=2,
            margin_k=2,
            max_agents_total=3,
        )

        self.assertTrue(consensus_reached)
        self.assertEqual(len(failed_predictions), 1)
        self.assertEqual(failed_predictions[0]["agent_id"], "2:1")
        self.assertIsNotNone(best_prediction)
        self.assertEqual(best_prediction["action"], 1)
        self.assertEqual(best_prediction["state"], 1)

    def test_no_valid_predictions_means_no_consensus(self) -> None:
        agent = DummyAgent(
            parse_outputs={
                "r1": ValueError("bad output"),
                "r2": ValueError("bad output"),
            },
            extra_outputs=[],
            initial_state=0,
        )

        candidate_voting, best_prediction, failed_predictions, consensus_reached = run_voting_batch(
            agent=agent,
            previous_move="None",
            current_state=0,
            current_step=3,
            batch_size=2,
            margin_k=1,
            max_agents_total=2,
        )

        self.assertFalse(consensus_reached)
        self.assertIsNone(best_prediction)
        self.assertEqual(candidate_voting, {})
        self.assertEqual(len(failed_predictions), 2)


if __name__ == "__main__":
    unittest.main()