
## Actual LLM Prompt at Step 1 (default)

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Moves:
- Allowed moves are EXACTLY: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>


---

## Fallback at Step 1, Retry 1

### System Prompt
You are a Rubik's Cube solver assistant. Your primary task is to propose the next move and accurately calculate the resulting cube state.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times in any valid cube state.

Moves:
- Allowed moves are EXACTLY: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STATE_VISUAL_FORMAT:
This is a 2D unfolded representation of the cube, providing a visual aid for reasoning.
Each character in the visual represents a sticker color, corresponding to the 54-character state string.

        U0 U1 U2
        U3 U4 U5
        U6 U7 U8
L36 L37 L38 F18 F19 F20 R9 R10 R11 B45 B46 B47
L39 L40 L41 F21 F22 F23 R12 R13 R14 B48 B49 B50
L42 L43 L44 F24 F25 F26 R15 R16 R17 B51 B52 B53
        D27 D28 D29
        D30 D31 D32
        D33 D34 D35

The placeholder {state_visual} in the User Prompt will be replaced by the current cube's state rendered in this format.

REQUIREMENTS (STRICT):
- The `next_state` MUST be the precise result of applying the chosen `move` to the `current_state`. **Inconsistent predictions will result in failure.** Double-check your `next_state` calculation carefully.
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).

### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Current state visual:
      BBB
      WWW
      WWW
YBB OOO GGW RRR
OOO GGW RRR YBB
OOO GGW RRR YBB
      YYG
      YYG
      YYG

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>

### Failed Predictions
- Agent 1:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

### Meta Prompt Sent To Fallback
You are a prompt-engineering expert. A multi-agent voting system is trying to solve
a puzzle. All agents failed on the current step. Your job is to analyze the failures
and produce improved system and user prompts that will help the agents reason better.

## Original System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Moves:
- Allowed moves are EXACTLY: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


## Original User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>


## Failed Predictions
  - Agent 1:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

## Instructions
1. Analyze why the agents failed (wrong parsing, bad reasoning, invalid moves, etc.).
2. Produce an improved system prompt and user prompt that address the failure modes.
3. Keep the same output format requirements (move = [...], next_state = [...]).
4. You CAN and SHOULD use the placeholders `{current_state}`, `{previous_move}`, and `{state_visual}` (if applicable) in your improved user prompt. Do NOT hardcode the state from the failed step.
5. Output your response in EXACTLY this format:

<SYSTEM_PROMPT>
(your improved system prompt here)
</SYSTEM_PROMPT>

<USER_PROMPT>
(your improved user prompt here)
</USER_PROMPT>


### Fallback Raw Response
<SYSTEM_PROMPT>
You are a Rubik's Cube solver assistant. Your primary task is to propose the next move and accurately calculate the resulting cube state.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times in any valid cube state.

Moves:
- Allowed moves are EXACTLY: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STATE_VISUAL_FORMAT:
This is a 2D unfolded representation of the cube, providing a visual aid for reasoning.
Each character in the visual represents a sticker color, corresponding to the 54-character state string.

        U0 U1 U2
        U3 U4 U5
        U6 U7 U8
L36 L37 L38 F18 F19 F20 R9 R10 R11 B45 B46 B47
L39 L40 L41 F21 F22 F23 R12 R13 R14 B48 B49 B50
L42 L43 L44 F24 F25 F26 R15 R16 R17 B51 B52 B53
        D27 D28 D29
        D30 D31 D32
        D33 D34 D35

The placeholder {state_visual} in the User Prompt will be replaced by the current cube's state rendered in this format.

REQUIREMENTS (STRICT):
- The `next_state` MUST be the precise result of applying the chosen `move` to the `current_state`. **Inconsistent predictions will result in failure.** Double-check your `next_state` calculation carefully.
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: {previous_move}
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
{current_state}

Current state visual:
{state_visual}

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
</USER_PROMPT>

---

## Actual LLM Prompt at Step 1 (fallback)

### System Prompt
You are a Rubik's Cube solver assistant. Your primary task is to propose the next move and accurately calculate the resulting cube state.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times in any valid cube state.

Moves:
- Allowed moves are EXACTLY: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2.
- U means rotate the U face 90° clockwise when looking at the U face from outside.
- U' is counter-clockwise, U2 is 180°. Same for R,F,D,L,B.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STATE_VISUAL_FORMAT:
This is a 2D unfolded representation of the cube, providing a visual aid for reasoning.
Each character in the visual represents a sticker color, corresponding to the 54-character state string.

        U0 U1 U2
        U3 U4 U5
        U6 U7 U8
L36 L37 L38 F18 F19 F20 R9 R10 R11 B45 B46 B47
L39 L40 L41 F21 F22 F23 R12 R13 R14 B48 B49 B50
L42 L43 L44 F24 F25 F26 R15 R16 R17 B51 B52 B53
        D27 D28 D29
        D30 D31 D32
        D33 D34 D35

The placeholder {state_visual} in the User Prompt will be replaced by the current cube's state rendered in this format.

REQUIREMENTS (STRICT):
- The `next_state` MUST be the precise result of applying the chosen `move` to the `current_state`. **Inconsistent predictions will result in failure.** Double-check your `next_state` calculation carefully.
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).

### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Current state visual:
      BBB
      WWW
      WWW
YBB OOO GGW RRR
OOO GGW RRR YBB
OOO GGW RRR YBB
      YYG
      YYG
      YYG

Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>

---
