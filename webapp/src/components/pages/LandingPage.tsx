import { Link } from 'react-router-dom';
import type { Experiment } from '../../types/experiment';

interface Props {
  experiments: Experiment[];
}

export function LandingPage({ experiments }: Props) {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-50 p-8">
      <div className="max-w-6xl mx-auto">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">Multi-Agent Experiment Viewer</h1>
          <p className="text-lg text-slate-400">
            Visualize and analyze multi-agent game-playing experiments
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {experiments.map((exp) => (
            <Link
              key={exp.filename}
              to={`/experiment/${exp.filename}`}
              className="bg-slate-800 border border-slate-700 rounded-xl p-6 hover:border-blue-500 hover:bg-slate-800/80 transition group"
            >
              <div className="mb-3">
                <span className="text-xs uppercase text-slate-400 font-semibold">
                  {exp.gameType.replace(/_/g, ' ')}
                </span>
              </div>
              
              <h3 className="text-xl font-semibold mb-2 group-hover:text-blue-400 transition">
                {exp.displayName}
              </h3>
              
              {exp.date && (
                <p className="text-sm text-slate-400 mb-3">{exp.date}</p>
              )}
              
              <div className="flex items-center justify-between text-sm">
                <span className="text-slate-400">
                  {exp.steps.length - 1} steps
                </span>
                <span className="text-blue-400 group-hover:translate-x-1 transition">
                  View →
                </span>
              </div>
            </Link>
          ))}
        </div>

        {experiments.length === 0 && (
          <div className="text-center text-slate-400 py-12">
            <p>No experiments found. Add JSON experiment files to get started.</p>
          </div>
        )}
      </div>
    </div>
  );
}
