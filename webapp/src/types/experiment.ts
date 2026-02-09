// Raw JSON file structure
export interface RawExperimentData {
  game_type: GameType;
  steps: RawStep[];
}

// Raw step data from JSON files
export interface RawStep {
  step: number;
  current_state: string;
  processed_state: string;
  agent_votes: Record<string, number>;
  best_action: string;
  failed_predictions: FailedPrediction[];
}

export interface FailedPrediction {
  agent_id: string;
  action: string;
  state: string;
  error: string;
}

// Game types
export type GameType = "tower_of_hanoi" | "sliding_puzzle";

// Tower of Hanoi state: array of 3 towers, each tower is an array of disk numbers
export interface TowerOfHanoiState {
  towers: number[][];
}

// Sliding Puzzle state: flat array of tiles with 0 representing empty space
export interface SlidingPuzzleState {
  tiles: number[];
  gridSize: number;
}

// Union type for all game states
export type GameState = TowerOfHanoiState | SlidingPuzzleState;

// Processed step ready for rendering
export interface DisplayStep {
  stepNumber: number;
  state: string; // Original string representation
  parsedState: GameState; // Parsed state object
  action: string | null;
  votes: Record<string, number> | null;
  failed: FailedPrediction[];
  explanation?: string;
}

// Complete experiment with metadata
export interface Experiment {
  filename: string;
  gameType: GameType;
  displayName: string;
  date: string;
  steps: DisplayStep[];
}
