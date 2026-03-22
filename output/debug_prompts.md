
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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

---

## Fallback at Step 1, Retry 1

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

### Failed Predictions
- Agent 1:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


## Original User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

## Failed Predictions
  - Agent 1:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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
[None]

---

## Actual LLM Prompt at Step 1 (fallback)

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

---

## Fallback at Step 1, Retry 2

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

### Failed Predictions
- Agent 1:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


## Original User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

## Failed Predictions
  - Agent 1:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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
[None]

---

## Actual LLM Prompt at Step 1 (fallback)

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

---

## Fallback at Step 1, Retry 3

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

### Failed Predictions
- Agent 1:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 1:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


## Original User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

## Failed Predictions
  - Agent 1:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 1:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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
[None]

---

## Actual LLM Prompt at Step 1 (fallback)

### System Prompt
You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY: The lookup table is sorted best-first. Always pick the FIRST entry.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the LOOKUP TABLE in the user prompt. Do NOT compute it yourself.


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: None

Current state:
BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

MOVE->NEXT_STATE LOOKUP TABLE (first entry = best move):
  U' : WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB  [score=17]
  R' : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B' : OOYWWWWWWGGBRRBRRBOOOGGWGGWYYGYYGRRWYBBYOOGOORBBRBBRYY  [score=11]
  B2 : GYYWWWWWWGGORRORRYOOOGGWGGWYYGYYGBBBRBBROOWOOBBYBBYRRR  [score=11]
  U  : BWWBWWBWWOOORRRRRRYBBGGWGGWYYGYYGYYGRRROOOOOOGGWYBBYBB  [score=9]
  U2 : WWWWWWBBBYBBRRRRRRRRRGGWGGWYYGYYGYYGGGWOOOOOOOOOYBBYBB  [score=9]
  R  : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]
  R2 : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  F  : BBBWWWOOBWGWWRRWRRGGOGGOWWORRGYYGYYGYBYOOYOOGRRRYBBYBB  [score=9]
  F2 : BBBWWWGYYOGWORRBRRWGGWGGOOOWWWYYGYYGYBROOROOGRRRYBBYBB  [score=9]
  D  : BBBWWWWWWGGWRRRYBBOOOGGWRRRGGGYYYYYYYBBOOOGGWRRRYBBOOO  [score=9]
  D' : BBBWWWWWWGGWRRRGGWOOOGGWOOOYYYYYYGGGYBBOOOYBBRRRYBBRRR  [score=9]
  D2 : BBBWWWWWWGGWRRROOOOOOGGWYBBGYYGYYGYYYBBOOORRRRRRYBBGGW  [score=9]
  L  : OBBGWWGWWGGWRRRRRRYOOYGWYGWBYGBYGRYGBOOBOOYOORRWYBWYBB  [score=9]
  L' : BBBBWWRWWGGWRRRRRRBOOWGWWGWOYGGYGGYGOOYOOBOOBRRYYBYYBY  [score=9]
  L2 : YBBYWWYWWGGWRRRRRRBOOBGWRGWBYGWYGWYGOOOOOOBBYRRGYBGYBO  [score=9]
  B  : WRRWWWWWWGGGRRYRRYOOOGGWGGWYYGYYGYOOBBBBOOBOOYYRBBRBBR  [score=9]
  F' : BBBWWWGRRGGWYRRYRROWWOGGOGGBOOYYGYYGYBWOOWOOWRRRYBBYBB  [score=7]

INSTRUCTION: Pick the FIRST move in the table. Copy its next_state EXACTLY from the table above.
Do NOT compute next_state yourself. Copy the 54-character string character-by-character.
Output EXACTLY TWO LINES:
move = <first move in table>
next_state = <exact 54-char next_state from first line of table>

---
