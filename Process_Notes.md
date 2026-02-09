# Process Notes

## Feature: WandB Integration, Fallback Mechanism & Pipeline Optimization

**Branch:** `feat/wandb-fallback-optimization`
**Date:** 2026-02-07

---

### Problem Statement

The MAKER framework had three gaps:
1. **No observability** -- no way to track experiments, compare runs, or inspect per-agent predictions across steps.
2. **No recovery when all agents fail** -- if every agent in a voting step produced an unparseable or invalid response, the solver immediately broke out of the game loop with no retry mechanism.
3. **Sequential bottleneck** -- agents were called one-by-one in the voting loop, wasting GPU throughput on a model that supports batch inference.

---

### Decisions Made

#### 1. Observability: WandB + failures.csv

- **WandB** tracks each run end-to-end: config is logged at init, a `predictions` Table captures every (step, agent, state, action, error) row, and summary metrics (`total_steps`, `solved`) are logged at the end.
- **`output/failures.csv`** is a lightweight, always-available failure log (timestamp, current_state, agent_id) written in the `Agent.parse_response()` error path. This complements WandB for quick offline debugging.

#### 2. Fallback Architecture: Gemini API + Local DeepSeek

When all agents fail a step, a **FallbackModel** rewrites the system and user prompts:

- **Fallback chain:** Gemini 2.5 Flash API (free tier) first, then local DeepSeek-R1-Distill-Qwen-32B if Gemini fails or is rate-limited.
- **Meta-prompt approach:** The fallback receives the original prompts + all failed predictions, analyzes the failure modes, and produces improved prompts in a structured `<SYSTEM_PROMPT>` / `<USER_PROMPT>` format.
- **Prompt composition:** The fallback's system prompt fully replaces the original (it's state-independent). The fallback's user prompt is **prepended** as additional guidance to the state-specific user prompt built by `agent.build_prompt()` -- this ensures game state (previous_move, current_state, step) is always present.
- **Lazy loading:** The local DeepSeek model is only loaded into VRAM when `_call_local()` is actually invoked, avoiding memory conflict with the primary Devstral model.
- **Debug tracking:** Each fallback invocation appends to `output/debug_prompts.md` with the rewritten prompts and the failures that triggered them.
- **Config-driven:** `max_fallback_retries` (default 3), `fallback_api` ("gemini" | "local" | "both"), model IDs all live in the per-game YAML configs.

#### 3. Pipeline Optimization: Batch Inference

- **`LLM.generate_batch()`** passes N message sets to the HuggingFace pipeline in a single call with `batch_size=N`. This is the primary speedup -- the GPU processes all prompts in one forward pass instead of N sequential passes.
- **`run_voting_batch()`** in main.py builds all N prompts, runs one batched LLM call, then parses responses and tallies votes. If the margin isn't met after the batch, additional single-agent tiebreaker calls are made sequentially.
- **Async for API fallback:** Gemini calls use `google-genai`'s async client (`client.aio.models.generate_content`) wrapped in a sync entrypoint that handles both event-loop and non-event-loop contexts.

#### 4. Agent Refactoring

The `Agent` class was split into three composable methods:
- `build_prompt(previous_move, current_state, step)` -- returns `(messages_list, user_prompt_str)`
- `parse_response(content, current_state, step, agent_num)` -- parses, logs to CSV + failures.csv, raises on error
- `execute_decompose_prompt(...)` -- convenience method that chains both (kept for backward compatibility and single-agent tiebreaker calls)

This separation enables batch inference (main.py builds N prompts, batches them, parses individually) without duplicating code.

#### 5. Type Annotations

All modified/created files are fully typed:
- `parser.py`: `re.Pattern`, `Callable`, `tuple[Any, Any]` returns
- `llm.py`: `Message` and `Conversation` type aliases, typed returns
- `decomposer.py`: `ModuleType` for prompts, `Conversation` for messages, `tuple[Any, Any]` for action/state
- `fallback.py`: `FailedPrediction` type alias, all methods typed with `str`, `int`, `tuple[str, str]` returns
- `main.py`: `argparse.Namespace`, `dict[str, Any]`, `wandb.Table | None`, full `run_voting_batch` signature

---

### Files Changed

| File | Action | What Changed |
|------|--------|-------------|
| `pyproject.toml` | Modified | Added `wandb`, `google-genai`, `aiohttp` dependencies |
| `src/config/tower_of_hanoi.yaml` | Modified | Added `max_fallback_retries`, `fallback_api`, `fallback_local_model`, `gemini_model` |
| `src/config/sliding_puzzle.yaml` | Modified | Same fallback config keys |
| `src/utils/parser.py` | Modified | Added type annotations |
| `src/utils/llm.py` | Modified | Added `generate_batch()`, `Message`/`Conversation` type aliases, type annotations |
| `src/utils/decomposer.py` | Modified | Split into `build_prompt()` + `parse_response()` + `execute_decompose_prompt()`, added `failures.csv` tracking, type annotations |
| `src/utils/fallback.py` | **Created** | `FallbackModel` class: Gemini async + local DeepSeek fallback chain, meta-prompt builder, debug logging |
| `src/main.py` | Modified | WandB init/table/logging, `run_voting_batch()` for batch inference, fallback retry loop, type annotations |
| `LLM/download.py` | Modified | Added DeepSeek-R1-Distill-Qwen-32B download |

---

### New Output Artifacts

| File | When Created | Purpose |
|------|-------------|---------|
| `output/failures.csv` | On agent parse errors | Quick offline failure log (timestamp, state, agent_id) |
| `output/debug_prompts.md` | On fallback invocations | Tracks rewritten prompts and the failures that triggered them |
| WandB `predictions` Table | End of each run | Per-agent prediction log viewable in WandB dashboard |

---

### Environment Requirements

- `GEMINI_API_KEY` env var required for Gemini fallback (free tier: 250 req/day)
- `HF_TOKEN` env var required for model downloads (existing requirement)
- `WANDB_API_KEY` env var or `wandb login` for experiment tracking

---

### Verification Plan

1. **WandB:** Run Tower of Hanoi (3 disks) -- verify WandB dashboard shows predictions table, config, and summary metrics
2. **failures.csv:** Temporarily break model output parsing -- verify `output/failures.csv` populates
3. **Fallback trigger:** Set `max_agents_per_step: 1` and break parsing -- verify fallback engages, `debug_prompts.md` populates, retries respect `max_fallback_retries`
4. **Batch inference:** Time 3-disk solve with sequential vs batch voting -- measure speedup
5. **Fallback chain:** Block Gemini API (invalid key) -- verify local DeepSeek loads and takes over

---

## Feature: Modern React Visualization Webapp

**Branch:** `feature/visualization-webapp`
**Date:** 2026-02-09

---

### Problem Statement

The existing vanilla JavaScript web app (`web/`) provided basic experiment visualization but lacked:
1. **Modern architecture** -- no component reusability, state management, or type safety
2. **Routing** -- couldn't share links to specific experiments or have a proper landing page
3. **Build pipeline** -- no bundling, minification, or production optimization
4. **Developer experience** -- no hot module replacement, TypeScript support, or modern tooling

---

### Decisions Made

#### 1. Tech Stack: Vite + React 18 + TypeScript + Tailwind CSS v4

- **Vite** for fast development server with HMR and optimized production builds
- **React 18** with TypeScript for component architecture and type safety
- **Tailwind CSS v4** (@tailwindcss/vite) for styling with dark theme (slate palette)
- **React Router v6** for client-side routing (landing page + experiment viewer)
- **No backend required** -- JSON data bundled directly via `import.meta.glob`

#### 2. Architecture: Component-Based with Hooks

**Type System:**
- `types/experiment.ts` defines all interfaces: `RawStep`, `DisplayStep`, `Experiment`, `GameState`, `GameType`
- Full type safety from data loading through rendering

**Data Layer:**
- `data/index.ts` uses `import.meta.glob` to auto-discover all JSON files in `src/data/experiments/`
- `parseState()` converts Python-stringified states (tuples, single quotes) to JavaScript objects
- `parseExperimentMetadata()` extracts game type, date, and display name from filename pattern

**Hooks:**
- `usePlayback()` manages currentStepIndex, isPlaying state, play/pause/next/prev/goToStep with 1-second interval
- `useKeyboardShortcuts()` registers keydown listeners for ←/→ arrows and Space bar

**Components:**
- **Visualizations:** `TowerOfHanoiRenderer` (SVG with colored disks), `SlidingPuzzleRenderer` (CSS grid), `GameStage` (dispatcher)
- **Controls:** `PlaybackControls` (buttons + slider + step counter)
- **Layout:** `Sidebar` (experiment list grouped by game type), `DetailsPanel` (votes + failures with color coding)
- **Pages:** `LandingPage` (experiment cards grid), `ExperimentPage` (3-column viewer layout)

#### 3. Visualization Design

**Tower of Hanoi:**
- 3 vertical rods with colored disks (red → orange → yellow → green → blue → violet → pink)
- Disk width proportional to size (30px + size × 20px)
- Disk numbers displayed on each disk
- CSS flexbox with `flex-col-reverse` for bottom-to-top stacking

**Sliding Puzzle:**
- CSS Grid with dynamic size based on puzzle dimensions
- 64px tiles with centered numbers
- Empty tile (0) rendered as transparent
- Dark slate background matching theme

#### 4. User Experience

**Landing Page:**
- Grid of experiment cards showing game type, name, date, and step count
- Click any card to navigate to experiment viewer
- Responsive layout (1-3 columns based on screen width)

**Experiment Viewer:**
- 3-column layout: sidebar (250px) | main visualization (flex) | details (300px)
- Full-height (100vh) app-like interface
- Playback controls with play/pause, prev/next, slider, and step counter
- Keyboard shortcuts: ←/→ for step navigation, Space for play/pause
- Auto-play advances every 1 second, stops at end

**Details Panel:**
- Chosen action highlighted with green border
- Agent votes sorted by count (descending)
- Failed predictions with red border showing agent ID and error
- Color-coded for quick visual scanning

#### 5. Build & Development

**Development:**
- `npm run dev` starts Vite dev server with HMR on http://localhost:5173/
- Fast refresh preserves component state during edits
- TypeScript compilation in watch mode

**Production:**
- `npm run build` creates optimized bundle in `webapp/dist/`
- Tree-shaking, minification, and code splitting
- CSS purging removes unused Tailwind classes
- Assets hashed for cache busting

---

### Files Created

| File | Purpose |
|------|---------|
| `webapp/vite.config.ts` | Vite configuration with React and Tailwind plugins |
| `webapp/tsconfig.json` / `tsconfig.app.json` | TypeScript configuration |
| `webapp/package.json` | Dependencies and scripts |
| `webapp/index.html` | HTML entry point with Inter font |
| `webapp/src/index.css` | Tailwind directives and custom scrollbar styles |
| `webapp/src/types/experiment.ts` | All TypeScript interfaces |
| `webapp/src/utils/parseState.ts` | Python state string parser |
| `webapp/src/utils/experimentMetadata.ts` | Filename metadata extractor |
| `webapp/src/data/index.ts` | Experiment loader with import.meta.glob |
| `webapp/src/data/experiments/*.json` | Copied experiment data (3 Tower of Hanoi runs) |
| `webapp/src/hooks/usePlayback.ts` | Playback state management hook |
| `webapp/src/hooks/useKeyboardShortcuts.ts` | Keyboard event handler hook |
| `webapp/src/components/visualizations/TowerOfHanoiRenderer.tsx` | Tower of Hanoi SVG renderer |
| `webapp/src/components/visualizations/SlidingPuzzleRenderer.tsx` | Sliding Puzzle CSS grid renderer |
| `webapp/src/components/visualizations/GameStage.tsx` | Game type dispatcher |
| `webapp/src/components/common/PlaybackControls.tsx` | Playback UI controls |
| `webapp/src/components/layout/Sidebar.tsx` | Experiment list sidebar |
| `webapp/src/components/layout/DetailsPanel.tsx` | Step details panel |
| `webapp/src/components/pages/LandingPage.tsx` | Home page with experiment cards |
| `webapp/src/components/pages/ExperimentPage.tsx` | Main experiment viewer |
| `webapp/src/App.tsx` | Router setup |
| `webapp/src/main.tsx` | React entry point |

---

### Directory Structure

```
webapp/
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── types/
│   │   └── experiment.ts
│   ├── data/
│   │   ├── experiments/
│   │   │   └── *.json
│   │   └── index.ts
│   ├── utils/
│   │   ├── parseState.ts
│   │   └── experimentMetadata.ts
│   ├── hooks/
│   │   ├── usePlayback.ts
│   │   └── useKeyboardShortcuts.ts
│   └── components/
│       ├── layout/
│       │   ├── Sidebar.tsx
│       │   └── DetailsPanel.tsx
│       ├── common/
│       │   └── PlaybackControls.tsx
│       ├── visualizations/
│       │   ├── GameStage.tsx
│       │   ├── TowerOfHanoiRenderer.tsx
│       │   └── SlidingPuzzleRenderer.tsx
│       └── pages/
│           ├── LandingPage.tsx
│           └── ExperimentPage.tsx
```

---

### Dependencies

```json
{
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^7.13.0",
    "tailwindcss": "^4.1.18",
    "@tailwindcss/vite": "^4.1.18"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^5.1.1",
    "typescript": "~5.9.3",
    "vite": "^7.3.1"
  }
}
```

---

### Data Flow

1. **App Initialization:** `loadExperiments()` in `data/index.ts` runs at module load
   - `import.meta.glob` discovers all JSON files
   - Each file is processed: parse metadata, create Step 0 from first `current_state`, map remaining steps from `processed_state`
   - Returns array of `Experiment` objects sorted by date

2. **Landing Page:** Displays experiment cards, each links to `/experiment/:filename`

3. **Experiment Viewer:**
   - URL param `:filename` used to find experiment in array
   - `usePlayback()` hook manages step index and play/pause state
   - `useKeyboardShortcuts()` connects keyboard events to playback actions
   - Current step's `parsedState` rendered by `GameStage` → specific renderer
   - `DetailsPanel` shows step's votes and failures

---

### Verification Checklist

✅ **Build:** `npm run build` succeeds with no errors
✅ **Dev Server:** `npm run dev` starts on http://localhost:5173/
✅ **Landing Page:** Shows 3 Tower of Hanoi experiment cards
✅ **Navigation:** Click card → navigates to experiment viewer
✅ **Visualization:** Tower of Hanoi disks render correctly with colors and numbers
✅ **Playback:** Play auto-advances, pause stops, slider seeks
✅ **Controls:** Prev/Next buttons work, disabled at boundaries
✅ **Keyboard:** ←/→ navigate steps, Space toggles play/pause
✅ **Details Panel:** Shows chosen action (green), votes sorted by count, failures (red)
✅ **Type Safety:** All components fully typed, no TypeScript errors

---

### Future Enhancements

- Add Sliding Puzzle experiment data and verify rendering
- Implement experiment comparison view (side-by-side)
- Add export functionality (GIF/video of playback)
- Chart/graph visualizations for agent vote distributions
- Filter/search experiments by date, game type, or success rate
- Dark/light theme toggle
