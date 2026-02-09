import type { Experiment, RawStep, RawExperimentData, DisplayStep, GameType } from '../types/experiment';
import { parseExperimentMetadata } from '../utils/experimentMetadata';
import { parseState } from '../utils/parseState';

// Auto-discover all JSON files in experiments directory
// Support both old format (RawStep[]) and new format (RawExperimentData)
const experimentFiles = import.meta.glob<RawStep[] | RawExperimentData>('./experiments/*.json', {
  eager: true,
  import: 'default'
});

/**
 * Processes raw JSON data into a complete Experiment object
 */
function processExperiment(filename: string, rawData: RawStep[] | RawExperimentData): Experiment {
  // Determine format and extract data
  let gameType: GameType;
  let rawSteps: RawStep[];

  if (Array.isArray(rawData)) {
    // Old format: array of steps (infer game type from filename)
    rawSteps = rawData;
    const metadata = parseExperimentMetadata(filename);
    gameType = metadata.gameType;
  } else {
    // New format: object with game_type and steps
    gameType = rawData.game_type;
    rawSteps = rawData.steps;
  }

  const metadata = parseExperimentMetadata(filename);

  // Override gameType with one from JSON if available
  metadata.gameType = gameType;

  const steps: DisplayStep[] = [];

  // Step 0: Initial state from first step's current_state
  if (rawSteps.length > 0) {
    steps.push({
      stepNumber: 0,
      state: rawSteps[0].current_state,
      parsedState: parseState(rawSteps[0].current_state, gameType),
      action: null,
      votes: null,
      failed: [],
      explanation: 'Initial State'
    });
  }

  // Steps 1..N: Use processed_state from each step
  rawSteps.forEach(raw => {
    steps.push({
      stepNumber: raw.step,
      state: raw.processed_state,
      parsedState: parseState(raw.processed_state, gameType),
      action: raw.best_action,
      votes: raw.agent_votes,
      failed: raw.failed_predictions
    });
  });

  return {
    ...metadata,
    steps
  };
}

/**
 * Load all experiments
 */
export function loadExperiments(): Experiment[] {
  const experiments: Experiment[] = [];

  for (const path in experimentFiles) {
    const rawData = experimentFiles[path];
    const filename = path.split('/').pop() || '';

    if (rawData && filename) {
      const experiment = processExperiment(filename, rawData);
      experiments.push(experiment);
    }
  }

  // Sort by date descending (newest first)
  experiments.sort((a, b) => b.date.localeCompare(a.date));

  return experiments;
}
