import type { GameType, GameState } from '../../types/experiment';
import { TowerOfHanoiRenderer } from './TowerOfHanoiRenderer';
import { SlidingPuzzleRenderer } from './SlidingPuzzleRenderer';

interface Props {
  gameType: GameType;
  state: GameState;
}

export function GameStage({ gameType, state }: Props) {
  if (gameType === 'tower_of_hanoi') {
    return <TowerOfHanoiRenderer state={state as any} />;
  } else if (gameType === 'sliding_puzzle') {
    return <SlidingPuzzleRenderer state={state as any} />;
  }

  return (
    <div className="text-slate-400 text-center">
      <p>Unknown game type: {gameType}</p>
    </div>
  );
}
