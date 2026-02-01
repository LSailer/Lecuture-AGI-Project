from utils.llm import LLM
from utils.parser import Parser
import csv
import os


class Agent:
    def __init__(self, environment, prompts_module, device="cpu"):
        self.environment = environment
        self.prompts = prompts_module
        self.system_prompt = prompts_module.get_system_prompt(environment)
        self.llm = LLM(device=device)
        self.output_parser = Parser(
            environment=environment,
            move_pattern=prompts_module.MOVE_PATTERN,
            state_pattern=prompts_module.STATE_PATTERN,
            parse_move_fn=prompts_module.parse_move,
            parse_state_fn=prompts_module.parse_state,
        )

    def execute_decompose_prompt(
        self, previous_move, current_state, step=0, agent_num=0
    ):
        user_prompt = self.prompts.build_user_prompt(
            current_state=current_state,
            previous_move=previous_move,
            environment=self.environment,
            step=step,
        )
        response = self.llm.generate(self.system_prompt, user_prompt)
        content = response[-1]["content"]

        action = "None"
        parsed_state = "None"
        error_message = "None"

        try:
            action, parsed_state = self.output_parser.parse_action_state(content)
        except Exception as e:
            error_message = str(e)

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
                [step, agent_num, content, action, parsed_state, error_message]
            )

        if error_message != "None":
            raise ValueError(error_message)

        return action, parsed_state
