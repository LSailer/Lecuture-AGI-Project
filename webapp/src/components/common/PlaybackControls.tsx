import type { UsePlaybackReturn } from '../../hooks/usePlayback';

interface Props {
  playback: UsePlaybackReturn;
  totalSteps: number;
}

export function PlaybackControls({ playback, totalSteps }: Props) {
  const { currentStepIndex, isPlaying, togglePlayPause, prev, next, goToStep } = playback;

  return (
    <div className="flex items-center justify-center gap-4 p-4 bg-slate-800 rounded-xl border border-slate-700">
      <button
        onClick={prev}
        disabled={currentStepIndex === 0}
        className="px-4 py-2 rounded-lg border border-slate-600 bg-transparent text-slate-50 font-medium hover:bg-slate-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
      >
        Previous
      </button>

      <button
        onClick={togglePlayPause}
        className={`px-6 py-2 rounded-lg font-medium transition ${
          isPlaying
            ? 'bg-transparent border border-slate-600 text-slate-50 hover:bg-slate-700'
            : 'bg-blue-500 border border-blue-500 text-white hover:bg-blue-600'
        }`}
      >
        {isPlaying ? 'Pause' : 'Play'}
      </button>

      <button
        onClick={next}
        disabled={currentStepIndex === totalSteps - 1}
        className="px-4 py-2 rounded-lg border border-slate-600 bg-transparent text-slate-50 font-medium hover:bg-slate-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
      >
        Next
      </button>

      <input
        type="range"
        min={0}
        max={totalSteps - 1}
        value={currentStepIndex}
        onChange={(e) => goToStep(parseInt(e.target.value))}
        className="w-64 accent-blue-500"
      />

      <span className="text-slate-300 font-medium min-w-[80px] text-center">
        {currentStepIndex} / {totalSteps - 1}
      </span>
    </div>
  );
}
