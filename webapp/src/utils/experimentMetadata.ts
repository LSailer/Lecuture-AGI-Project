import type { GameType } from '../types/experiment';

export interface ExperimentMetadata {
  filename: string;
  gameType: GameType;
  displayName: string;
  date: string;
}

/**
 * Extracts metadata from experiment filename
 * Expected format: experiment_YYYYMMDD_HHMMSS_game_name.json
 */
export function parseExperimentMetadata(filename: string): ExperimentMetadata {
  const displayName = filename
    .replace('experiment_', '')
    .replace('.json', '');

  const parts = displayName.split('_');

  // Determine game type
  let gameType: GameType = 'tower_of_hanoi';
  if (filename.includes('sliding_puzzle')) {
    gameType = 'sliding_puzzle';
  }

  // Extract date if present
  let date = '';
  let gameName = displayName;

  if (parts.length >= 2 && parts[0].length === 8 && parts[1].length === 6) {
    const d = parts[0]; // YYYYMMDD
    const t = parts[1]; // HHMMSS
    // Format: YYYY-MM-DD HH:MM:SS
    date = `${d.substring(0,4)}-${d.substring(4,6)}-${d.substring(6,8)} ${t.substring(0,2)}:${t.substring(2,4)}:${t.substring(4,6)}`;
    gameName = parts.slice(2).join(' ').replace(/_/g, ' ');
  }

  // Capitalize game name
  const formattedName = gameName
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');

  return {
    filename,
    gameType,
    displayName: formattedName,
    date
  };
}
