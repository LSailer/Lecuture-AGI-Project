import type { GameState, GameType, TowerOfHanoiState, SlidingPuzzleState } from '../types/experiment';

/**
 * Parses Python-stringified state into a JavaScript object
 * Converts:
 * - Python tuples (...) to JSON arrays [...]
 * - Single quotes to double quotes
 * - Handles both flat and nested representations
 */
export function parseState(stateStr: string, gameType: GameType): GameState {
  // Clean up the string: convert Python syntax to JSON
  let clean = stateStr
    .replace(/\(/g, '[')
    .replace(/\)/g, ']')
    .replace(/'/g, '"');

  try {
    const parsed = JSON.parse(clean);

    if (gameType === 'tower_of_hanoi') {
      return {
        towers: parsed as number[][]
      } as TowerOfHanoiState;
    } else if (gameType === 'sliding_puzzle') {
      // Handle both flat [1, 2, 3, 4, 5, 0, 7, 8, 6] and nested [[1,2,3],[4,5,0],[7,8,6]]
      if (Array.isArray(parsed[0])) {
        // Nested format - flatten it
        const tiles = (parsed as number[][]).flat();
        const gridSize = parsed.length;
        return { tiles, gridSize } as SlidingPuzzleState;
      } else {
        // Already flat format
        const tiles = parsed as number[];
        const gridSize = Math.sqrt(tiles.length);
        return { tiles, gridSize } as SlidingPuzzleState;
      }
    }
  } catch (error) {
    console.error('Failed to parse state:', stateStr, error);
  }

  // Fallback
  return gameType === 'tower_of_hanoi'
    ? { towers: [[], [], []] } as TowerOfHanoiState
    : { tiles: [], gridSize: 3 } as SlidingPuzzleState;
}
