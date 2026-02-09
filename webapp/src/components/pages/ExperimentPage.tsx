import { useParams, Navigate } from 'react-router-dom';
import type { Experiment } from '../../types/experiment';
import { Sidebar } from '../layout/Sidebar';
import { DetailsPanel } from '../layout/DetailsPanel';
import { GameStage } from '../visualizations/GameStage';
import { PlaybackControls } from '../common/PlaybackControls';
import { usePlayback } from '../../hooks/usePlayback';
import { useKeyboardShortcuts } from '../../hooks/useKeyboardShortcuts';

interface Props {
  experiments: Experiment[];
}

export function ExperimentPage({ experiments }: Props) {
  const { filename } = useParams<{ filename: string }>();
  
  const experiment = experiments.find(exp => exp.filename === filename);

  const playback = usePlayback(experiment?.steps.length || 0);
  const { currentStepIndex } = playback;

  useKeyboardShortcuts({
    onLeft: playback.prev,
    onRight: playback.next,
    onSpace: playback.togglePlayPause,
  });

  if (!filename || !experiment) {
    return <Navigate to="/" replace />;
  }

  const currentStep = experiment.steps[currentStepIndex];

  return (
    <div className="h-screen grid grid-cols-[250px_1fr_300px] bg-slate-900 text-slate-50">
      <Sidebar experiments={experiments} />

      <main className="flex flex-col p-8 overflow-hidden">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-semibold mb-2">{experiment.displayName}</h1>
          <p className="text-lg text-slate-400">
            Step {currentStepIndex} / {experiment.steps.length - 1}
          </p>
        </div>

        <div className="flex-1 flex items-center justify-center bg-slate-800/30 rounded-xl border border-slate-700 mb-8 overflow-hidden">
          {currentStep && (
            <GameStage
              gameType={experiment.gameType}
              state={currentStep.parsedState}
            />
          )}
        </div>

        <PlaybackControls
          playback={playback}
          totalSteps={experiment.steps.length}
        />
      </main>

      <DetailsPanel step={currentStep} />
    </div>
  );
}
