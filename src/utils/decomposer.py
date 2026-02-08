from typing import Any
from types import ModuleType

from utils.llm import LLM, Conversation, Message
from utils.parser import Parser
import csv
import os
from datetime import datetime


class Agent:
    def __init__(
        self, environment: Any, prompts_module: ModuleType, device: str = "cpu"
    ) -> None:
        self.environment = environment
        self.prompts = prompts_module
        self.system_prompt: str = prompts_module.get_system_prompt(environment)
        self.llm = LLM(device=device)
        self.output_parser = Parser(
            environment=environment,
            move_pattern=prompts_module.MOVE_PATTERN,
            state_pattern=prompts_module.STATE_PATTERN,
            parse_move_fn=prompts_module.parse_move,
            parse_state_fn=prompts_module.parse_state,
        )

    def build_prompt(
        self, previous_move: str, current_state: Any, step: int = 0
    ) -> tuple[Conversation, str]:
        """Build the messages list for a single agent call (for batching)."""
        user_prompt: str = self.prompts.build_user_prompt(
            current_state=current_state,
            previous_move=previous_move,
            environment=self.environment,
            step=step,
        )
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
        ], user_prompt

    def parse_response(
        self,
        response_content: str,
        current_state: Any,
        step: int = 0,
        agent_num: int = 0,
    ) -> tuple[Any, Any]:
        """Parse a single LLM response. Returns (action, parsed_state) or raises ValueError."""
        action: Any = "None"
        parsed_state: Any = "None"
        error_message: str = "None"

        try:
            action, parsed_state = self.output_parser.parse_action_state(
                response_content
            )
        except Exception as e:
            error_message = str(e)
            # Track failures to failures.csv
            failures_file = os.path.join("output", "failures.csv")
            os.makedirs("output", exist_ok=True)
            failures_exists = os.path.isfile(failures_file)
            with open(failures_file, mode="a", newline="") as ff:
                fw = csv.writer(ff)
                if not failures_exists:
                    fw.writerow(["timestamp", "current_state", "agent_id"])
                fw.writerow(
                    [
                        datetime.now().isoformat(),
                        current_state,
                        f"{step}:{agent_num}",
                    ]
                )

        if error_message == "None":
            valid_moves_file = os.path.join("output", "valid_moves.csv")
            os.makedirs("output", exist_ok=True)
            valid_exists = os.path.isfile(valid_moves_file)
            with open(valid_moves_file, mode="a", newline="") as vf:
                vw = csv.writer(vf)
                if not valid_exists:
                    vw.writerow(["step", "agent_num", "action", "parsed_state"])
                vw.writerow([step, agent_num, action, parsed_state])

        # Log to CSV
        log_file = "output/log.csv"
        os.makedirs("output", exist_ok=True)
        file_exists = os.path.isfile(log_file)

        with open(log_file, mode="a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(
                    [
                        "step",
                        "number_agent",
                        "response",
                        "predicted_action",
                        "predicted_state",
                        "error_message",
                    ]
                )
            writer.writerow(
                [step, agent_num, response_content, action, parsed_state, error_message]
            )

        if error_message != "None":
            raise ValueError(error_message)

        return action, parsed_state

    def execute_decompose_prompt(
        self, previous_move: str, current_state: Any, step: int = 0, agent_num: int = 0
    ) -> tuple[Any, Any]:
        """Single-agent call: build prompt, generate, parse. Kept for backward compat."""
        messages, _user_prompt = self.build_prompt(previous_move, current_state, step)
        response: list[Message] = self.llm.generate(
            messages[0]["content"], messages[1]["content"]
        )
        content: str = response[-1]["content"]
        return self.parse_response(content, current_state, step, agent_num)
