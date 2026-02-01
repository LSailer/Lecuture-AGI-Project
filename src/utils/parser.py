class Parser:
    def __init__(self, environment, move_pattern, state_pattern, parse_move_fn, parse_state_fn):
        self.environment = environment
        self.move_pattern = move_pattern
        self.state_pattern = state_pattern
        self.parse_move_fn = parse_move_fn
        self.parse_state_fn = parse_state_fn

    def parse_action_state(self, response: str):
        move_matches = list(self.move_pattern.finditer(response))
        state_matches = list(self.state_pattern.finditer(response))

        if not move_matches or not state_matches:
            raise ValueError("Could not find move or next_state in the response.")

        try:
            move = self.parse_move_fn(move_matches[-1])
            state = self.parse_state_fn(state_matches[-1])
        except Exception as e:
            raise ValueError("Error parsing move or next_state") from e

        return self.environment.validate_move(move), self.environment.is_valid_state(state)
