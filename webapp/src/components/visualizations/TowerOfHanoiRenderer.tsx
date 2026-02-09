import type { TowerOfHanoiState } from '../../types/experiment';

interface Props {
  state: TowerOfHanoiState;
}

const DISK_COLORS = [
  '#ef4444', // red
  '#f97316', // orange
  '#eab308', // yellow
  '#22c55e', // green
  '#3b82f6', // blue
  '#8b5cf6', // violet
  '#ec4899', // pink
];

export function TowerOfHanoiRenderer({ state }: Props) {
  return (
    <div className="flex items-end justify-center gap-8 h-80 w-full px-8">
      {state.towers.map((tower, rodIndex) => (
        <div key={rodIndex} className="relative flex flex-col-reverse items-center gap-0.5">
          {/* Rod */}
          <div className="w-5 h-64 bg-slate-500 rounded-t-lg" />
          
          {/* Base */}
          <div className="absolute -bottom-5 w-32 h-5 bg-slate-600 rounded-md" />
          
          {/* Disks */}
          <div className="absolute bottom-0 flex flex-col-reverse items-center gap-0.5 pb-1">
            {tower.map((diskSize) => {
              const width = 30 + diskSize * 20;
              const color = DISK_COLORS[(diskSize - 1) % DISK_COLORS.length];
              
              return (
                <div
                  key={`${rodIndex}-${diskSize}`}
                  className="h-6 rounded flex items-center justify-center font-bold text-white text-sm shadow-lg"
                  style={{
                    width: `${width}px`,
                    backgroundColor: color
                  }}
                >
                  {diskSize}
                </div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}
