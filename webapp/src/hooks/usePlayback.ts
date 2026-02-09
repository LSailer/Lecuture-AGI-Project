import { useState, useEffect, useRef, useCallback } from 'react';

export interface UsePlaybackReturn {
  currentStepIndex: number;
  isPlaying: boolean;
  play: () => void;
  pause: () => void;
  togglePlayPause: () => void;
  next: () => void;
  prev: () => void;
  goToStep: (index: number) => void;
}

export function usePlayback(totalSteps: number): UsePlaybackReturn {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const intervalRef = useRef<number | null>(null);

  const goToStep = useCallback((index: number) => {
    if (index < 0) index = 0;
    if (index >= totalSteps) index = totalSteps - 1;
    setCurrentStepIndex(index);
  }, [totalSteps]);

  const pause = useCallback(() => {
    setIsPlaying(false);
    if (intervalRef.current !== null) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  }, []);

  const play = useCallback(() => {
    if (currentStepIndex >= totalSteps - 1) {
      // If at the end, restart from beginning
      setCurrentStepIndex(0);
    }
    setIsPlaying(true);
  }, [currentStepIndex, totalSteps]);

  const togglePlayPause = useCallback(() => {
    if (isPlaying) {
      pause();
    } else {
      play();
    }
  }, [isPlaying, play, pause]);

  const next = useCallback(() => {
    pause();
    goToStep(currentStepIndex + 1);
  }, [currentStepIndex, goToStep, pause]);

  const prev = useCallback(() => {
    pause();
    goToStep(currentStepIndex - 1);
  }, [currentStepIndex, goToStep, pause]);

  // Auto-advance when playing
  useEffect(() => {
    if (isPlaying) {
      intervalRef.current = window.setInterval(() => {
        setCurrentStepIndex(current => {
          if (current >= totalSteps - 1) {
            setIsPlaying(false);
            return current;
          }
          return current + 1;
        });
      }, 1000);
    }

    return () => {
      if (intervalRef.current !== null) {
        clearInterval(intervalRef.current);
      }
    };
  }, [isPlaying, totalSteps]);

  // Reset when totalSteps changes (new experiment loaded)
  useEffect(() => {
    setCurrentStepIndex(0);
    pause();
  }, [totalSteps, pause]);

  return {
    currentStepIndex,
    isPlaying,
    play,
    pause,
    togglePlayPause,
    next,
    prev,
    goToStep
  };
}
