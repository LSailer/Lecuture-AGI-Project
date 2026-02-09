import type { DisplayStep } from '../../types/experiment';

interface Props {
  step: DisplayStep | null;
}

export function DetailsPanel({ step }: Props) {
  if (!step) {
    return (
      <aside className="bg-slate-800 border-l border-slate-700 p-4">
        <h3 className="text-lg font-semibold mb-4 pb-4 border-b border-slate-700">
          Step Details
        </h3>
        <p className="text-slate-400">Select an experiment to view details</p>
      </aside>
    );
  }

  if (step.stepNumber === 0) {
    return (
      <aside className="bg-slate-800 border-l border-slate-700 p-4 overflow-y-auto">
        <h3 className="text-lg font-semibold mb-4 pb-4 border-b border-slate-700">
          Step Details
        </h3>
        <p className="text-slate-400">Initial State (No actions yet)</p>
      </aside>
    );
  }

  // Sort votes by count (descending)
  const sortedVotes = step.votes
    ? Object.entries(step.votes).sort((a, b) => b[1] - a[1])
    : [];

  return (
    <aside className="bg-slate-800 border-l border-slate-700 p-4 overflow-y-auto">
      <h3 className="text-lg font-semibold mb-4 pb-4 border-b border-slate-700">
        Step Details
      </h3>

      {/* Chosen Action */}
      <div className="mb-6">
        <h4 className="text-xs uppercase text-slate-400 font-semibold mb-2">
          Chosen Action
        </h4>
        <div className="bg-slate-900/50 p-3 rounded-lg border border-green-500/50">
          <strong className="text-green-400 font-mono">{step.action}</strong>
        </div>
      </div>

      {/* Agent Votes */}
      {sortedVotes.length > 0 && (
        <div className="mb-6">
          <h4 className="text-xs uppercase text-slate-400 font-semibold mb-2">
            Agent Votes
          </h4>
          <div className="space-y-2">
            {sortedVotes.map(([action, count]) => {
              const isChosen = action === step.action;
              return (
                <div
                  key={action}
                  className={`bg-slate-900/50 p-3 rounded-lg ${
                    isChosen ? 'border border-green-500/50' : 'border border-slate-700'
                  }`}
                >
                  <div className="font-mono text-sm">{action}</div>
                  <div className="text-xs text-slate-400 mt-1">Votes: {count}</div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Failed Predictions */}
      {step.failed && step.failed.length > 0 && (
        <div>
          <h4 className="text-xs uppercase text-slate-400 font-semibold mb-2">
            Failed Predictions
          </h4>
          <div className="space-y-2">
            {step.failed.map((fail, idx) => (
              <div
                key={idx}
                className="bg-slate-900/50 p-3 rounded-lg border border-red-500/50 text-sm"
              >
                <div className="text-red-400 font-medium">Agent {fail.agent_id}</div>
                <div className="text-xs text-slate-400 mt-1">Error: {fail.error}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </aside>
  );
}
