import { useEffect } from 'react';

export interface KeyboardShortcutHandlers {
  onLeft?: () => void;
  onRight?: () => void;
  onSpace?: () => void;
}

export function useKeyboardShortcuts(handlers: KeyboardShortcutHandlers) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowLeft' && handlers.onLeft) {
        e.preventDefault();
        handlers.onLeft();
      } else if (e.key === 'ArrowRight' && handlers.onRight) {
        e.preventDefault();
        handlers.onRight();
      } else if (e.key === ' ' && handlers.onSpace) {
        e.preventDefault();
        handlers.onSpace();
      }
    };

    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handlers]);
}
