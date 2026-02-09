import { Link, useParams } from 'react-router-dom';
import type { Experiment } from '../../types/experiment';

interface Props {
  experiments: Experiment[];
}

export function Sidebar({ experiments }: Props) {
  const { filename } = useParams<{ filename: string }>();

  // Group experiments by game type
  const grouped = experiments.reduce((acc, exp) => {
    if (!acc[exp.gameType]) {
      acc[exp.gameType] = [];
    }
    acc[exp.gameType].push(exp);
    return acc;
  }, {} as Record<string, Experiment[]>);

  return (
    <aside className="bg-slate-800 border-r border-slate-700 flex flex-col">
      <div className="p-4 border-b border-slate-700">
        <h2 className="text-lg font-semibold">Experiments</h2>
      </div>

      <div className="flex-1 overflow-y-auto">
        {Object.entries(grouped).map(([gameType, exps]) => (
          <div key={gameType} className="mb-4">
            <div className="px-4 py-2 text-xs uppercase text-slate-400 font-semibold">
              {gameType.replace(/_/g, ' ')}
            </div>
            <ul className="space-y-0">
              {exps.map((exp) => (
                <li key={exp.filename}>
                  <Link
                    to={`/experiment/${exp.filename}`}
                    className={`block px-4 py-3 text-sm border-b border-slate-700 hover:bg-slate-700/50 transition ${
                      filename === exp.filename
                        ? 'bg-blue-500/20 border-l-4 border-l-blue-500'
                        : ''
                    }`}
                  >
                    <div className="font-medium">{exp.displayName}</div>
                    {exp.date && (
                      <div className="text-xs text-slate-400 mt-1">{exp.date}</div>
                    )}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </aside>
  );
}
