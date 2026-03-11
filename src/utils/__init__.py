class CycleDetectedError(Exception):
    """Raised when a state has been revisited more than max_state_revisits times."""
    pass
