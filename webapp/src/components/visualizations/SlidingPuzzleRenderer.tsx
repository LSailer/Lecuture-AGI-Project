import type { SlidingPuzzleState } from '../../types/experiment';

interface Props {
  state: SlidingPuzzleState;
}

export function SlidingPuzzleRenderer({ state }: Props) {
  const { tiles, gridSize } = state;

  return (
    <div className="flex items-center justify-center">
      <div
        className="grid gap-1.5 bg-slate-700 p-2.5 rounded-lg"
        style={{
          gridTemplateColumns: `repeat(${gridSize}, 64px)`,
          gridTemplateRows: `repeat(${gridSize}, 64px)`
        }}
      >
        {tiles.map((tile, index) => (
          <div
            key={index}
            className={`
              flex items-center justify-center
              text-2xl font-bold rounded
              ${tile === 0 
                ? 'bg-transparent text-transparent' 
                : 'bg-slate-800 text-slate-50'
              }
            `}
          >
            {tile !== 0 && tile}
          </div>
        ))}
      </div>
    </div>
  );
}
