
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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 1
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 15
Previous move: None

Current state:
WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWBWWWWWYRGWRRRWRRRRBGGBGGOYYGYYGYYGOOGOOOOOORBBYBBYBB  [score=15]
  R' : WWGWWGWWGRRWRRRWGRRRYGGYGGRYYBYYWYYYOOGOOOOOOOBBBBBBBB  [score=15]
  R2 : WWYWWYWWRWRRGRRRRWRRBGGWGGYYYBYYBYYOOOGOOOOOOGBBGBBGBB  [score=15]
  F  : WWBWWBOOGWRRWRGORWGGRGGRGGGRRWYYYYYROOYOOYOOYYBBWBBBBB  [score=15]
  F' : WWBWWBWRRYRRYRGYRWGGGRGGRGGGOOYYYYYROOOOOWOOWYBBWBBBBB  [score=15]
  F2 : WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB  [score=15]
  D  : WWBWWBWWOWRRRRGBBBRRGGGGRRWYYRYYYYYYOOGOOOGGGYBBWBBOOO  [score=15]
  D' : WWBWWBWWOWRRRRGGGGRRGGGGOOOYYYYYYRYYOOGOOOBBBYBBWBBRRW  [score=15]
  D2 : WWBWWBWWOWRRRRGOOORRGGGGBBBRYYYYYYYYOOGOOORRWYBBWBBGGG  [score=15]
  L  : RWBGWBGWOWRRRRGRRWYRGYGGYGGBYYBYYBYRGOOOOOOOOYBWWBWBBW  [score=13]
  L' : BWBBWBBWOWRRRRGRRWWRGWGGWGGRYYGYYGYROOOOOOOOGYBYWBYBBY  [score=13]
  L2 : YWBYWBYWOWRRRRGRRWBRGBGGBGGWYYWYYWYROOOOOOGOOYBGWBGBBR  [score=13]
  B' : OOOWWBWWOWRWRRWRRBRRGGGGGGGYYYYYYWGRYOGYOOROOBBBBBBYWB  [score=13]
  B2 : RYYWWBWWOWRORRORRORRGGGGGGGYYYYYYBWWWOGGOOROOBBBBBWBBY  [score=13]
  U  : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  B  : RGWWWBWWOWRRRRYRRYRRGGGGGGGYYYYYYOOOBOGWOOWOOBWYBBBBBB  [score=11]
  U' : WWWWWWOBBYBBRRGRRWWRRGGGGGGYYYYYYYYRRRGOOOOOOOOGWBBBBB  [score=9]
  U2 : OWWBWWBWWOOGRRGRRWYBBGGGGGGYYYYYYYYRWRROOOOOORRGWBBBBB  [score=9]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 2 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 2
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U'

Current state:
WWWWWWOBBYBBRRGRRWWRRGGGGGGYYYYYYYYRRRGOOOOOOOOGWBBBBB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  F  : WWWWWWOOGOBBBRGBRWGGWGGRGGRRRYYYYYYRRRYOOYOOYOOGWBBBBB  [score=11]
  F' : WWWWWWYRRYBBYRGYRWRGGRGGWGGGOOYYYYYRRRBOOBOOOOOGWBBBBB  [score=11]
  F2 : WWWWWWYYYOBBORGGRWGGGGGGRRWBBOYYYYYRRRROOROOYOOGWBBBBB  [score=11]
  U' : OWWBWWBWWOOGRRGRRWYBBGGGGGGYYYYYYYYRWRROOOOOORRGWBBBBB  [score=9]
  R  : WWBWWWOBOBGWBRRYRRWRWGGWGGBYYRYYGYYGRRGOOOOOOROGYBBYBB  [score=9]
  R' : WWRWWGOBGRRYRRBWGBWRYGGYGGRYYBYYWYYORRGOOOOOOBOGWBBWBB  [score=9]
  R2 : WWYWWYOBRWRRGRRBBYWRBGGWGGOYYWYYWYYBRRGOOOOOOGOGGBBRBB  [score=9]
  D  : WWWWWWOBBYBBRRGBBBWRRGGGRRWYYRYYYYYYRRGOOOGGGOOGWBBOOO  [score=9]
  D' : WWWWWWOBBYBBRRGGGGWRRGGGOOOYYYYYYRYYRRGOOOBBBOOGWBBRRW  [score=9]
  D2 : WWWWWWOBBYBBRRGOOOWRRGGGBBBRYYYYYYYYRRGOOORRWOOGWBBGGG  [score=9]
  L  : WWWGWWGBBYBBRRGRRWYRRYGGYGGBYYBYYGYRGOOROOROOOOOWBWBBW  [score=9]
  L' : BWWBWWGBBYBBRRGRRWWRRWGGOGGWYYGYYGYROOROOROOGOOYWBYBBY  [score=9]
  L2 : YWWYWWYBBYBBRRGRRWBRRBGGGGGWYYWYYOYROOOOOOGRROOGWBGBBW  [score=9]
  B' : OORWWWOBBYBWRRWRRWWRRGGGGGGYYYYYYWGBYRGYOOROOGBBOBBOWB  [score=9]
  B2 : RYYWWWOBBYBORRORRRWRRGGGGGGYYYYYYWWWWRGGOOBOOBBBBBWGOO  [score=9]
  B  : BGWWWWOBBYBRRRYRRYWRRGGGGGGYYYYYYROOWRGWOOWOOBWOBBOBBG  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 3 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 11
Previous move: U2

Current state:
BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U' : WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB  [score=15]
  B' : OOYWWWWWWRRBRRBRROOOGGGGGGGYYYYYYWGGYBBYOOROORBBRBBWWB  [score=13]
  B2 : RYYWWWWWWRRORRORRYOOGGGGGGGYYYYYYOBBWBBGOOGOOBBBBBWRRW  [score=13]
  F  : BBOWWWOOBWRGWRGWRWGGOGGOGGGRRRYYYYYRYBYOOYOOYWRRWBBBBB  [score=11]
  F' : BBOWWWRRRYRGYRGYRWGGGOGGOGGBOOYYYYYRYBWOOWOOWWRRWBBBBB  [score=11]
  F2 : BBOWWWYYYORGORGBRWGGGGGGGOOWWWYYYYYRYBROOROORWRRWBBBBB  [score=11]
  D  : BBOWWWWWWRRGRRGBBBOOGGGGRRWYYRYYYYYYYBBOOOGGGWRRWBBOOO  [score=11]
  D' : BBOWWWWWWRRGRRGGGGOOGGGGOOOYYYYYYRYYYBBOOOBBBWRRWBBRRW  [score=11]
  D2 : BBOWWWWWWRRGRRGOOOOOGGGGBBBRYYYYYYYYYBBOOORRWWRRWBBGGG  [score=11]
  L  : OBOGWWGWWRRGRRGRRWYOGYGGYGGBYYBYYRYRBOOBOOYOOWRWWBWBBB  [score=11]
  L' : BBOBWWRWWRRGRRGRRWBOGWGGWGGOYYGYYGYROOYOOBOOBWRYWBYBBY  [score=11]
  L2 : YBOYWWYWWRRGRRGRRWBOGBGGRGGBYYWYYWYROOOOOOBBYWRGWBGBBO  [score=11]
  B  : GGWWWWWWWRRRRRYRRYOOGGGGGGGYYYYYYYOOOBBBOOBOOBWWBBRBBR  [score=11]
  U  : OWWBWWBWWOOGRRGRRWYBBGGGGGGYYYYYYYYRWRROOOOOORRGWBBBBB  [score=9]
  R  : BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB  [score=9]
  R' : BBGWWGWWGRRRRRRWGGOOYGGYGGRYYBYYWYYWYBBOOOOOOWRRWBBOBB  [score=9]
  R2 : BBYWWYWWRWRRGRRGRROOBGGWGGWYYOYYWYYWYBBOOOOOOGRRGBBGBB  [score=9]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 4 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 4
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 15
Previous move: U'

Current state:
WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWBWWWWWYRGWRRRWRRRRBGGBGGOYYGYYGYYGOOGOOOOOORBBYBBYBB  [score=15]
  R' : WWGWWGWWGRRWRRRWGRRRYGGYGGRYYBYYWYYYOOGOOOOOOOBBBBBBBB  [score=15]
  R2 : WWYWWYWWRWRRGRRRRWRRBGGWGGYYYBYYBYYOOOGOOOOOOGBBGBBGBB  [score=15]
  F  : WWBWWBOOGWRRWRGORWGGRGGRGGGRRWYYYYYROOYOOYOOYYBBWBBBBB  [score=15]
  F' : WWBWWBWRRYRRYRGYRWGGGRGGRGGGOOYYYYYROOOOOWOOWYBBWBBBBB  [score=15]
  F2 : WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB  [score=15]
  D  : WWBWWBWWOWRRRRGBBBRRGGGGRRWYYRYYYYYYOOGOOOGGGYBBWBBOOO  [score=15]
  D' : WWBWWBWWOWRRRRGGGGRRGGGGOOOYYYYYYRYYOOGOOOBBBYBBWBBRRW  [score=15]
  D2 : WWBWWBWWOWRRRRGOOORRGGGGBBBRYYYYYYYYOOGOOORRWYBBWBBGGG  [score=15]
  L  : RWBGWBGWOWRRRRGRRWYRGYGGYGGBYYBYYBYRGOOOOOOOOYBWWBWBBW  [score=13]
  L' : BWBBWBBWOWRRRRGRRWWRGWGGWGGRYYGYYGYROOOOOOOOGYBYWBYBBY  [score=13]
  L2 : YWBYWBYWOWRRRRGRRWBRGBGGBGGWYYWYYWYROOOOOOGOOYBGWBGBBR  [score=13]
  B' : OOOWWBWWOWRWRRWRRBRRGGGGGGGYYYYYYWGRYOGYOOROOBBBBBBYWB  [score=13]
  B2 : RYYWWBWWOWRORRORRORRGGGGGGGYYYYYYBWWWOGGOOROOBBBBBWBBY  [score=13]
  B  : RGWWWBWWOWRRRRYRRYRRGGGGGGGYYYYYYOOOBOGWOOWOOBWYBBBBBB  [score=11]
  U' : WWWWWWOBBYBBRRGRRWWRRGGGGGGYYYYYYYYRRRGOOOOOOOOGWBBBBB  [score=9]
  U2 : OWWBWWBWWOOGRRGRRWYBBGGGGGGYYYYYYYYRWRROOOOOORRGWBBBBB  [score=9]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 5 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 5
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U'

Current state:
WWWWWWOBBYBBRRGRRWWRRGGGGGGYYYYYYYYRRRGOOOOOOOOGWBBBBB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB  [score=11]
  F  : WWWWWWOOGOBBBRGBRWGGWGGRGGRRRYYYYYYRRRYOOYOOYOOGWBBBBB  [score=11]
  F' : WWWWWWYRRYBBYRGYRWRGGRGGWGGGOOYYYYYRRRBOOBOOOOOGWBBBBB  [score=11]
  F2 : WWWWWWYYYOBBORGGRWGGGGGGRRWBBOYYYYYRRRROOROOYOOGWBBBBB  [score=11]
  U' : OWWBWWBWWOOGRRGRRWYBBGGGGGGYYYYYYYYRWRROOOOOORRGWBBBBB  [score=9]
  R  : WWBWWWOBOBGWBRRYRRWRWGGWGGBYYRYYGYYGRRGOOOOOOROGYBBYBB  [score=9]
  R' : WWRWWGOBGRRYRRBWGBWRYGGYGGRYYBYYWYYORRGOOOOOOBOGWBBWBB  [score=9]
  R2 : WWYWWYOBRWRRGRRBBYWRBGGWGGOYYWYYWYYBRRGOOOOOOGOGGBBRBB  [score=9]
  D  : WWWWWWOBBYBBRRGBBBWRRGGGRRWYYRYYYYYYRRGOOOGGGOOGWBBOOO  [score=9]
  D' : WWWWWWOBBYBBRRGGGGWRRGGGOOOYYYYYYRYYRRGOOOBBBOOGWBBRRW  [score=9]
  D2 : WWWWWWOBBYBBRRGOOOWRRGGGBBBRYYYYYYYYRRGOOORRWOOGWBBGGG  [score=9]
  L  : WWWGWWGBBYBBRRGRRWYRRYGGYGGBYYBYYGYRGOOROOROOOOOWBWBBW  [score=9]
  L' : BWWBWWGBBYBBRRGRRWWRRWGGOGGWYYGYYGYROOROOROOGOOYWBYBBY  [score=9]
  L2 : YWWYWWYBBYBBRRGRRWBRRBGGGGGWYYWYYOYROOOOOOGRROOGWBGBBW  [score=9]
  B' : OORWWWOBBYBWRRWRRWWRRGGGGGGYYYYYYWGBYRGYOOROOGBBOBBOWB  [score=9]
  B2 : RYYWWWOBBYBORRORRRWRRGGGGGGYYYYYYWWWWRGGOOBOOBBBBBWGOO  [score=9]
  B  : BGWWWWOBBYBRRRYRRYWRRGGGGGGYYYYYYROOWRGWOOWOOBWOBBOBBG  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 6 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 6
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: B

Current state:
BGWWWWOBBYBRRRYRRYWRRGGGGGGYYYYYYROOWRGWOOWOOBWOBBOBBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWBGWBBWOWRRRRYRRYWRGGGGGGGYYYYYYROOBWOWOOWOOYBRBBOBBG  [score=11]
  U2 : BBOWWWWGBWRGRRYRRYBWOGGGGGGYYYYYYROOYBRWOOWOOWRRBBOBBG  [score=9]
  F  : BGWWWWOOGOBRBRYBRYGGWGGRGGRRRYYYYROOWRYWOYWOYBWOBBOBBG  [score=9]
  F' : BGWWWWYRRYBRYRYYRYRGGRGGWGGGOOYYYROOWRBWOBWOOBWOBBOBBG  [score=9]
  F2 : BGWWWWYYYOBRORYGRYGGGGGGRRWBBOYYYROOWRRWORWOYBWOBBOBBG  [score=9]
  B  : RYYWWWOBBYBORRORRRWRRGGGGGGYYYYYYWWWWRGGOOBOOBBBBBWGOO  [score=9]
  B2 : OORWWWOBBYBWRRWRRWWRRGGGGGGYYYYYYWGBYRGYOOROOGBBOBBOWB  [score=9]
  U' : OWBBWGBWWBWORRYRRYYBRGGGGGGYYYYYYROOWRRWOOWOOWRGBBOBBG  [score=7]
  R' : BGRWWGOBGRRYRRBYYRWRYGGYGGOYYBYYBROBWRGWOOWOOBWOWBOWBG  [score=7]
  R2 : BGYWWYOBOYRRYRRRBYWRBGGBGGBYYWYYWROBWRGWOOWOOGWOGBORBG  [score=7]
  D  : BGWWWWOBBYBRRRYBBGWRRGGGRRYYYOYYOYYRWRGWOOGGGBWOBBOWOO  [score=7]
  D' : BGWWWWOBBYBRRRYGGGWRRGGGWOORYYOYYOYYWRGWOOBBGBWOBBORRY  [score=7]
  D2 : BGWWWWOBBYBRRRYWOOWRRGGGBBGOORYYYYYYWRGWOORRYBWOBBOGGG  [score=7]
  L  : WGWGWWGBBYBRRRYRRYYRRYGGRGGGYYOYYOOOGOOROOWWWBWOBBWBBB  [score=7]
  L2 : YGWYWWRBBYBRRRYRRYGRROGGOGGBYYWYYOOOOOWOOWGRWBWGBBGBBW  [score=7]
  R  : BGBWWBOBBRYYBRRYRRWRWGGWGGBYYRYYGROGWRGWOOWOOOWOYBOYBG  [score=5]
  L' : GGWOWWOBBYBRRRYRRYBRRWGGOGGWYYGYYGOOWWWOOROOGBWRBBYBBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 7 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 7
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 11
Previous move: U

Current state:
WWBGWBBWOWRRRRYRRYWRGGGGGGGYYYYYYROOBWOWOOWOOYBRBBOBBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : WWBGWBGWOWRRRRYRRYYRGYGGRGGGYYOYYROOOOOWOOBWWYBBBBGBBW  [score=13]
  L2 : YWBYWBRWOWRRRRYRRYGRGOGGRGGWYYGYYBOOOOWOOWOWBYBGBBGBBW  [score=13]
  R' : WWGGWGBWGRRWRRRYYRWRYGGYGGOYYBYYBROYBWOWOOWOOOBRBBOBBG  [score=11]
  R2 : WWYGWYBWOYRRYRRRRWWRBGGBGGYYYBYYBROOBWOWOOWOOGBRGBOGBG  [score=11]
  F  : WWBGWBOOOBRRWRYORYGGWGGRGGGRRWYYYROOBWYWOYWOYYBRBBOBBG  [score=11]
  F' : WWBGWBWRRYRRYRYYRYGGGRGGWGGOOOYYYROOBWOWOWWOBYBRBBOBBG  [score=11]
  F2 : WWBGWBYYYORRORYORYGGGGGGGRWOWBYYYROOBWRWORWOWYBRBBOBBG  [score=11]
  D  : WWBGWBBWOWRRRRYBBGWRGGGGRRYYYOYYOYYRBWOWOOGGGYBRBBOWOO  [score=11]
  D' : WWBGWBBWOWRRRRYGGGWRGGGGWOORYYOYYOYYBWOWOOBBGYBRBBORRY  [score=11]
  D2 : WWBGWBBWOWRRRRYWOOWRGGGGBBGOORYYYYYYBWOWOORRYYBRBBOGGG  [score=11]
  L' : GWBOWBRWOWRRRRYRRYWRGGGGBGGWYYGYYGOOWWBOOWOOOYBRBBYBBY  [score=11]
  U  : BBOWWWWGBWRGRRYRRYBWOGGGGGGYYYYYYROOYBRWOOWOOWRRBBOBBG  [score=9]
  R  : WWBGWBBWYRYYRRRWRRWRBGGBGGOYYGYYGROGBWOWOOWOOOBRYBOYBG  [score=9]
  B  : RYYGWBBWOWRORRORRRWRGGGGGGGYYYYYYBWWBWOWOOWOOBBYBBBGOR  [score=9]
  B' : WWBGWBBWOWRWRRWRRBWRGGGGGGGYYYYYYYYRRWOOOOOOOROGBBBYBB  [score=9]
  B2 : OORGWBBWOWRWRRWRRBWRGGGGGGGYYYYYYBWWYWOYOOROOGBBOBBRBY  [score=9]
  U2 : OWBBWGBWWBWORRYRRYYBRGGGGGGYYYYYYROOWRRWOOWOOWRGBBOBBG  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 8 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 8
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U

Current state:
BBOWWWWGBWRGRRYRRYBWOGGGGGGYYYYYYROOYBRWOOWOOWRRBBOBBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F  : BBOWWWOORWRGGRYBRYGGBGGWGGORRWYYYROOYBYWOYWOYWRRBBOBBG  [score=11]
  F' : BBOWWWWRRYRGYRYYRYOGGWGGBGGROOYYYROOYBBWOGWOWWRRBBOBBG  [score=11]
  F2 : BBOWWWYYYORGORYRRYGGGGGGOWBBGWYYYROOYBRWORWOWWRRBBOBBG  [score=11]
  B  : GYYWWWWGBWRORRORRRBWOGGGGGGYYYYYYYWWOBRBOOBOOBBWBBRGOR  [score=11]
  B' : WWYWWWWGBWRBRRBRROBWOGGGGGGYYYYYYYYGRBROOOOOOROGRBBWBB  [score=11]
  B2 : OORWWWWGBWRWRRWRRYBWOGGGGGGYYYYYYOBBYBRYOOGOOGBBOBBRRW  [score=11]
  D  : BBOWWWWGBWRGRRYBBGBWOGGGRRYYYOYYOYYRYBRWOOGGGWRRBBOWOO  [score=9]
  D' : BBOWWWWGBWRGRRYGGGBWOGGGWOORYYOYYOYYYBRWOOBBGWRRBBORRY  [score=9]
  D2 : BBOWWWWGBWRGRRYWOOBWOGGGBBGOORYYYYYYYBRWOORRYWRRBBOGGG  [score=9]
  L  : BBOGWWGGBWRGRRYRRYYWOYGGRGGGYYOYYROOROOBOOYWWWRWBBWBBB  [score=9]
  L2 : YBOYWWRGBWRGRRYRRYGWOOGGRGGBYYWYYWOOOOWOOWRBYWRGBBGBBB  [score=9]
  U  : OWBBWGBWWBWORRYRRYYBRGGGGGGYYYYYYROOWRRWOOWOOWRGBBOBBG  [score=7]
  U2 : BGWWWWOBBYBRRRYRRYWRRGGGGGGYYYYYYROOWRGWOOWOOBWOBBOBBG  [score=7]
  R' : BBOWWGWGGRRWRRRYYGBWYGGYGGOYYBYYBROWYBRWOOWOOBRRWBOOBG  [score=7]
  R2 : BBYWWYWGOYRRYRRGRWBWBGGBGGWYYOYYWROBYBRWOOWOOGRRGBOOBG  [score=7]
  L' : GBOOWWRGBWRGRRYRRYBWOWGGWGGBYYGYYGOOWWYOOBOORWRRBBYBBY  [score=7]
  R  : BBBWWBWGWGYYRRRWRRBWOGGWGGBYYOYYGROGYBRWOOWOOORRYBOYBG  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 9 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 9
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: R

Current state:
BBBWWBWGWGYYRRRWRRBWOGGWGGBYYOYYGROGYBRWOOWOOORRYBOYBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U' : WWBGWBWBBORRRRRWRRGYYGGWGGBYYOYYGROGBWOWOOWOOYBRYBOYBG  [score=9]
  R  : BBYWWYWGOYRRYRRGRWBWBGGBGGWYYOYYWROBYBRWOOWOOGRRGBOOBG  [score=7]
  R2 : BBOWWGWGGRRWRRRYYGBWYGGYGGOYYBYYBROWYBRWOOWOOBRRWBOOBG  [score=7]
  F  : BBBWWBOORWYYGRRWRRGGBGGWBWOWRGYYGROGYBYWOYWOOORRYBOYBG  [score=7]
  F2 : BBBWWBOYYOYYORRRRRBGGWGGOWBWGWYYGROGYBWWORWOGORRYBOYBG  [score=7]
  B' : WWYWWBWGWGYBRRBWRBBWOGGWGGBYYOYYGRRYRBROOOGOOROGRBBOYY  [score=7]
  B2 : GORWWBWGWGYWRRWWRYBWOGGWGGBYYOYYGBBBRBRROOYOOGBYOBYRRO  [score=7]
  U  : BBWBWGBWWBWORRRWRRYBRGGWGGBYYOYYGROGORRWOOWOOGYYYBOYBG  [score=5]
  U2 : WGWBWWBBBYBRRRRWRRORRGGWGGBYYOYYGROGGYYWOOWOOBWOYBOYBG  [score=5]
  F' : BBBWWBGRWOYYYRRYRROWBWGGBGGROOYYGROGYBWWOGWOWORRYBOYBG  [score=5]
  D  : BBBWWBWGWGYYRRRYBGBWOGGWWRROGGYYOYYRYBRWOOGGBORRYBOWOO  [score=5]
  D' : BBBWWBWGWGYYRRRGGBBWOGGWWOORYYOYYGGOYBRWOOYBGORRYBOWRR  [score=5]
  D2 : BBBWWBWGWGYYRRRWOOBWOGGWYBGGORGYYOYYYBRWOOWRRORRYBOGGB  [score=5]
  L  : BBBGWBGGWGYYRRRWRRYWOYGWRGBGYOOYGROGROOBOOYWWORWYBWYBB  [score=5]
  L2 : YBBYWBRGWGYYRRRWRRGWOOGWRGBBYOWYGWOGOOWOOWRBYORGYBGYBB  [score=5]
  B  : YRRWWBWGWGYGRROWRRBWOGGWGGBYYOYYGYWWBBRBOOBOOYYOBBRGOR  [score=5]
  L' : GBBOWBRGWGYYRRRWRRBWOWGWWGBBYOGYGGOGWWYOOBOORORRYBYYBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 10 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 10
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U'

Current state:
WWBGWBWBBORRRRRWRRGYYGGWGGBYYOYYGROGBWOWOOWOOYBRYBOYBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : WWYGWWWBBWRORRRRRRGYOGGGGGGYYYYYYROYBWOWOOWOOBBRBBOBBG  [score=11]
  F  : WWBGWBOOOWRRBRRBRRGGGGGYBWYWROYYGROGBWYWOYWOOYBRYBOYBG  [score=11]
  F2 : WWBGWBOYYORRORRORRBGGWGGYYGBBWYYGROGBWWWORWOOYBRYBOYBG  [score=11]
  L  : GWBGWBGBBORRRRRWRRYYYYGWRGBGYOOYGROGOOOWOOBWWYBWYBGYBW  [score=11]
  L2 : YWBYWBRBBORRRRRWRRGYYOGWRGBWYOGYGWOGOOWOOWOWBYBGYBGYBG  [score=11]
  R  : WWYGWYWBYRRRRRRORWGYBGGBGGBYYYYYWROBBWOWOOWOOGBRGBOOBG  [score=9]
  R2 : WWOGWGWBGRRWRRRRROGYYGGYGGYYYBYYBROBBWOWOOWOOBBRWBOYBG  [score=9]
  F' : WWBGWBORWORRYRRYRRYWBYGGGGGOOOYYGROGBWBWOBWOWYBRYBOYBG  [score=9]
  D  : WWBGWBWBBORRRRRYBGGYYGGWWRROGGYYOYYRBWOWOOGGBYBRYBOWOO  [score=9]
  D' : WWBGWBWBBORRRRRGGBGYYGGWWOORYYOYYGGOBWOWOOYBGYBRYBOWRR  [score=9]
  D2 : WWBGWBWBBORRRRRWOOGYYGGWYBGGORGYYOYYBWOWOOWRRYBRYBOGGB  [score=9]
  L' : GWBOWBRBBORRRRRWRRWYYGGWWGBGYOGYGGOGWWBOOWOOOYBRYBYYBY  [score=9]
  B' : WWBGWBWBBORWRRWWRBGYYGGWGGBYYOYYGRRRRWOOOOGOOROGBBBYYY  [score=7]
  B2 : GORGWBWBBORWRRWWRBGYYGGWGGBYYOYYGBWWRWOROOROOGBYOBYRBY  [score=7]
  U' : WGWBWWBBBYBRRRRWRRORRGGWGGBYYOYYGROGGYYWOOWOOBWOYBOYBG  [score=5]
  U2 : BBWBWGBWWBWORRRWRRYBRGGWGGBYYOYYGROGORRWOOWOOGYYYBOYBG  [score=5]
  B  : RRRGWBWBBORGRROWRRGYYGGWGGBYYOYYGBWWBWOWOOWOOYYYBBBGOR  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 11 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 11
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U'

Current state:
WGWBWWBBBYBRRRRWRRORRGGWGGBYYOYYGROGGYYWOOWOOBWOYBOYBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : WGRBWWBBBWRYRRBRRROROGGGGGGYYYYYYROBGYYWOOWOOBWOWBOWBG  [score=7]
  F  : WGWBWWOOYBBRBRRBRRGGOGGRBWRWRYYYGROGGYYWOYWOOBWOYBOYBG  [score=7]
  F2 : WGWBWWOYYOBRORRYRRBGGWGGRROBBBYYGROGGYWWORWOYBWOYBOYBG  [score=7]
  L  : OGWGWWGBBYBRRRRWRRYRRYGWRGBGYOOYGOOGYOOYOOGWWBWBYBBYBW  [score=7]
  L2 : YGWYWWRBBYBRRRRWRRGRROGWOGBWYOBYGBOGOOWOOWYYGBWGYBGYBO  [score=7]
  B' : WWGBWWBBBYBWRRGWRWORRGGWGGBYYOYYGRRRRYYOOOGOOOOGWBBBYY  [score=7]
  B2 : GORBWWBBBYBWRRWWRGORRGGWGGBYYOYYGWGWRYYROOROOGBYOBYOWB  [score=7]
  U' : BBWBWGBWWBWORRRWRRYBRGGWGGBYYOYYGROGORRWOOWOOGYYYBOYBG  [score=5]
  U2 : BBBWWBWGWGYYRRRWRRBWOGGWGGBYYOYYGROGYBRWOOWOOORRYBOYBG  [score=5]
  R  : WGYBWYBBBRRRBRRYRWORWGGWGGBYYRYYWROBGYYWOOWOOGWOGBOOBG  [score=5]
  R2 : WGOBWGBBGRRWRRRRBYORYGGYGGBYYWYYWROBGYYWOOWOOBWOWBORBG  [score=5]
  F' : WGWBWWYRWOBRYRRYRRRWBRGGOGGYOOYYGROGGYBWOBWOBBWOYBOYBG  [score=5]
  D  : WGWBWWBBBYBRRRRYBGORRGGWWRROGGYYOYYRGYYWOOGGBBWOYBOWOO  [score=5]
  D' : WGWBWWBBBYBRRRRGGBORRGGWWOORYYOYYGGOGYYWOOYBGBWOYBOWRR  [score=5]
  D2 : WGWBWWBBBYBRRRRWOOORRGGWYBGGORGYYOYYGYYWOOWRRBWOYBOGGB  [score=5]
  L' : GGWOWWOBBYBRRRRWRRWRRBGWBGBOYOGYGGOGWWGOOYOOYBWRYBYYBY  [score=5]
  B  : RRRBWWBBBYBGRROWRRORRGGWGGBYYOYYGGWWWYYGOOWOOYYBBBWGOO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 12 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 12
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: R'

Current state:
WGRBWWBBBWRYRRBRRROROGGGGGGYYYYYYROBGYYWOOWOOBWOWBOWBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F  : WGRBWWOOYBRYBRBBRRGGOGGRGGORRWYYYROBGYYWOYWOYBWOWBOWBG  [score=9]
  F' : WGRBWWWRRYRYYRBYRROGGRGGOGGYOOYYYROBGYBWOBWOBBWOWBOWBG  [score=9]
  F2 : WGRBWWYYYORYORBYRRGGGGGGOROBBBYYYROBGYRWORWOWBWOWBOWBG  [score=9]
  L  : OGRGWWGBBWRYRRBRRRYROYGGRGGGYYOYYOOBYOOYOOGWWBWBWBBWBW  [score=9]
  L2 : YGRYWWRBBWRYRRBRRRGROOGGOGGWYYBYYBOBOOWOOWYYGBWGWBGWBO  [score=9]
  B' : WWGBWWBBBWRWRRGRRROROGGGGGGYYYYYYRBYRYYOOOBOOOOGWBBBWW  [score=9]
  B2 : BORBWWBBBWRWRRWRRGOROGGGGGGYYYYYYRGWRYYBOOYOOGBWOBWOWB  [score=9]
  U  : RWBGWBWBBORORRBRRRGYYGGGGGGYYYYYYROBBWOWOOWOOWRYWBOWBG  [score=7]
  D  : WGRBWWBBBWRYRRBWBGOROGGGRRRYYBYYOYYRGYYWOOGGGBWOWBOWOO  [score=7]
  D' : WGRBWWBBBWRYRRBGGGOROGGGWOORYYOYYBYYGYYWOOWBGBWOWBORRR  [score=7]
  D2 : WGRBWWBBBWRYRRBWOOOROGGGWBGBORYYYYYYGYYWOORRRBWOWBOGGG  [score=7]
  L' : GGROWWOBBWRYRRBRRRWROBGGBGGOYYGYYGOBWWGOOYOOYBWRWBYWBY  [score=7]
  B  : YBRBWWBBBWRBRRORRROROGGGGGGYYYYYYGWWRYYGOOWOOWWBBBWGOO  [score=7]
  U' : BBWBWGBWRBWORRBRRRWRYGGGGGGYYYYYYROBOROWOOWOOGYYWBOWBG  [score=5]
  U2 : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  R' : WGOBWGBBGRRWRRRRBYORYGGYGGBYYWYYWROBGYYWOOWOOBWOWBORBG  [score=5]
  R2 : WGYBWYBBBRRRBRRYRWORWGGWGGBYYRYYWROBGYYWOOWOOGWOGBOOBG  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 13 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 13
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
RWBGWBWBBORORRBRRRGYYGGGGGGYYYYYYROBBWOWOOWOOWRYWBOWBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F  : RWBGWBOOOWROBRBBRRGGGGGYGGYRROYYYROBBWYWOYWOYWRYWBOWBG  [score=9]
  F' : RWBGWBORRYROYRBYRRYGGYGGGGGOOOYYYROBBWBWOBWOWWRYWBOWBG  [score=9]
  F2 : RWBGWBYYYOROORBORRGGGGGGYYGBBWYYYROBBWRWORWOOWRYWBOWBG  [score=9]
  L  : GWBGWBGBBORORRBRRRYYYYGGRGGGYYOYYYOBOOOWOOBWWWRWWBGWBR  [score=9]
  L2 : YWBYWBRBBORORRBRRRGYYOGGYGGRYYGYYWOBOOWOOWOWBWRGWBGWBG  [score=9]
  R  : RWWGWWWBWOBRRRRORRGYBGGBGGBYYYYYGROGBWOWOOWOOBRYYBOYBG  [score=7]
  R' : RWYGWGWBGRRORRRRBOGYYGGYGGBYYWYYWROWBWOWOOWOOBRYBBOBBG  [score=7]
  R2 : RWYGWYWBBRRRBRROROGYWGGWGGWYYBYYBROBBWOWOOWOOGRYGBOYBG  [score=7]
  D  : RWBGWBWBBORORRBWBGGYYGGGRRRYYBYYOYYRBWOWOOGGGWRYWBOWOO  [score=7]
  D' : RWBGWBWBBORORRBGGGGYYGGGWOORYYOYYBYYBWOWOOWBGWRYWBORRR  [score=7]
  D2 : RWBGWBWBBORORRBWOOGYYGGGWBGBORYYYYYYBWOWOORRRWRYWBOGGG  [score=7]
  L' : GWBOWBYBBORORRBRRRRYYGGGWGGGYYGYYGOBWWBOOWOOOWRRWBYWBY  [score=7]
  B' : WWBGWBWBBORRRRWRRBGYYGGGGGGYYYYYYRBORWOOOOBOOYOGRBBWWW  [score=7]
  B2 : BORGWBWBBORWRRWRRBGYYGGGGGGYYYYYYBWRRWOBOOOOOGBWOBWYRW  [score=7]
  U  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  U2 : BBWBWGBWRBWORRBRRRWRYGGGGGGYYYYYYROBOROWOOWOOGYYWBOWBG  [score=5]
  B  : OBRGWBWBBORBRRORRRGYYGGGGGGYYYYYYBWWBWOWOOROOWWWBBRGOY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 14 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 14
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : WGRBWWBBBWRYRRBRRROROGGGGGGYYYYYYROBGYYWOOWOOBWOWBOWBG  [score=7]
  R  : BBWWWWRGOYBRYRRGRRBWBGGBGGWYYOYYGROGWRYWOOWOOBROYBOYBG  [score=7]
  R' : BBOWWGRGGRRGRRYRBYBWYGGYGGBYYWYYWROOWRYWOOWOOWROBBOBBG  [score=7]
  R2 : BBYWWYRGBRRRBRRYYGBWWGGWGGOYYBYYBROWWRYWOOWOOGROGBOOBG  [score=7]
  F  : BBBWWBOOYRYYGRBWRRGGBGGWGGORRGYYYROBWRYWOYWOYOROWBOWBG  [score=7]
  F' : BBBWWBGRRYYYYRBYRROGGWGGBGGYOOYYYROBWRWWOGWOROROWBOWBG  [score=7]
  F2 : BBBWWBYYYOYYORBYRRGGGGGGOWBWGRYYYROBWRRWORWOGOROWBOWBG  [score=7]
  B' : WWWWWBRGWGYBRRBRRBBWOGGGGGGYYYYYYRBYRRYOOOBOOOOGRBBOWW  [score=7]
  B2 : BORWWBRGWGYWRRWRRWBWOGGGGGGYYYYYYBBBRRYBOOYOOGBWOBWORO  [score=7]
  U  : BBWBWGBWRBWORRBRRRWRYGGGGGGYYYYYYROBOROWOOWOOGYYWBOWBG  [score=5]
  D  : BBBWWBRGWGYYRRBWBGBWOGGGRRRYYBYYOYYRWRYWOOGGGOROWBOWOO  [score=5]
  D' : BBBWWBRGWGYYRRBGGGBWOGGGWOORYYOYYBYYWRYWOOWBGOROWBORRR  [score=5]
  D2 : BBBWWBRGWGYYRRBWOOBWOGGGWBGBORYYYYYYWRYWOORRROROWBOGGG  [score=5]
  L  : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  L2 : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  B  : YBRWWBRGWGYBRRORRRBWOGGGGGGYYYYYYWWWBRYBOOBOOWWOBBRGOO  [score=5]
  L' : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 15 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 15
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: L'

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U' : OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY  [score=5]
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 16 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 16
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U'

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  U2 : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 17 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 17
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U'

Current state:
WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WGWBWWBBBWBRWRRWRROROWGORGGBYRGYGGOGGYYOOROOYBWOYBYYBY  [score=5]
  R' : WGRBWGBBGRRWRRWRBWORYWGYRGBBYWGYWGOBGYYOOROOYGWOOBYOBY  [score=5]
  R2 : WGYBWYBBBRRRBRRWWWORWWGWRGBBYOGYOGOGGYYOOROOYGWOGBYRBY  [score=5]
  F' : WGOBWOWRRYWWYRBBRRRGGRGGOWRYRYGYYGOBGYGOOBOOBBWOWBYWBY  [score=5]
  F2 : WGOBWOYYBYWWRRBYRRGGRGGWRROGBBGYYGOBGYROOROOWBWOWBYWBY  [score=5]
  L  : OGOWWORBGWWWRRBRRRBRRGGGGGGYYYYYYOOBYRYYOOGOOBWBWBBWBW  [score=5]
  L' : YGOYWOOBGWWWRRBRRRWRRBGGBGGOYYWYYROBOOGOOYYRYBWGWBGWBB  [score=5]
  L2 : BGOGWOGBGWWWRRBRRRYRRYGGOGGWYYBYYBOBYOOROOYYGBWRWBWWBO  [score=5]
  B2 : BOGBWOBBGWWORRORRGORRWGGRGGBYYGYYOGWRYYBORWOYYBWYBWOWB  [score=5]
  U' : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  F  : WGOBWOYRYBWWBRBGRRRWOGGRGGRRRWGYYGOBGYBOOYOOYBWOWBYWBY  [score=3]
  D  : WGOBWOBBGWWWRRBWBYORRWGGRRRYYBYYOBGGGYYOORRGGBWOWBYOOY  [score=3]
  D' : WGOBWOBBGWWWRRBRGGORRWGGOOYGGBOYYBYYGYYOORWBYBWOWBYRRR  [score=3]
  D2 : WGOBWOBBGWWWRRBOOYORRWGGWBYBOGYYGYYBGYYOORRRRBWOWBYRGG  [score=3]
  B  : WBRBWOBBGWWBRRORRGORRWGGRGGBYYGYYGOOOYYGORWOYWWBBBWYYO  [score=3]
  B' : OOGBWOBBGWWWRRGRROORRWGGRGGBYYGYYRBWGYYOORBOYOYYWBBBWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 18 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 18
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U'

Current state:
BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY  [score=5]
  R  : BBWBWWGOGOBRWRRBRRWWWWGGRGOBYWGYGGOGORROOROOYBYYYBYYBY  [score=5]
  R' : BBWBWGGOGRRBRRWRBOWWYWGYRGBBYWGYWGOGORROOROOYOYYGBYWBY  [score=5]
  R2 : BBYBWYGOBRRRBRROWBWWWWGWRGGBYWGYGGOOORROOROOYGYYGBYWBY  [score=5]
  F' : BBWBWGBRRYWOYRBBRRWGGWGGWWRRRYGYYGOBOROOOOOOGGYYWBYWBY  [score=5]
  F2 : BBWBWGYYBYWORRBRRRGGRGGWWWWOOGGYYGOBORROOROOBGYYWBYWBY  [score=5]
  L  : WBWWWGROOBWORRBRRRBWWGGGGGGYYYYYYYOBRRYROOOOOGYGWBBWBB  [score=5]
  L' : YBWYWGYOOBWORRBRRRBWWBGGGGGWYYWYYROBOOOOORYRRGYGWBGWBB  [score=5]
  L2 : BBWGWGGOOBWORRBRRRYWWYGGYGGBYYBYYGOBYOOROORROGYRWBWWBW  [score=5]
  B2 : BOGBWGGOOBWORRORROWWWWGGRGGBYYGYYWBBRRRBOROOYYBWYBWYYG  [score=5]
  U' : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  F  : BBWBWGYRRGWOORBORRRWWGGWGGWRRBGYYGOBORBOOYOOYGYYWBYWBY  [score=3]
  D  : BBWBWGGOOBWORRBWBYWWWWGGRRRYYBYYOBGGORROORRGGGYYWBYOOY  [score=3]
  D' : BBWBWGGOOBWORRBRGGWWWWGGOOYGGBOYYBYYORROORWBYGYYWBYRRR  [score=3]
  D2 : BBWBWGGOOBWORRBOOYWWWWGGWBYBOGYYGYYBORROORRRRGYYWBYRGG  [score=3]
  B  : OBRBWGGOOBWBRRORRGWWWWGGRGGBYYGYYOOOWRRBORBOYWWGBBYYYY  [score=3]
  B' : OOOBWGGOOBWBRRBRRWWWWWGGRGGBYYGYYRBOGRROORBOYYYYYBBGWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 19 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 19
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 20 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 20
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 21 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 21
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY  [score=5]
  R  : BBWBWWGOGOBRWRRBRRWWWWGGRGOBYWGYGGOGORROOROOYBYYYBYYBY  [score=5]
  R' : BBWBWGGOGRRBRRWRBOWWYWGYRGBBYWGYWGOGORROOROOYOYYGBYWBY  [score=5]
  R2 : BBYBWYGOBRRRBRROWBWWWWGWRGGBYWGYGGOOORROOROOYGYYGBYWBY  [score=5]
  F' : BBWBWGBRRYWOYRBBRRWGGWGGWWRRRYGYYGOBOROOOOOOGGYYWBYWBY  [score=5]
  F2 : BBWBWGYYBYWORRBRRRGGRGGWWWWOOGGYYGOBORROOROOBGYYWBYWBY  [score=5]
  L  : WBWWWGROOBWORRBRRRBWWGGGGGGYYYYYYYOBRRYROOOOOGYGWBBWBB  [score=5]
  L' : YBWYWGYOOBWORRBRRRBWWBGGGGGWYYWYYROBOOOOORYRRGYGWBGWBB  [score=5]
  L2 : BBWGWGGOOBWORRBRRRYWWYGGYGGBYYBYYGOBYOOROORROGYRWBWWBW  [score=5]
  B2 : BOGBWGGOOBWORRORROWWWWGGRGGBYYGYYWBBRRRBOROOYYBWYBWYYG  [score=5]
  U  : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : BBWBWGYRRGWOORBORRRWWGGWGGWRRBGYYGOBORBOOYOOYGYYWBYWBY  [score=3]
  D  : BBWBWGGOOBWORRBWBYWWWWGGRRRYYBYYOBGGORROORRGGGYYWBYOOY  [score=3]
  D' : BBWBWGGOOBWORRBRGGWWWWGGOOYGGBOYYBYYORROORWBYGYYWBYRRR  [score=3]
  D2 : BBWBWGGOOBWORRBOOYWWWWGGWBYBOGYYGYYBORROORRRRGYYWBYRGG  [score=3]
  B  : OBRBWGGOOBWBRRORRGWWWWGGRGGBYYGYYOOOWRRBORBOYWWGBBYYYY  [score=3]
  B' : OOOBWGGOOBWBRRBRRWWWWWGGRGGBYYGYYRBOGRROORBOYYYYYBBGWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 22 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 22
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 23 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 23
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 24 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 24
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY  [score=5]
  R  : BBWBWWGOGOBRWRRBRRWWWWGGRGOBYWGYGGOGORROOROOYBYYYBYYBY  [score=5]
  R' : BBWBWGGOGRRBRRWRBOWWYWGYRGBBYWGYWGOGORROOROOYOYYGBYWBY  [score=5]
  R2 : BBYBWYGOBRRRBRROWBWWWWGWRGGBYWGYGGOOORROOROOYGYYGBYWBY  [score=5]
  F' : BBWBWGBRRYWOYRBBRRWGGWGGWWRRRYGYYGOBOROOOOOOGGYYWBYWBY  [score=5]
  F2 : BBWBWGYYBYWORRBRRRGGRGGWWWWOOGGYYGOBORROOROOBGYYWBYWBY  [score=5]
  L  : WBWWWGROOBWORRBRRRBWWGGGGGGYYYYYYYOBRRYROOOOOGYGWBBWBB  [score=5]
  L' : YBWYWGYOOBWORRBRRRBWWBGGGGGWYYWYYROBOOOOORYRRGYGWBGWBB  [score=5]
  L2 : BBWGWGGOOBWORRBRRRYWWYGGYGGBYYBYYGOBYOOROORROGYRWBWWBW  [score=5]
  B2 : BOGBWGGOOBWORRORROWWWWGGRGGBYYGYYWBBRRRBOROOYYBWYBWYYG  [score=5]
  U  : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : BBWBWGYRRGWOORBORRRWWGGWGGWRRBGYYGOBORBOOYOOYGYYWBYWBY  [score=3]
  D  : BBWBWGGOOBWORRBWBYWWWWGGRRRYYBYYOBGGORROORRGGGYYWBYOOY  [score=3]
  D' : BBWBWGGOOBWORRBRGGWWWWGGOOYGGBOYYBYYORROORWBYGYYWBYRRR  [score=3]
  D2 : BBWBWGGOOBWORRBOOYWWWWGGWBYBOGYYGYYBORROORRRRGYYWBYRGG  [score=3]
  B  : OBRBWGGOOBWBRRORRGWWWWGGRGGBYYGYYOOOWRRBORBOYWWGBBYYYY  [score=3]
  B' : OOOBWGGOOBWBRRBRRWWWWWGGRGGBYYGYYRBOGRROORBOYYYYYBBGWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Fallback at Step 25, Retry 1

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES:

1.  **IMMEDIATE FAILURE HANDLING (CRITICAL):**
    If the user prompt includes a "FAILURE REPORT" section indicating a cycle, you MUST prioritize avoiding that cycle. You are instructed to select a move that does NOT lead to a cycle and is different from any moves explicitly identified as problematic in the "FAILURE REPORT". Filter out these problematic moves from the lookup table *before* proceeding with phase-specific rules.

2.  **Phase white_cross:**
    - Apply these rules to the remaining (filtered) moves in the lookup table:
        - If there is any U-face move (U, U', U2) that is among the highest-scoring *available* moves AND results in a score *higher* than the `Current score`, pick the first such U-face move.
        - Otherwise, pick the FIRST entry in the filtered lookup table (which is the highest scoring available move).

3.  **Phase full_solve:**
    - Pick the FIRST entry in the filtered lookup table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

      OOG
      GWB
      WBB
BWO GYY ORR WWW
OOR WGG RRB WBY
OOY RGG RRR WBY
      BYY
      GYY
      GOB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

## FAILURE REPORT:
The previous attempt to select a move for this step resulted in a "Cycle detected" error. The system identified that selecting either `U` or `U'` would lead to a state previously visited too many times, causing a loop.

You **MUST** select a move that does NOT lead to a cycle. Specifically, you **MUST NOT** choose `U` or `U'`. Apply the `MOVE SELECTION RULES` from the system prompt, ensuring you filter out `U` and `U'` from the `MOVE LOOKUP TABLE` before making your choice. Your goal is to pick the best available move that avoids the detected cycle.

### Failed Predictions
- Agent cycle_detector: action=N/A, state=OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent cycle_detector: predicted action=N/A, predicted state=OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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
The agents failed because the `MOVE SELECTION RULE` for the `white_cross` phase prioritized U-face moves (`U`, `U'`, `U2`) even when they did not improve the score, or even lowered it, as long as the score was `>= (current score - 2)`. In the provided example, the current score is 5. U-face moves `U` and `U'` both have a score of 3, which is `>= (5 - 2)`. This led the agents to select `U` or `U'`, which did not improve the state and ultimately resulted in a detected cycle, meaning the agent was stuck in a loop. Meanwhile, other moves like `F'` or `L` offered a score of 7, which would have been a significant improvement, but were ignored due to the U-face preference.

The `cycle_detector`'s feedback "You MUST choose a completely different move" is crucial and needs to be integrated into the agent's decision-making process. The original prompt does not provide a mechanism for the agent to react to such feedback. The improved prompts will:
1.  **Prioritize cycle avoidance:** Introduce a critical rule to filter out problematic moves identified in a `FAILURE REPORT`.
2.  **Refine U-face preference:** Adjust the `white_cross` rule to prioritize score improvement first, only preferring U-face moves if they are among the highest-scoring improving moves.
3.  **Explicitly convey failure:** Modify the user prompt to include a `FAILURE REPORT` section that clearly states the problematic moves to avoid.

---

<SYSTEM_PROMPT>
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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES:

1.  **IMMEDIATE FAILURE HANDLING (CRITICAL):**
    If the user prompt includes a "FAILURE REPORT" section indicating a cycle, you MUST prioritize avoiding that cycle. You are instructed to select a move that does NOT lead to a cycle and is different from any moves explicitly identified as problematic in the "FAILURE REPORT". Filter out these problematic moves from the lookup table *before* proceeding with phase-specific rules.

2.  **Phase white_cross:**
    - Apply these rules to the remaining (filtered) moves in the lookup table:
        - If there is any U-face move (U, U', U2) that is among the highest-scoring *available* moves AND results in a score *higher* than the `Current score`, pick the first such U-face move.
        - Otherwise, pick the FIRST entry in the filtered lookup table (which is the highest scoring available move).

3.  **Phase full_solve:**
    - Pick the FIRST entry in the filtered lookup table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: {previous_move}

Current state:
{current_state}

{state_visual}

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

## FAILURE REPORT:
The previous attempt to select a move for this step resulted in a "Cycle detected" error. The system identified that selecting either `U` or `U'` would lead to a state previously visited too many times, causing a loop.

You **MUST** select a move that does NOT lead to a cycle. Specifically, you **MUST NOT** choose `U` or `U'`. Apply the `MOVE SELECTION RULES` from the system prompt, ensuring you filter out `U` and `U'` from the `MOVE LOOKUP TABLE` before making your choice. Your goal is to pick the best available move that avoids the detected cycle.
</USER_PROMPT>

---

## Actual LLM Prompt at Step 25 (fallback)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES:

1.  **IMMEDIATE FAILURE HANDLING (CRITICAL):**
    If the user prompt includes a "FAILURE REPORT" section indicating a cycle, you MUST prioritize avoiding that cycle. You are instructed to select a move that does NOT lead to a cycle and is different from any moves explicitly identified as problematic in the "FAILURE REPORT". Filter out these problematic moves from the lookup table *before* proceeding with phase-specific rules.

2.  **Phase white_cross:**
    - Apply these rules to the remaining (filtered) moves in the lookup table:
        - If there is any U-face move (U, U', U2) that is among the highest-scoring *available* moves AND results in a score *higher* than the `Current score`, pick the first such U-face move.
        - Otherwise, pick the FIRST entry in the filtered lookup table (which is the highest scoring available move).

3.  **Phase full_solve:**
    - Pick the FIRST entry in the filtered lookup table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

      OOG
      GWB
      WBB
BWO GYY ORR WWW
OOR WGG RRB WBY
OOY RGG RRR WBY
      BYY
      GYY
      GOB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

## FAILURE REPORT:
The previous attempt to select a move for this step resulted in a "Cycle detected" error. The system identified that selecting either `U` or `U'` would lead to a state previously visited too many times, causing a loop.

You **MUST** select a move that does NOT lead to a cycle. Specifically, you **MUST NOT** choose `U` or `U'`. Apply the `MOVE SELECTION RULES` from the system prompt, ensuring you filter out `U` and `U'` from the `MOVE LOOKUP TABLE` before making your choice. Your goal is to pick the best available move that avoids the detected cycle.

---

## Fallback at Step 25, Retry 2

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your core function is to act as a **STRICT RULE-FOLLOWER** and **EXACT DATA PARSER**. Your task is to apply specific selection rules to a provided lookup table and **ABSOLUTELY EXACTLY COPY** the results.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

**MOVE SELECTION RULES (CRITICAL - FOLLOW PRECISELY, NO EXCEPTIONS):**

**white_cross phase:**
1.  Check if any U-face move (U, U', U2) exists in the provided lookup table.
2.  From these U-face moves, identify any that have a score **>= (current score - 2)**.
3.  If such U-face moves are found:
    *   **SELECT THE VERY FIRST** of these qualifying U-face moves as it appears in the lookup table.
4.  Otherwise (if no U-face move meets the score condition):
    *   **SELECT THE VERY FIRST** entry in the entire lookup table.

**full_solve phase:**
- SELECT THE VERY FIRST entry in the lookup table (which is always the highest score).

**COPY RULE (ABSOLUTELY STRICT - NO MODIFICATION PERMITTED):**
- You **MUST** copy the `next_state` **ABSOLUTELY EXACTLY** as it appears on the chosen line in the lookup table.
- **DO NOT COMPUTE, MODIFY, OR INFER THE NEXT STATE.** Your role is NOT to simulate the cube or predict the outcome of a move.
- Copy **ONLY** the 54-character string that appears **BETWEEN** ": " and "  [score=" on the chosen line.

**REQUIREMENTS (ABSOLUTELY CRITICAL - ADHERE STRICTLY, NO EXTRA TEXT):**
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown, no comments).
- `next_state` MUST be copied **EXACTLY** from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2

Current state:
```
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY
```

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

--- SELECTION AND COPYING INSTRUCTIONS (FOLLOW THESE STEPS EXACTLY) ---
1.  You are in the '{phase}' phase.
2.  Your current score is {current_score}.
3.  Calculate the required score threshold for U-face moves: {current_score} - 2 = **{score_threshold}**.
4.  Examine the 'MOVE LOOKUP TABLE' carefully.
    *   **First, check for any U-face moves (U, U', U2)** that have a score **>= {score_threshold}**.
    *   If you find one or more such U-face moves, **SELECT THE FIRST ONE** that appears in the table.
    *   If no U-face moves meet this condition, **SELECT THE VERY FIRST ENTRY** in the entire lookup table (regardless of move type).
5.  Once you have identified the chosen move and its corresponding next_state string from the table, **COPY THE 54-CHARACTER next_state STRING ABSOLUTELY EXACTLY**. **DO NOT COMPUTE OR ALTER IT IN ANY WAY.**

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

### Failed Predictions
- Agent 25:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:4: action=None, state=None, error=Invalid move: immediate undo move (loop prevention).
- Agent 25:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:7: action=None, state=None, error=Invalid move: immediate undo move (loop prevention).
- Agent 25:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent 25:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:4: predicted action=None, predicted state=None, error=Invalid move: immediate undo move (loop prevention).
  - Agent 25:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:7: predicted action=None, predicted state=None, error=Invalid move: immediate undo move (loop prevention).
  - Agent 25:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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
The agents failed primarily because they did not adhere strictly to the "COPY RULE" for `next_state` and, in some cases, likely misinterpreted or failed to apply the `MOVE SELECTION RULE` for the `white_cross` phase, leading to invalid move choices.

1.  **Inconsistent Prediction Error:** The most common error ("Inconsistent prediction: next_state does not match current_state + move.") clearly indicates that agents were attempting to *compute* or *simulate* the `next_state` rather than *copying it character-by-character* from the lookup table as explicitly instructed. LLMs often default to reasoning/simulation unless strongly constrained.
2.  **Invalid Move Error:** The "Invalid move: immediate undo move (loop prevention)" suggests a failure in selecting the correct move according to the `white_cross` phase rules. With `current_score: 5`, the threshold `(5 - 2)` is `3`. Both `U` and `U'` (scores `3`) meet the condition. The rule states "If ANY U-face move... pick it". This is slightly ambiguous if multiple match. The agents may have picked a non-U-face move, or a U-face move other than `U` or `U'`, or just generally got confused due to the state calculation attempt. The `previous_move: U2` means `U` is *not* an undo move, so if `U` was chosen correctly, this error shouldn't happen. This further points to the agents not strictly following the rules or attempting their own "validity check" beyond instructions.

**Improvements:**

1.  **Extreme Emphasis on Copying:** The system and user prompts will use stronger, more explicit language, including negative constraints and repetition, to force the LLM to understand its role as a data copier for `next_state`, not a simulator.
2.  **Clarified Selection Logic:** The `white_cross` selection rule will be made completely unambiguous regarding *which* U-face move to pick if multiple satisfy the condition (i.e., the first one found in the table).
3.  **Simplified User Prompt:** The user prompt will pre-calculate the score threshold and guide the agent step-by-step through the selection logic to reduce cognitive load and potential misinterpretation.

---

<SYSTEM_PROMPT>
You are a highly precise Rubik's Cube solver assistant. Your core function is to act as a **STRICT RULE-FOLLOWER** and **EXACT DATA PARSER**. Your task is to apply specific selection rules to a provided lookup table and **ABSOLUTELY EXACTLY COPY** the results.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

**MOVE SELECTION RULES (CRITICAL - FOLLOW PRECISELY, NO EXCEPTIONS):**

**white_cross phase:**
1.  Check if any U-face move (U, U', U2) exists in the provided lookup table.
2.  From these U-face moves, identify any that have a score **>= (current score - 2)**.
3.  If such U-face moves are found:
    *   **SELECT THE VERY FIRST** of these qualifying U-face moves as it appears in the lookup table.
4.  Otherwise (if no U-face move meets the score condition):
    *   **SELECT THE VERY FIRST** entry in the entire lookup table.

**full_solve phase:**
- SELECT THE VERY FIRST entry in the lookup table (which is always the highest score).

**COPY RULE (ABSOLUTELY STRICT - NO MODIFICATION PERMITTED):**
- You **MUST** copy the `next_state` **ABSOLUTELY EXACTLY** as it appears on the chosen line in the lookup table.
- **DO NOT COMPUTE, MODIFY, OR INFER THE NEXT STATE.** Your role is NOT to simulate the cube or predict the outcome of a move.
- Copy **ONLY** the 54-character string that appears **BETWEEN** ": " and "  [score=" on the chosen line.

**REQUIREMENTS (ABSOLUTELY CRITICAL - ADHERE STRICTLY, NO EXTRA TEXT):**
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown, no comments).
- `next_state` MUST be copied **EXACTLY** from the lookup table — the 54 characters before "[score=".
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: {previous_move}

Current state:
```
{current_state}
```

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

--- SELECTION AND COPYING INSTRUCTIONS (FOLLOW THESE STEPS EXACTLY) ---
1.  You are in the '{phase}' phase.
2.  Your current score is {current_score}.
3.  Calculate the required score threshold for U-face moves: {current_score} - 2 = **{score_threshold}**.
4.  Examine the 'MOVE LOOKUP TABLE' carefully.
    *   **First, check for any U-face moves (U, U', U2)** that have a score **>= {score_threshold}**.
    *   If you find one or more such U-face moves, **SELECT THE FIRST ONE** that appears in the table.
    *   If no U-face moves meet this condition, **SELECT THE VERY FIRST ENTRY** in the entire lookup table (regardless of move type).
5.  Once you have identified the chosen move and its corresponding next_state string from the table, **COPY THE 54-CHARACTER next_state STRING ABSOLUTELY EXACTLY**. **DO NOT COMPUTE OR ALTER IT IN ANY WAY.**

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>
</USER_PROMPT>

---

## Actual LLM Prompt at Step 25 (fallback)

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your core function is to act as a **STRICT RULE-FOLLOWER** and **EXACT DATA PARSER**. Your task is to apply specific selection rules to a provided lookup table and **ABSOLUTELY EXACTLY COPY** the results.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

**MOVE SELECTION RULES (CRITICAL - FOLLOW PRECISELY, NO EXCEPTIONS):**

**white_cross phase:**
1.  Check if any U-face move (U, U', U2) exists in the provided lookup table.
2.  From these U-face moves, identify any that have a score **>= (current score - 2)**.
3.  If such U-face moves are found:
    *   **SELECT THE VERY FIRST** of these qualifying U-face moves as it appears in the lookup table.
4.  Otherwise (if no U-face move meets the score condition):
    *   **SELECT THE VERY FIRST** entry in the entire lookup table.

**full_solve phase:**
- SELECT THE VERY FIRST entry in the lookup table (which is always the highest score).

**COPY RULE (ABSOLUTELY STRICT - NO MODIFICATION PERMITTED):**
- You **MUST** copy the `next_state` **ABSOLUTELY EXACTLY** as it appears on the chosen line in the lookup table.
- **DO NOT COMPUTE, MODIFY, OR INFER THE NEXT STATE.** Your role is NOT to simulate the cube or predict the outcome of a move.
- Copy **ONLY** the 54-character string that appears **BETWEEN** ": " and "  [score=" on the chosen line.

**REQUIREMENTS (ABSOLUTELY CRITICAL - ADHERE STRICTLY, NO EXTRA TEXT):**
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown, no comments).
- `next_state` MUST be copied **EXACTLY** from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2

Current state:
```
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY
```

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

--- SELECTION AND COPYING INSTRUCTIONS (FOLLOW THESE STEPS EXACTLY) ---
1.  You are in the '{phase}' phase.
2.  Your current score is {current_score}.
3.  Calculate the required score threshold for U-face moves: {current_score} - 2 = **{score_threshold}**.
4.  Examine the 'MOVE LOOKUP TABLE' carefully.
    *   **First, check for any U-face moves (U, U', U2)** that have a score **>= {score_threshold}**.
    *   If you find one or more such U-face moves, **SELECT THE FIRST ONE** that appears in the table.
    *   If no U-face moves meet this condition, **SELECT THE VERY FIRST ENTRY** in the entire lookup table (regardless of move type).
5.  Once you have identified the chosen move and its corresponding next_state string from the table, **COPY THE 54-CHARACTER next_state STRING ABSOLUTELY EXACTLY**. **DO NOT COMPUTE OR ALTER IT IN ANY WAY.**

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Fallback at Step 25, Retry 3

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your primary task is to apply specific move selection and state copying rules with absolute accuracy.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (STRICT):
- The MOVE LOOKUP TABLE is always sorted best-first; the first entry is the highest scoring move overall.

- MOVE SELECTION RULE (white_cross phase):
  1. Calculate the required minimum score for U-face moves: `current score - 2`.
  2. Identify all U-face moves (U, U', U2) in the table whose score is greater than or equal to this minimum score.
  3. If ANY such qualifying U-face move exists, select the *first one* among these qualifying U-face moves as it appears in the table.
  4. If NO qualifying U-face move exists, then select the *first entry* in the *entire table*.

- MOVE SELECTION RULE (full_solve phase):
  - Pick the FIRST entry in the table (highest score).

COPY RULE (CRITICAL):
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table. Any deviation will result in failure.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

      OOG
      GWB
      WBB
BWO GYY ORR WWW
OOR WGG RRB WBY
OOY RGG RRR WBY
      BYY
      GYY
      GOB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

DETAILED REASONING PROCESS:
1.  **Determine Phase:** The current phase is `white_cross`.
2.  **Calculate Required Minimum Score for U-face Moves:** `Current score (5) - 2 = 3`.
3.  **Identify Qualifying U-face Moves:**
    *   U-face moves are U, U', U2. We need moves with score >= 3.
    *   From the `MOVE LOOKUP TABLE`:
        *   `U` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U'` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U2` is not listed with a qualifying score in the table.
4.  **Select Move:** Since qualifying U-face moves exist, we must apply Rule 3 for `white_cross` phase: "select the *first one* among these qualifying U-face moves as it appears in the table."
    *   The first qualifying U-face move in the table is `U`.
5.  **Identify and Copy next_state (CRITICAL):** Copy the 54-character string associated with the chosen move `U` EXACTLY from its line in the table.
    *   The selected line is: `U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]`
    *   The `next_state` string to copy is the 54 characters strictly between ": " and "  [score=":
        `GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY`

FINAL OUTPUT (EXACTLY two lines):
move = U
next_state = GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

### Failed Predictions
- Agent 25:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 25:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent 25:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 25:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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
The agents failed with "Inconsistent prediction: next_state does not match current_state + move". This error typically arises when the `next_state` output by the agent, for a chosen `move`, does not match the actual state that results from applying that `move` to the `current_state`.

Given the strict "COPY RULE" in the original system prompt ("Do NOT compute or modify next_state — copy it character-by-character from the table"), the agent is explicitly forbidden from calculating the `next_state`. This implies two primary failure modes for the agents:

1.  **Misinterpretation of Move Selection Rules:** The rule "If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it." is ambiguous if multiple U-face moves qualify. The agents might not be picking the *intended* U-face move, or they might be ignoring this rule entirely and picking the overall best move (`F'`, score 7).
2.  **Parsing/Copying Error:** Even if the correct move is identified, the agent might fail to copy the `next_state` string accurately from the lookup table due to misidentifying the correct line, copying the wrong part of the line, or making a transcription error.

My improved prompts aim to address these issues by:
*   **Clarifying the Move Selection Rule:** Explicitly stating to pick the *first* qualifying U-face move from the sorted table.
*   **Reinforcing the Copy Rule:** Emphasizing its criticality and providing a very clear example in the user prompt.
*   **Structured Reasoning:** Guiding the agent through a step-by-step reasoning process within the user prompt, acting as a few-shot example for precise execution.

---

<SYSTEM_PROMPT>
You are a highly precise Rubik's Cube solver assistant. Your primary task is to apply specific move selection and state copying rules with absolute accuracy.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (STRICT):
- The MOVE LOOKUP TABLE is always sorted best-first; the first entry is the highest scoring move overall.

- MOVE SELECTION RULE (white_cross phase):
  1. Calculate the required minimum score for U-face moves: `current score - 2`.
  2. Identify all U-face moves (U, U', U2) in the table whose score is greater than or equal to this minimum score.
  3. If ANY such qualifying U-face move exists, select the *first one* among these qualifying U-face moves as it appears in the table.
  4. If NO qualifying U-face move exists, then select the *first entry* in the *entire table*.

- MOVE SELECTION RULE (full_solve phase):
  - Pick the FIRST entry in the table (highest score).

COPY RULE (CRITICAL):
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table. Any deviation will result in failure.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: {previous_move}

Current state:
{current_state}

{state_visual}

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

DETAILED REASONING PROCESS:
1.  **Determine Phase:** The current phase is `white_cross`.
2.  **Calculate Required Minimum Score for U-face Moves:** `Current score (5) - 2 = 3`.
3.  **Identify Qualifying U-face Moves:**
    *   U-face moves are U, U', U2. We need moves with score >= 3.
    *   From the `MOVE LOOKUP TABLE`:
        *   `U` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U'` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U2` is not listed with a qualifying score in the table.
4.  **Select Move:** Since qualifying U-face moves exist, we must apply Rule 3 for `white_cross` phase: "select the *first one* among these qualifying U-face moves as it appears in the table."
    *   The first qualifying U-face move in the table is `U`.
5.  **Identify and Copy next_state (CRITICAL):** Copy the 54-character string associated with the chosen move `U` EXACTLY from its line in the table.
    *   The selected line is: `U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]`
    *   The `next_state` string to copy is the 54 characters strictly between ": " and "  [score=":
        `GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY`

FINAL OUTPUT (EXACTLY two lines):
move = U
next_state = GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY
</USER_PROMPT>

---

## Actual LLM Prompt at Step 25 (fallback)

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your primary task is to apply specific move selection and state copying rules with absolute accuracy.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (STRICT):
- The MOVE LOOKUP TABLE is always sorted best-first; the first entry is the highest scoring move overall.

- MOVE SELECTION RULE (white_cross phase):
  1. Calculate the required minimum score for U-face moves: `current score - 2`.
  2. Identify all U-face moves (U, U', U2) in the table whose score is greater than or equal to this minimum score.
  3. If ANY such qualifying U-face move exists, select the *first one* among these qualifying U-face moves as it appears in the table.
  4. If NO qualifying U-face move exists, then select the *first entry* in the *entire table*.

- MOVE SELECTION RULE (full_solve phase):
  - Pick the FIRST entry in the table (highest score).

COPY RULE (CRITICAL):
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table. Any deviation will result in failure.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: 25
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U2

Current state:
OOGGWBWBBORRRRBRRRGYYWGGRGGBYYGYYGOBBWOOOROOYWWWWBYWBY

      OOG
      GWB
      WBB
BWO GYY ORR WWW
OOR WGG RRB WBY
OOY RGG RRR WBY
      BYY
      GYY
      GOB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : OOGGWBORRYRRYRBBRRYGGYGGGWRORYGYYGOBBWBOOBOOWWWWWBYWBY  [score=7]
  F2 : OOGGWBYYBYRRRRBORRGGRGGWYYGBBWGYYGOBBWROOROOOWWWWBYWBY  [score=7]
  L  : GOGWWBRBBORRRRBRRRBYYGGGGGGYYYYYYWOBORYWOOBOOWWWWBGWBO  [score=7]
  L' : YOGYWBWBBORRRRBRRROYYGGGWGGGYYWYYROBOOBOOWYROWWGWBGWBB  [score=7]
  L2 : BOGGWBGBBORRRRBRRRYYYYGGWGGOYYGYYWOBYOOROOOWBWWRWBWWBG  [score=7]
  B2 : BOGGWBWBBORORRORRBGYYWGGRGGBYYGYYGOORWOBORROYYBWYBWWWW  [score=7]
  R  : OOWGWWWBWRBRRRRORRGYGWGBRGBBYYGYGGOGBWOOOROOYBWWYBYYBY  [score=5]
  R' : OOYGWGWBGRRORRRRBRGYYWGYRGBBYWGYWGOWBWOOOROOYBWWBBYGBY  [score=5]
  R2 : OOYGWYWBBRRRBRRRROGYWWGWRGWBYGGYBGOBBWOOOROOYGWWGBYYBY  [score=5]
  F  : OOGGWBYROWRRBRBBRRRWGGGYGGYRROGYYGOBBWBOOYOOYWWWWBYWBY  [score=5]
  D  : OOGGWBWBBORRRRBWBYGYYWGGRRRYYBYYOBGGBWOOORRGGWWWWBYOOY  [score=5]
  D' : OOGGWBWBBORRRRBRGGGYYWGGOOYGGBOYYBYYBWOOORWBYWWWWBYRRR  [score=5]
  D2 : OOGGWBWBBORRRRBOOYGYYWGGWBYBOGYYGYYBBWOOORRRRWWWWBYRGG  [score=5]
  B  : RBRGWBWBBORBRRORRGGYYWGGRGGBYYGYYBOOGWOOOROOYWWWBBWYYW  [score=5]
  B' : OOBGWBWBBORORRORRGGYYWGGRGGBYYGYYRBRGWOOORBOYWYYWBBWWW  [score=5]
  U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]
  U' : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]

DETAILED REASONING PROCESS:
1.  **Determine Phase:** The current phase is `white_cross`.
2.  **Calculate Required Minimum Score for U-face Moves:** `Current score (5) - 2 = 3`.
3.  **Identify Qualifying U-face Moves:**
    *   U-face moves are U, U', U2. We need moves with score >= 3.
    *   From the `MOVE LOOKUP TABLE`:
        *   `U` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U'` has score 3. (3 >= 3) -> QUALIFIES.
        *   `U2` is not listed with a qualifying score in the table.
4.  **Select Move:** Since qualifying U-face moves exist, we must apply Rule 3 for `white_cross` phase: "select the *first one* among these qualifying U-face moves as it appears in the table."
    *   The first qualifying U-face move in the table is `U`.
5.  **Identify and Copy next_state (CRITICAL):** Copy the 54-character string associated with the chosen move `U` EXACTLY from its line in the table.
    *   The selected line is: `U  : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]`
    *   The `next_state` string to copy is the 54 characters strictly between ": " and "  [score=":
        `GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY`

FINAL OUTPUT (EXACTLY two lines):
move = U
next_state = GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

---

## Fallback at Step 26, Retry 1

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 26
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

### Failed Predictions
- Agent cycle_detector: action=N/A, state=GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 26
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent cycle_detector: predicted action=N/A, predicted state=GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

## Actual LLM Prompt at Step 26 (fallback)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 26
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

Step: 26
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 3
Previous move: U

Current state:
GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  R2 : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  F' : GBBOWBGRRYYYYRBBRROGGWGGBWRWRYGYYGOBWWWOOGOOOORRWBYWBY  [score=5]
  F2 : GBBOWBYYBYYYRRBWRRGGRGGWOWBWGOGYYGOBWWROOROOGORRWBYWBY  [score=5]
  L  : BBBWWBRGWGYYRRBRRRBWOGGGGGGYYYYYYROBWRYWOOWOOOROWBOWBG  [score=5]
  L' : YBBYWBRGWGYYRRBRRRGWOOGGOGGBYYWYYROBOOWOOWYRWORGWBGWBB  [score=5]
  L2 : BBBGWBGGWGYYRRBRRRYWOYGGRGGGYYOYYOOBYOOROOWWWORRWBWWBB  [score=5]
  B2 : BOGOWBOGWGYORRORRWBWOWGGRGGBYYGYYBBGRWWBORYOYYBWYBWRRO  [score=5]
  U  : BBWBWGGOOBWORRBRRRWWWWGGRGGBYYGYYGOBORROOROOYGYYWBYWBY  [score=3]
  U2 : WGOBWOBBGWWWRRBRRRORRWGGRGGBYYGYYGOBGYYOOROOYBWOWBYWBY  [score=3]
  F  : GBBOWBYRWOYYGRBWRRRWBGGWGGORRGGYYGOBWWBOOYOOYORRWBYWBY  [score=3]
  D  : GBBOWBOGWGYYRRBWBYBWOWGGRRRYYBYYOBGGWWWOORRGGORRWBYOOY  [score=3]
  D' : GBBOWBOGWGYYRRBRGGBWOWGGOOYGGBOYYBYYWWWOORWBYORRWBYRRR  [score=3]
  D2 : GBBOWBOGWGYYRRBOOYBWOWGGWBYBOGYYGYYBWWWOORRRRORRWBYRGG  [score=3]
  B  : YBROWBOGWGYBRRORRGBWOWGGRGGBYYGYYWOOBWWBORGOYWWOBBRYYR  [score=3]
  B' : OOWOWBOGWGYGRRBRRBBWOWGGRGGBYYGYYRBYGWWOORBOYRYYRBBOWW  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 27 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 27
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: R

Current state:
GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  U' : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  F2 : GBWOWWOYBYBRRRRWRRWGRBGWBWBOGOGYGGOGWWGOOYOOYBRRYBYYBY  [score=7]
  L  : BBWWWWRGOYBRYRRGRRBWBGGBGGWYYOYYGROGWRYWOOWOOBROYBOYBG  [score=7]
  L' : YBWYWWRGOYBRYRRGRRGWBOGBOGWBYOWYGROGOOWOOWYRWBRGYBGYBB  [score=7]
  L2 : BBWGWWGGOYBRYRRGRRYWBYGBRGWGYOOYGOOGYOOROOWWWBRRYBWYBB  [score=7]
  B2 : GOGOWWOGOYBOYROGRWBWBWGBRGWBYOGYGWBGRWWRORROYYBYYBYRRB  [score=7]
  U2 : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  R  : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  R2 : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  F  : GBWOWWYRWOBRGRRORRRWBGGWWBBGYYGYGGOGWWBOOYOOOBRRYBYYBY  [score=5]
  F' : GBWOWWYYGOBRYRRBRRBBWWGGBWRWRYGYGGOGWWOOOGOOOBRRYBYYBY  [score=5]
  D  : GBWOWWOGOYBRYRRYBYBWBWGBGRROGGYYOBGGWWWOORRGWBRRYBYOOY  [score=5]
  D' : GBWOWWOGOYBRYRRRGWBWBWGBOOYGGBOYYGGOWWWOORYBYBRRYBYGRR  [score=5]
  D2 : GBWOWWOGOYBRYRROOYBWBWGBYBYGOGGYGOYBWWWOORGRRBRRYBYRGW  [score=5]
  B  : RRROWWOGOYBGYROGRGBWBWGBRGWBYOGYGWOOWWWBORGOYYYBBBRYYR  [score=5]
  B' : OOWOWWOGOYBGYRBGRWBWBWGBRGWBYOGYGRRRGWWOORGOYRYYRBBBYY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 28 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 28
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  U2 : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 29 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 29
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R  : OGYWWYWBBWRRWRRWYGBROWGORGGBYRGYBGOWYBROOROOYGWBGBYOBY  [score=7]
  R2 : OGOWWGWBGRRGRRYWWWBRYWGYRGBBYOGYOGOGYBROOROOYWWBBBYRBY  [score=7]
  F2 : OGOWWOOYBYWWRRRRRRWGRBGWRRBGBWGYGGOGYBGOOYOOWBWBYBYYBY  [score=7]
  B2 : GOGWWOWBGWWOYROGRYBRRWGBRGWBYOGYGOGORBRRORWOYYBYYBYBWB  [score=7]
  U2 : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OGRWWBWBWGYWRRWRRWBROWGGRGGBYYGYYGOBYBROOROOYGWBOBYOBY  [score=5]
  F  : OGOWWOYRRWWWBRRGRRRWBGGRWBRGYWGYGGOGYBBOOYOOOBWBYBYYBY  [score=5]
  F' : OGOWWOWYGOWWYRRBRRRBWRGGBWRRRYGYGGOGYBGOOBOOWBWBYBYYBY  [score=5]
  D  : OGOWWOWBGWWWYRRYBYBRRWGBGRROGGYYOBGGYBROORRGWBWBYBYOOY  [score=5]
  D' : OGOWWOWBGWWWYRRRGWBRRWGBOOYGGBOYYGGOYBROORYBYBWBYBYGRR  [score=5]
  D2 : OGOWWOWBGWWWYRROOYBRRWGBYBYGOGGYGOYBYBROORGRRBWBYBYRGW  [score=5]
  L  : BGOWWORBGWWWYRRGRRBRRGGBGGWYYOYYGBOGRRYBOOYOOBWWYBWYBO  [score=5]
  L' : YGOYWOBBGWWWYRRGRRORRWGBWGWBYOWYGROGOOYOOBYRRBWGYBGYBB  [score=5]
  L2 : BGOGWOGBGWWWYRRGRRYRRYGBBGWOYOWYGWOGYOOROORBYBWRYBWYBB  [score=5]
  B  : WRRWWOWBGWWGYROGRGBRRWGBRGWBYOGYGYOOOBRGOROOYYYBBBWYYB  [score=5]
  B' : OOYWWOWBGWWOYRGGROBRRWGBRGWBYOGYGRRWGBROORGOYBYYWBBBYY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 30 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 30
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : YOGWWBRWWBRRYRRGRRBBRGGBGGWYYOYYGWOGBRYWOOBOOWWOYBGYBO  [score=9]
  L' : YOGYWBWWWBRRYRRGRROBRGGBOGWYYOWYGROGOOBOOWYRBWWGYBGYBB  [score=9]
  L2 : BOGGWBGWWBRRYRRGRRYBRYGBWGWOYOGYGOOGYOOROOBWBWWRYBWYBY  [score=9]
  B2 : GOGGWBOWWBROYROGRBYBRWGBRGWBYOGYGGOORWBRORROYYBYYBYWWW  [score=9]
  U2 : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  R  : OOYGWYOWWRRRRRRBYGYBGWGBRGWBYRGYBGOWBWBOOROOYGWWGBYOBY  [score=7]
  R2 : OOOGWGOWGRRGRRYRRBYBYWGYRGWBYGGYBGOWBWBOOROOYWWWBBYRBY  [score=7]
  F2 : OOGGWBOYBYRRRRRBRRWGRBGWRBYWWOGYGGOGBWGOOYOOBWWWYBYYBY  [score=7]
  D  : OOGGWBOWWBRRYRRYBYYBRWGBGRROGGYYOBGGBWBOORRGWWWWYBYOOY  [score=7]
  D' : OOGGWBOWWBRRYRRRGWYBRWGBOOYGGBOYYGGOBWBOORYBYWWWYBYGRR  [score=7]
  D2 : OOGGWBOWWBRRYRROOYYBRWGBYBYGOGGYGOYBBWBOORGRRWWWYBYRGW  [score=7]
  B  : RRRGWBOWWBRGYROGRGYBRWGBRGWBYOGYGBOOGWBOOROOYYYWBBWYYW  [score=7]
  B' : OOBGWBOWWBROYROGRGYBRWGBRGWBYOGYGRRRGWBOORGOYWYYWBBWYY  [score=7]
  U  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OORGWBOWWGYBRRRRRRYBOWGGRGGBYYGYYGOWBWBOOROOYWWWBBYGBY  [score=5]
  F  : OOGGWBYRBORRWRRWRRRWYGGBWBRGYBGYGGOGBWBOOYOOOWWWYBYYBY  [score=5]
  F' : OOGGWBBYGORRYRRBRRRBWBGGYWRBRYGYGGOGBWWOOWOOOWWWYBYYBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 31 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 31
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  U' : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 32 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 32
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R  : OGYWWYWBBWRRWRRWYGBROWGORGGBYRGYBGOWYBROOROOYGWBGBYOBY  [score=7]
  R2 : OGOWWGWBGRRGRRYWWWBRYWGYRGBBYOGYOGOGYBROOROOYWWBBBYRBY  [score=7]
  F2 : OGOWWOOYBYWWRRRRRRWGRBGWRRBGBWGYGGOGYBGOOYOOWBWBYBYYBY  [score=7]
  B2 : GOGWWOWBGWWOYROGRYBRRWGBRGWBYOGYGOGORBRRORWOYYBYYBYBWB  [score=7]
  U2 : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OGRWWBWBWGYWRRWRRWBROWGGRGGBYYGYYGOBYBROOROOYGWBOBYOBY  [score=5]
  F  : OGOWWOYRRWWWBRRGRRRWBGGRWBRGYWGYGGOGYBBOOYOOOBWBYBYYBY  [score=5]
  F' : OGOWWOWYGOWWYRRBRRRBWRGGBWRRRYGYGGOGYBGOOBOOWBWBYBYYBY  [score=5]
  D  : OGOWWOWBGWWWYRRYBYBRRWGBGRROGGYYOBGGYBROORRGWBWBYBYOOY  [score=5]
  D' : OGOWWOWBGWWWYRRRGWBRRWGBOOYGGBOYYGGOYBROORYBYBWBYBYGRR  [score=5]
  D2 : OGOWWOWBGWWWYRROOYBRRWGBYBYGOGGYGOYBYBROORGRRBWBYBYRGW  [score=5]
  L  : BGOWWORBGWWWYRRGRRBRRGGBGGWYYOYYGBOGRRYBOOYOOBWWYBWYBO  [score=5]
  L' : YGOYWOBBGWWWYRRGRRORRWGBWGWBYOWYGROGOOYOOBYRRBWGYBGYBB  [score=5]
  L2 : BGOGWOGBGWWWYRRGRRYRRYGBBGWOYOWYGWOGYOOROORBYBWRYBWYBB  [score=5]
  B  : WRRWWOWBGWWGYROGRGBRRWGBRGWBYOGYGYOOOBRGOROOYYYBBBWYYB  [score=5]
  B' : OOYWWOWBGWWOYRGGROBRRWGBRGWBYOGYGRRWGBROORGOYBYYWBBBYY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 33 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 33
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : YOGWWBRWWBRRYRRGRRBBRGGBGGWYYOYYGWOGBRYWOOBOOWWOYBGYBO  [score=9]
  L' : YOGYWBWWWBRRYRRGRROBRGGBOGWYYOWYGROGOOBOOWYRBWWGYBGYBB  [score=9]
  L2 : BOGGWBGWWBRRYRRGRRYBRYGBWGWOYOGYGOOGYOOROOBWBWWRYBWYBY  [score=9]
  B2 : GOGGWBOWWBROYROGRBYBRWGBRGWBYOGYGGOORWBRORROYYBYYBYWWW  [score=9]
  U2 : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  R  : OOYGWYOWWRRRRRRBYGYBGWGBRGWBYRGYBGOWBWBOOROOYGWWGBYOBY  [score=7]
  R2 : OOOGWGOWGRRGRRYRRBYBYWGYRGWBYGGYBGOWBWBOOROOYWWWBBYRBY  [score=7]
  F2 : OOGGWBOYBYRRRRRBRRWGRBGWRBYWWOGYGGOGBWGOOYOOBWWWYBYYBY  [score=7]
  D  : OOGGWBOWWBRRYRRYBYYBRWGBGRROGGYYOBGGBWBOORRGWWWWYBYOOY  [score=7]
  D' : OOGGWBOWWBRRYRRRGWYBRWGBOOYGGBOYYGGOBWBOORYBYWWWYBYGRR  [score=7]
  D2 : OOGGWBOWWBRRYRROOYYBRWGBYBYGOGGYGOYBBWBOORGRRWWWYBYRGW  [score=7]
  B  : RRRGWBOWWBRGYROGRGYBRWGBRGWBYOGYGBOOGWBOOROOYYYWBBWYYW  [score=7]
  B' : OOBGWBOWWBROYROGRGYBRWGBRGWBYOGYGRRRGWBOORGOYWYYWBBWYY  [score=7]
  U  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OORGWBOWWGYBRRRRRRYBOWGGRGGBYYGYYGOWBWBOOROOYWWWBBYGBY  [score=5]
  F  : OOGGWBYRBORRWRRWRRRWYGGBWBRGYBGYGGOGBWBOOYOOOWWWYBYYBY  [score=5]
  F' : OOGGWBBYGORRYRRBRRRBWBGGYWRBRYGYGGOGBWWOOWOOOWWWYBYYBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 34 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 34
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  U' : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 35 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 35
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R  : OGYWWYWBBWRRWRRWYGBROWGORGGBYRGYBGOWYBROOROOYGWBGBYOBY  [score=7]
  R2 : OGOWWGWBGRRGRRYWWWBRYWGYRGBBYOGYOGOGYBROOROOYWWBBBYRBY  [score=7]
  F2 : OGOWWOOYBYWWRRRRRRWGRBGWRRBGBWGYGGOGYBGOOYOOWBWBYBYYBY  [score=7]
  B2 : GOGWWOWBGWWOYROGRYBRRWGBRGWBYOGYGOGORBRRORWOYYBYYBYBWB  [score=7]
  U2 : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OGRWWBWBWGYWRRWRRWBROWGGRGGBYYGYYGOBYBROOROOYGWBOBYOBY  [score=5]
  F  : OGOWWOYRRWWWBRRGRRRWBGGRWBRGYWGYGGOGYBBOOYOOOBWBYBYYBY  [score=5]
  F' : OGOWWOWYGOWWYRRBRRRBWRGGBWRRRYGYGGOGYBGOOBOOWBWBYBYYBY  [score=5]
  D  : OGOWWOWBGWWWYRRYBYBRRWGBGRROGGYYOBGGYBROORRGWBWBYBYOOY  [score=5]
  D' : OGOWWOWBGWWWYRRRGWBRRWGBOOYGGBOYYGGOYBROORYBYBWBYBYGRR  [score=5]
  D2 : OGOWWOWBGWWWYRROOYBRRWGBYBYGOGGYGOYBYBROORGRRBWBYBYRGW  [score=5]
  L  : BGOWWORBGWWWYRRGRRBRRGGBGGWYYOYYGBOGRRYBOOYOOBWWYBWYBO  [score=5]
  L' : YGOYWOBBGWWWYRRGRRORRWGBWGWBYOWYGROGOOYOOBYRRBWGYBGYBB  [score=5]
  L2 : BGOGWOGBGWWWYRRGRRYRRYGBBGWOYOWYGWOGYOOROORBYBWRYBWYBB  [score=5]
  B  : WRRWWOWBGWWGYROGRGBRRWGBRGWBYOGYGYOOOBRGOROOYYYBBBWYYB  [score=5]
  B' : OOYWWOWBGWWOYRGGROBRRWGBRGWBYOGYGRRWGBROORGOYBYYWBBBYY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 36 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 36
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : YOGWWBRWWBRRYRRGRRBBRGGBGGWYYOYYGWOGBRYWOOBOOWWOYBGYBO  [score=9]
  L' : YOGYWBWWWBRRYRRGRROBRGGBOGWYYOWYGROGOOBOOWYRBWWGYBGYBB  [score=9]
  L2 : BOGGWBGWWBRRYRRGRRYBRYGBWGWOYOGYGOOGYOOROOBWBWWRYBWYBY  [score=9]
  B2 : GOGGWBOWWBROYROGRBYBRWGBRGWBYOGYGGOORWBRORROYYBYYBYWWW  [score=9]
  U2 : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  R  : OOYGWYOWWRRRRRRBYGYBGWGBRGWBYRGYBGOWBWBOOROOYGWWGBYOBY  [score=7]
  R2 : OOOGWGOWGRRGRRYRRBYBYWGYRGWBYGGYBGOWBWBOOROOYWWWBBYRBY  [score=7]
  F2 : OOGGWBOYBYRRRRRBRRWGRBGWRBYWWOGYGGOGBWGOOYOOBWWWYBYYBY  [score=7]
  D  : OOGGWBOWWBRRYRRYBYYBRWGBGRROGGYYOBGGBWBOORRGWWWWYBYOOY  [score=7]
  D' : OOGGWBOWWBRRYRRRGWYBRWGBOOYGGBOYYGGOBWBOORYBYWWWYBYGRR  [score=7]
  D2 : OOGGWBOWWBRRYRROOYYBRWGBYBYGOGGYGOYBBWBOORGRRWWWYBYRGW  [score=7]
  B  : RRRGWBOWWBRGYROGRGYBRWGBRGWBYOGYGBOOGWBOOROOYYYWBBWYYW  [score=7]
  B' : OOBGWBOWWBROYROGRGYBRWGBRGWBYOGYGRRRGWBOORGOYWYYWBBWYY  [score=7]
  U  : GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY  [score=5]
  R' : OORGWBOWWGYBRRRRRRYBOWGGRGGBYYGYYGOWBWBOOROOYWWWBBYGBY  [score=5]
  F  : OOGGWBYRBORRWRRWRRRWYGGBWBRGYBGYGGOGBWBOOYOOOWWWYBYYBY  [score=5]
  F' : OOGGWBBYGORRYRRBRRRBWBGGYWRBRYGYGGOGBWWOOWOOOWWWYBYYBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 37 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 37
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
GBWOWWOGOYBRYRRGRRBWBWGBRGWBYOGYGGOGWWWOOROOYBRRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  F2 : GBWOWWOYBYBRRRRWRRWGRBGWBWBOGOGYGGOGWWGOOYOOYBRRYBYYBY  [score=7]
  L  : BBWWWWRGOYBRYRRGRRBWBGGBGGWYYOYYGROGWRYWOOWOOBROYBOYBG  [score=7]
  L' : YBWYWWRGOYBRYRRGRRGWBOGBOGWBYOWYGROGOOWOOWYRWBRGYBGYBB  [score=7]
  L2 : BBWGWWGGOYBRYRRGRRYWBYGBRGWGYOOYGOOGYOOROOWWWBRRYBWYBB  [score=7]
  B2 : GOGOWWOGOYBOYROGRWBWBWGBRGWBYOGYGWBGRWWRORROYYBYYBYRRB  [score=7]
  U2 : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  R  : GBYOWYOGBRRRBRRYYGBWWWGWRGOBYBGYBGOWWWWOOROOYGRRGBYOBY  [score=5]
  R2 : GBOOWGOGGRRGRRYRBYBWYWGYRGBBYWGYWGOOWWWOOROOYWRRBBYBBY  [score=5]
  F  : GBWOWWYRWOBRGRRORRRWBGGWWBBGYYGYGGOGWWBOOYOOOBRRYBYYBY  [score=5]
  F' : GBWOWWYYGOBRYRRBRRBBWWGGBWRWRYGYGGOGWWOOOGOOOBRRYBYYBY  [score=5]
  D  : GBWOWWOGOYBRYRRYBYBWBWGBGRROGGYYOBGGWWWOORRGWBRRYBYOOY  [score=5]
  D' : GBWOWWOGOYBRYRRRGWBWBWGBOOYGGBOYYGGOWWWOORYBYBRRYBYGRR  [score=5]
  D2 : GBWOWWOGOYBRYRROOYBWBWGBYBYGOGGYGOYBWWWOORGRRBRRYBYRGW  [score=5]
  B  : RRROWWOGOYBGYROGRGBWBWGBRGWBYOGYGWOOWWWBORGOYYYBBBRYYR  [score=5]
  B' : OOWOWWOGOYBGYRBGRWBWBWGBRGWBYOGYGRRRGWWOORGOYRYYRBBBYY  [score=5]
  R' : GBBOWBOGWGYYRRBRRRBWOWGGRGGBYYGYYGOBWWWOOROOYORRWBYWBY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Fallback at Step 38, Retry 1

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 38
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  U2 : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

### Failed Predictions
- Agent cycle_detector: action=N/A, state=WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 38
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  U2 : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent cycle_detector: predicted action=N/A, predicted state=WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

## Actual LLM Prompt at Step 38 (fallback)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 38
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  U2 : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

Step: 38
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  R2 : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F2 : WWOBWGOYBYWBRRRRRRWGRBGWWWWOOGGYGGOGBRGOOYOOBYBRYBYYBY  [score=9]
  L  : WWOWWGROOBWBYRRGRRBWWGGBGGWYYOYYGROGRRYROOBOOYBGYBBYBW  [score=9]
  L' : YWOYWGROOBWBYRRGRRWWWBGBGGWWYOWYGROGOOBOORYRRYBGYBGYBB  [score=9]
  L2 : BWOGWGGOOBWBYRRGRRYWWYGBRGWWYOBYGGOGYOOROORRBYBRYBWYBW  [score=9]
  U2 : OOGGWBOWWBRRYRRGRRYBRWGBRGWBYOGYGGOGBWBOOROOYWWWYBYYBY  [score=7]
  R' : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  F  : WWOBWGYRRGWBORRORRRWWGGWWBWGYBGYGGOGBRBOOYOOOYBRYBYYBY  [score=7]
  F' : WWOBWGBYGOWBYRRBRRWBWWGGWWRRRYGYGGOGBROOOOOOGYBRYBYYBY  [score=7]
  D  : WWOBWGGOOBWBYRRYBYWWWWGBGRROGGYYOBGGBRROORRGWYBRYBYOOY  [score=7]
  D' : WWOBWGGOOBWBYRRRGWWWWWGBOOYGGBOYYGGOBRROORYBYYBRYBYGRR  [score=7]
  D2 : WWOBWGGOOBWBYRROOYWWWWGBYBYGOGGYGOYBBRROORGRRYBRYBYRGW  [score=7]
  U  : OGOWWOWBGWWWYRRGRRBRRWGBRGWBYOGYGGOGYBROOROOYBWBYBYYBY  [score=5]
  B2 : GOGBWGGOOBWOYROGRBWWWWGBRGWBYOGYGOWWRRRRORBOYYBYYBYRBY  [score=5]
  B  : BRRBWGGOOBWGYROGRGWWWWGBRGWBYOGYGBOOORRWORWOYYYYBBBYYR  [score=3]
  B' : OOBBWGGOOBWWYRWGROWWWWGBRGWBYOGYGRRBGRROORGOYRYYBBBYYY  [score=3]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 39 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 39
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: R

Current state:
WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F2 : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  L  : WWYWWYROYBRRWRRBYGBWOGGGGGOYYWYYBROWRRYROOBOOGBGGBBOBW  [score=11]
  L' : YWYYWYROYBRRWRRBYGWWOBGGGGOWYWWYBROWOOBOORYRRGBGGBGOBB  [score=11]
  L2 : BWYGWYGOYBRRWRRBYGYWOYGGRGOWYWBYBGOWYOOROORRBGBRGBWOBW  [score=11]
  R  : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F  : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  D  : WWYBWYGOYBRRWRROBYWWOWGGBYGWBWYYOBGGBRROORRGOGBRGBYOOY  [score=9]
  D' : WWYBWYGOYBRRWRRRGOWWOWGGOOYGGBOYYWBWBRROOROBYGBRGBYBYG  [score=9]
  D2 : WWYBWYGOYBRRWRROOYWWOWGGOBYWOGBYGWYBBRROORBYGGBRGBYRGO  [score=9]
  U2 : YOGYWBYWWBRRWRRBYGGBRWGGRGOBYWGYBGOWBRROOROOYWWOGBYOBY  [score=7]
  R2 : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  B2 : WOGBWYGOYBROWROBYBWWOWGGRGOBYWGYBYWWGRRRORROYYBOYBGRBG  [score=7]
  U  : YYYWWOWBGWWOWRRBYGBRRWGGRGOBYWGYBGOWGBROOROOYBRRGBYOBY  [score=5]
  U' : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  B  : RRGBWYGOYBRWWROBYGWWOWGGRGOBYWGYBBOOYRRWORWOYOGGBBBYYR  [score=5]
  B' : OOBBWYGOYBRWWRWBYYWWOWGGRGOBYWGYBGRRGRROORWOYRYYBBBGGO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 40 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 40
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
YYYWWOWBGWWOWRRBYGBRRWGGRGOBYWGYBGOWGBROOROOYBRRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : YYYWWOWWBWWOYRRBYGRGORGGBWRRRYGYBGOWGBGOOBOOWBRRGBYOBY  [score=9]
  U  : YOGYWBYWWBRRWRRBYGGBRWGGRGOBYWGYBGOWBRROOROOYWWOGBYOBY  [score=7]
  R  : YYOWWGWBBORGWRYWWBBRYWGORGGBYRGYGGOOGBROOROOYWRRBBYWBY  [score=7]
  F2 : YYYWWOWYBYWORRRRYGOGRGGWRRBGBWGYBGOWGBBOOWOOWBRRGBYOBY  [score=7]
  B2 : WOGWWOWBGWWOWROBYGBRRWGGRGOBYWGYBYYYGBRROROOYYBOYBGRRB  [score=7]
  U2 : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  R' : YYRWWGWBOBWWYRWGROBRWWGBRGWBYOGYGGOBGBROOROOYGRROBYYBY  [score=5]
  R2 : YYWWWBWBWGYBRRWOWWBROWGGRGBBYYGYOGOGGBROOROOYORRGBYRBY  [score=5]
  F  : YYYWWOYRRWWOBRRGYGRWBGGROGRBWWGYBGOWGBBOOYOOWBRRGBYOBY  [score=5]
  D  : YYYWWOWBGWWOWRROBYBRRWGGBYGWBWYYOBGGGBROORRGOBRRGBYOOY  [score=5]
  D' : YYYWWOWBGWWOWRRRGOBRRWGGOOYGGBOYYWBWGBROOROBYBRRGBYBYG  [score=5]
  D2 : YYYWWOWBGWWOWRROOYBRRWGGOBYWOGBYGWYBGBROORBYGBRRGBYRGO  [score=5]
  L  : BYYWWORBGWWOWRRBYGBRRGGGGGOYYWYYBROWRRYBOOGOOBRWGBWOBY  [score=5]
  L' : YYYYWORBGWWOWRRBYGYRRWGGWGOBYWWYBROWOOGOOBYRRBRGGBGOBB  [score=5]
  L2 : BYYGWOGBGWWOWRRBYGYRRYGGRGOYYWWYBWOWYOOROORBGBRRGBWOBB  [score=5]
  B  : ORGWWOWBGWWWWROBYGBRRWGGRGOBYWGYBGOOYBRYORYOYOGBBBRYYR  [score=5]
  B' : OOGWWOWBGWWYWRYBYYBRRWGGRGOBYWGYBGROGBROORWOYRYYRBBBGO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 41 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 41
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
YOGYWBYWWBRRWRRBYGGBRWGGRGOBYWGYBGOWBRROOROOYWWOGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F' : YOGYWBBWBWRRYRRBYGRGOBGGGWRRRYGYBGOWBRWOOWOOYWWOGBYOBY  [score=9]
  L  : GOGWWBRWWBRRWRRBYGBBRGGGGGOYYWYYBOOWRRYROOBOOWWYGBYOBY  [score=9]
  L' : YOGYWBOWWBRRWRRBYGYBRYGGYGOGYWWYBROWOOBOORYRRWWGGBGOBB  [score=9]
  L2 : BOGGWBGWWBRRWRRBYGYBRYGGOGOYYWYYBYOWYOOROORRBWWRGBWOBG  [score=9]
  B2 : WOGYWBYWWBROWROBYBGBRWGGRGOBYWGYBGOYGRRRORROYYBOYBGOWW  [score=9]
  R  : YOOYWGYWWRRGRRYBWBGBGWGBRGWBYRGYGGOOBRROOROOYWWOBBYWBY  [score=7]
  F2 : YOGYWBWYBYRRRRRRYGOGRGGWRBGWWYGYBGOWBRBOOWOOBWWOGBYOBY  [score=7]
  D  : YOGYWBYWWBRRWRROBYGBRWGGBYGWBWYYOBGGBRROORRGOWWOGBYOOY  [score=7]
  D' : YOGYWBYWWBRRWRRRGOGBRWGGOOYGGBOYYWBWBRROOROBYWWOGBYBYG  [score=7]
  D2 : YOGYWBYWWBRRWRROOYGBRWGGOBYWOGBYGWYBBRROORBYGWWOGBYRGO  [score=7]
  B  : RRGYWBYWWBRWWROBYGGBRWGGRGOBYWGYBBOOGRROORYOYOGWBBWYYO  [score=7]
  B' : OOBYWBYWWBRYWROBYGGBRWGGRGOBYWGYBGRRGRROORWOYOYYWBBWGO  [score=7]
  U  : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  R' : YORYWGYWOBWBYRRGRRGBWWGBRGWBYOGYGGOWBRROOROOYWWOBBYGBY  [score=5]
  R2 : YOWYWBYWWGYBRRWRRBGBOWGGRGWBYGGYBGOWBRROOROOYOWOGBYRBY  [score=5]
  F  : YOGYWBYRRYRRWRRWYGRWGGGBOGRBWBGYBGOWBRBOOYOOWWWOGBYOBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 42 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 42
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U2

Current state:
WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F2 : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  L  : WWYWWYROYBRRWRRBYGBWOGGGGGOYYWYYBROWRRYROOBOOGBGGBBOBW  [score=11]
  L' : YWYYWYROYBRRWRRBYGWWOBGGGGOWYWWYBROWOOBOORYRRGBGGBGOBB  [score=11]
  L2 : BWYGWYGOYBRRWRRBYGYWOYGGRGOWYWBYBGOWYOOROORRBGBRGBWOBW  [score=11]
  R  : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F  : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  D  : WWYBWYGOYBRRWRROBYWWOWGGBYGWBWYYOBGGBRROORRGOGBRGBYOOY  [score=9]
  D' : WWYBWYGOYBRRWRRRGOWWOWGGOOYGGBOYYWBWBRROOROBYGBRGBYBYG  [score=9]
  D2 : WWYBWYGOYBRRWRROOYWWOWGGOBYWOGBYGWYBBRROORBYGGBRGBYRGO  [score=9]
  R' : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  R2 : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  B2 : WOGBWYGOYBROWROBYBWWOWGGRGOBYWGYBYWWGRRRORROYYBOYBGRBG  [score=7]
  U  : YYYWWOWBGWWOWRRBYGBRRWGGRGOBYWGYBGOWGBROOROOYBRRGBYOBY  [score=5]
  U' : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  B  : RRGBWYGOYBRWWROBYGWWOWGGRGOBYWGYBBOOYRRWORWOYOGGBBBYYR  [score=5]
  B' : OOBBWYGOYBRWWRWBYYWWOWGGRGOBYWGYBGRRGRROORWOYRYYBBBGGO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 43 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 43
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: U

Current state:
YYYWWOWBGWWOWRRBYGBRRWGGRGOBYWGYBGOWGBROOROOYBRRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : YYYWWOWWBWWOYRRBYGRGORGGBWRRRYGYBGOWGBGOOBOOWBRRGBYOBY  [score=9]
  U  : YOGYWBYWWBRRWRRBYGGBRWGGRGOBYWGYBGOWBRROOROOYWWOGBYOBY  [score=7]
  R  : YYOWWGWBBORGWRYWWBBRYWGORGGBYRGYGGOOGBROOROOYWRRBBYWBY  [score=7]
  F2 : YYYWWOWYBYWORRRRYGOGRGGWRRBGBWGYBGOWGBBOOWOOWBRRGBYOBY  [score=7]
  B2 : WOGWWOWBGWWOWROBYGBRRWGGRGOBYWGYBYYYGBRROROOYYBOYBGRRB  [score=7]
  U2 : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  R' : YYRWWGWBOBWWYRWGROBRWWGBRGWBYOGYGGOBGBROOROOYGRROBYYBY  [score=5]
  R2 : YYWWWBWBWGYBRRWOWWBROWGGRGBBYYGYOGOGGBROOROOYORRGBYRBY  [score=5]
  F  : YYYWWOYRRWWOBRRGYGRWBGGROGRBWWGYBGOWGBBOOYOOWBRRGBYOBY  [score=5]
  D  : YYYWWOWBGWWOWRROBYBRRWGGBYGWBWYYOBGGGBROORRGOBRRGBYOOY  [score=5]
  D' : YYYWWOWBGWWOWRRRGOBRRWGGOOYGGBOYYWBWGBROOROBYBRRGBYBYG  [score=5]
  D2 : YYYWWOWBGWWOWRROOYBRRWGGOBYWOGBYGWYBGBROORBYGBRRGBYRGO  [score=5]
  L  : BYYWWORBGWWOWRRBYGBRRGGGGGOYYWYYBROWRRYBOOGOOBRWGBWOBY  [score=5]
  L' : YYYYWORBGWWOWRRBYGYRRWGGWGOBYWWYBROWOOGOOBYRRBRGGBGOBB  [score=5]
  L2 : BYYGWOGBGWWOWRRBYGYRRYGGRGOYYWWYBWOWYOOROORBGBRRGBWOBB  [score=5]
  B  : ORGWWOWBGWWWWROBYGBRRWGGRGOBYWGYBGOOYBRYORYOYOGBBBRYYR  [score=5]
  B' : OOGWWOWBGWWYWRYBYYBRRWGGRGOBYWGYBGROGBROORWOYRYYRBBBGO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 44 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 44
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
YOGYWBYWWBRRWRRBYGGBRWGGRGOBYWGYBGOWBRROOROOYWWOGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U2 : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F' : YOGYWBBWBWRRYRRBYGRGOBGGGWRRRYGYBGOWBRWOOWOOYWWOGBYOBY  [score=9]
  L  : GOGWWBRWWBRRWRRBYGBBRGGGGGOYYWYYBOOWRRYROOBOOWWYGBYOBY  [score=9]
  L' : YOGYWBOWWBRRWRRBYGYBRYGGYGOGYWWYBROWOOBOORYRRWWGGBGOBB  [score=9]
  L2 : BOGGWBGWWBRRWRRBYGYBRYGGOGOYYWYYBYOWYOOROORRBWWRGBWOBG  [score=9]
  B2 : WOGYWBYWWBROWROBYBGBRWGGRGOBYWGYBGOYGRRRORROYYBOYBGOWW  [score=9]
  R  : YOOYWGYWWRRGRRYBWBGBGWGBRGWBYRGYGGOOBRROOROOYWWOBBYWBY  [score=7]
  F2 : YOGYWBWYBYRRRRRRYGOGRGGWRBGWWYGYBGOWBRBOOWOOBWWOGBYOBY  [score=7]
  D  : YOGYWBYWWBRRWRROBYGBRWGGBYGWBWYYOBGGBRROORRGOWWOGBYOOY  [score=7]
  D' : YOGYWBYWWBRRWRRRGOGBRWGGOOYGGBOYYWBWBRROOROBYWWOGBYBYG  [score=7]
  D2 : YOGYWBYWWBRRWRROOYGBRWGGOBYWOGBYGWYBBRROORBYGWWOGBYRGO  [score=7]
  B  : RRGYWBYWWBRWWROBYGGBRWGGRGOBYWGYBBOOGRROORYOYOGWBBWYYO  [score=7]
  B' : OOBYWBYWWBRYWROBYGGBRWGGRGOBYWGYBGRRGRROORWOYOYYWBBWGO  [score=7]
  U  : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  R' : YORYWGYWOBWBYRRGRRGBWWGBRGWBYOGYGGOWBRROOROOYWWOBBYGBY  [score=5]
  R2 : YOWYWBYWWGYBRRWRRBGBOWGGRGWBYGGYBGOWBRROOROOYOWOGBYRBY  [score=5]
  F  : YOGYWBYRRYRRWRRWYGRWGGGBOGRBWBGYBGOWBRBOOYOOWWWOGBYOBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 45 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 45
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U2

Current state:
WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  F' : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F2 : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  L  : WWYWWYROYBRRWRRBYGBWOGGGGGOYYWYYBROWRRYROOBOOGBGGBBOBW  [score=11]
  L' : YWYYWYROYBRRWRRBYGWWOBGGGGOWYWWYBROWOOBOORYRRGBGGBGOBB  [score=11]
  L2 : BWYGWYGOYBRRWRRBYGYWOYGGRGOWYWBYBGOWYOOROORRBGBRGBWOBW  [score=11]
  R  : WWOBWGGOGRRGRRYBWBWWYWGYRGYBYOGYGGOOBRROOROOYWBRBBYWBY  [score=9]
  F  : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  D  : WWYBWYGOYBRRWRROBYWWOWGGBYGWBWYYOBGGBRROORRGOGBRGBYOOY  [score=9]
  D' : WWYBWYGOYBRRWRRRGOWWOWGGOOYGGBOYYWBWBRROOROBYGBRGBYBYG  [score=9]
  D2 : WWYBWYGOYBRRWRROOYWWOWGGOBYWOGBYGWYBBRROORBYGGBRGBYRGO  [score=9]
  R' : WWOBWGGOOBWBYRRGRRWWWWGBRGWBYOGYGGOGBRROOROOYYBRYBYYBY  [score=7]
  R2 : WWWBWBGOWGYBRRWRRBWWOWGGRGGBYYGYYGOYBRROOROOYOBRGBYOBY  [score=7]
  B2 : WOGBWYGOYBROWROBYBWWOWGGRGOBYWGYBYWWGRRRORROYYBOYBGRBG  [score=7]
  U  : YYYWWOWBGWWOWRRBYGBRRWGGRGOBYWGYBGOWGBROOROOYBRRGBYOBY  [score=5]
  U' : GBWOWWYYYGBRWRRBYGBRRWGGRGOBYWGYBGOWWWOOOROOYBRRGBYOBY  [score=5]
  B  : RRGBWYGOYBRWWROBYGWWOWGGRGOBYWGYBBOOYRRWORWOYOGGBBBYYR  [score=5]
  B' : OOBBWYGOYBRWWRWBYYWWOWGGRGOBYWGYBGRRGRROORWOYRYYBBBGGO  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 46 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 46
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: F'

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  U' : BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 47 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 47
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U2

Current state:
BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : GWBWWBWWWBRYYRRBYGRBRGGGGWRYRYYYBOOWROGROOWOOOGYGBYOBB  [score=13]
  L' : YWBYWBOWWBRYYRRBYGBBRYGGYWRGRYWYBWOWOOWOORGOROGGGBGOBR  [score=11]
  L2 : RWBGWBGWWBRYYRRBYGYBRYGGOWRBRYYYBYOWGOOOOORRWOGWGBWOBG  [score=11]
  R  : BWOYWGYWOYRGRRYBYBGBBWGBWWWRRRGYGGORWRROOOOOGWGOBBYYBY  [score=9]
  F' : BWBYWBBYBYRYRRRRYGRGRBGWGWWROGGYBGOWWRWOOWOOYOGOGBYOBY  [score=9]
  D  : BWBYWBYWWBRYYRROBYGBRWGGBYGYBWRYORGGWRROOOWWROGOGBYOOG  [score=9]
  D' : BWBYWBYWWBRYYRRWWRGBRWGGOOGGGROYRWBYWRROOOOBYOGOGBYBYG  [score=9]
  D2 : BWBYWBYWWBRYYRROOGGBRWGGOBYWOGBYGYRRWRROOOBYGOGOGBYWWR  [score=9]
  B2 : WOGYWBYWWBROYROBYWGBRWGGWWRRRYGYBBWBGRRROOYOGYBOYBGOGO  [score=9]
  U  : BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY  [score=7]
  U' : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R' : BWRYWGYWRBYBYRRGRYGBYWGBWWWRROGYGGOOWRROOOOOGWGOBBYBBY  [score=7]
  R2 : BWYYWBYWWGYBRRYYRBGBOWGGWWORRBGYBGOWWRROOOOOGRGOGBYRBY  [score=7]
  F  : BWBYWBGORYRYWRRWYGWWGWGBRGRBYBGYBGOWWRROOROOYOGOGBYOBY  [score=7]
  F2 : BWBYWBYRRGRYORRRYGRWWGGWRBGWWYGYBGOWWRBOOYOOBOGOGBYOBY  [score=7]
  B  : YRGYWBYWWBRWYROBYGGBRWGGWWRRRYGYBWOOBRRWOOBOGOGOBBGYYO  [score=7]
  B' : OOWYWBYWWBRBYRWBYBGBRWGGWWRRRYGYBGRYGRROOOWOGOYYGBBOGO  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 48 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 48
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F' : BBWWWWGYBYBRRRRRYGRGRRGWWWWOOGGYBGOWOGYOOYOOBBRYGBYOBY  [score=9]
  L  : WBWWWWWYYGBRYRRBYGRRRGGGGWRYRYYYBYOWOOGGOOOOOBRBGBWOBB  [score=9]
  B2 : WOGWWWBYYGBOYROBYOWRRWGGWWRRRYGYBWBBGGOROOROGYBOYBGYRB  [score=9]
  U2 : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R  : BBOWWGBYBRRGBRYGYBWRWWGWWWYRRRGYGGOROGOOOOOOGWRYBBYYBY  [score=7]
  F  : BBWWWWGOOBBRYRRYYGWWWWGRRGRBYGGYBGOWOGROOROOYBRYGBYOBY  [score=7]
  F2 : BBWWWWYRRGBRORROYGRWWGGWRRWYYBGYBGOWOGBOOYOOGBRYGBYOBY  [score=7]
  D  : BBWWWWBYYGBRYRROBYWRRWGGBYGYBWRYORGGOGOOOOWWRBRYGBYOOG  [score=7]
  D' : BBWWWWBYYGBRYRRWWRWRRWGGOOGGGROYRWBYOGOOOOOBYBRYGBYBYG  [score=7]
  D2 : BBWWWWBYYGBRYRROOGWRRWGGOBYWOGBYGYRROGOOOOBYGBRYGBYWWR  [score=7]
  L' : YBWYWWYYYGBRYRRBYGBRRWGGBWRWRYWYBWOWOOOOOGGOOBRGGBGOBR  [score=7]
  L2 : RBWGWWGYYGBRYRRBYGYRRYGGYWRBRYWYBBOWGOOOOOOGOBRWGBWOBW  [score=7]
  B  : RRGWWWBYYGBWYROBYGWRRWGGWWRRRYGYBOOOWGOBOOBOGOGBBBRYYY  [score=7]
  B' : OOOWWWBYYGBBYRBBYWWRRWGGWWRRRYGYBGRRGGOOOOWOGYYYRBBBGO  [score=7]
  R' : BBRWWGBYRBYGYRBGRRWRYWGBWWWRROGYGGOBOGOOOOOOGYRYWBYWBY  [score=5]
  R2 : BBYWWBBYWGYBRRYRBGWROWGGWWBRRWGYWGOYOGOOOOOOGRRYGBYRBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 49 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 49
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 50 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 50
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U2

Current state:
BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : GWBWWBWWWBRYYRRBYGRBRGGGGWRYRYYYBOOWROGROOWOOOGYGBYOBB  [score=13]
  L' : YWBYWBOWWBRYYRRBYGBBRYGGYWRGRYWYBWOWOOWOORGOROGGGBGOBR  [score=11]
  L2 : RWBGWBGWWBRYYRRBYGYBRYGGOWRBRYYYBYOWGOOOOORRWOGWGBWOBG  [score=11]
  R  : BWOYWGYWOYRGRRYBYBGBBWGBWWWRRRGYGGORWRROOOOOGWGOBBYYBY  [score=9]
  F' : BWBYWBBYBYRYRRRRYGRGRBGWGWWROGGYBGOWWRWOOWOOYOGOGBYOBY  [score=9]
  D  : BWBYWBYWWBRYYRROBYGBRWGGBYGYBWRYORGGWRROOOWWROGOGBYOOG  [score=9]
  D' : BWBYWBYWWBRYYRRWWRGBRWGGOOGGGROYRWBYWRROOOOBYOGOGBYBYG  [score=9]
  D2 : BWBYWBYWWBRYYRROOGGBRWGGOBYWOGBYGYRRWRROOOBYGOGOGBYWWR  [score=9]
  B2 : WOGYWBYWWBROYROBYWGBRWGGWWRRRYGYBBWBGRRROOYOGYBOYBGOGO  [score=9]
  U  : BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY  [score=7]
  U' : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R' : BWRYWGYWRBYBYRRGRYGBYWGBWWWRROGYGGOOWRROOOOOGWGOBBYBBY  [score=7]
  R2 : BWYYWBYWWGYBRRYYRBGBOWGGWWORRBGYBGOWWRROOOOOGRGOGBYRBY  [score=7]
  F  : BWBYWBGORYRYWRRWYGWWGWGBRGRBYBGYBGOWWRROOROOYOGOGBYOBY  [score=7]
  F2 : BWBYWBYRRGRYORRRYGRWWGGWRBGWWYGYBGOWWRBOOYOOBOGOGBYOBY  [score=7]
  B  : YRGYWBYWWBRWYROBYGGBRWGGWWRRRYGYBWOOBRRWOOBOGOGOBBGYYO  [score=7]
  B' : OOWYWBYWWBRBYRWBYBGBRWGGWWRRRYGYBGRYGRROOOWOGOYYGBBOGO  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 51 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 51
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F' : BBWWWWGYBYBRRRRRYGRGRRGWWWWOOGGYBGOWOGYOOYOOBBRYGBYOBY  [score=9]
  L  : WBWWWWWYYGBRYRRBYGRRRGGGGWRYRYYYBYOWOOGGOOOOOBRBGBWOBB  [score=9]
  B2 : WOGWWWBYYGBOYROBYOWRRWGGWWRRRYGYBWBBGGOROOROGYBOYBGYRB  [score=9]
  U2 : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R  : BBOWWGBYBRRGBRYGYBWRWWGWWWYRRRGYGGOROGOOOOOOGWRYBBYYBY  [score=7]
  F  : BBWWWWGOOBBRYRRYYGWWWWGRRGRBYGGYBGOWOGROOROOYBRYGBYOBY  [score=7]
  F2 : BBWWWWYRRGBRORROYGRWWGGWRRWYYBGYBGOWOGBOOYOOGBRYGBYOBY  [score=7]
  D  : BBWWWWBYYGBRYRROBYWRRWGGBYGYBWRYORGGOGOOOOWWRBRYGBYOOG  [score=7]
  D' : BBWWWWBYYGBRYRRWWRWRRWGGOOGGGROYRWBYOGOOOOOBYBRYGBYBYG  [score=7]
  D2 : BBWWWWBYYGBRYRROOGWRRWGGOBYWOGBYGYRROGOOOOBYGBRYGBYWWR  [score=7]
  L' : YBWYWWYYYGBRYRRBYGBRRWGGBWRWRYWYBWOWOOOOOGGOOBRGGBGOBR  [score=7]
  L2 : RBWGWWGYYGBRYRRBYGYRRYGGYWRBRYWYBBOWGOOOOOOGOBRWGBWOBW  [score=7]
  B  : RRGWWWBYYGBWYROBYGWRRWGGWWRRRYGYBOOOWGOBOOBOGOGBBBRYYY  [score=7]
  B' : OOOWWWBYYGBBYRBBYWWRRWGGWWRRRYGYBGRRGGOOOOWOGYYYRBBBGO  [score=7]
  R' : BBRWWGBYRBYGYRBGRRWRYWGBWWWRROGYGGOBOGOOOOOOGYRYWBYWBY  [score=5]
  R2 : BBYWWBBYWGYBRRYRBGWROWGGWWBRRWGYWGOYOGOOOOOOGRRYGBYRBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 52 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 52
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 53 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 53
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 9
Previous move: U2

Current state:
BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : GWBWWBWWWBRYYRRBYGRBRGGGGWRYRYYYBOOWROGROOWOOOGYGBYOBB  [score=13]
  L' : YWBYWBOWWBRYYRRBYGBBRYGGYWRGRYWYBWOWOOWOORGOROGGGBGOBR  [score=11]
  L2 : RWBGWBGWWBRYYRRBYGYBRYGGOWRBRYYYBYOWGOOOOORRWOGWGBWOBG  [score=11]
  R  : BWOYWGYWOYRGRRYBYBGBBWGBWWWRRRGYGGORWRROOOOOGWGOBBYYBY  [score=9]
  F' : BWBYWBBYBYRYRRRRYGRGRBGWGWWROGGYBGOWWRWOOWOOYOGOGBYOBY  [score=9]
  D  : BWBYWBYWWBRYYRROBYGBRWGGBYGYBWRYORGGWRROOOWWROGOGBYOOG  [score=9]
  D' : BWBYWBYWWBRYYRRWWRGBRWGGOOGGGROYRWBYWRROOOOBYOGOGBYBYG  [score=9]
  D2 : BWBYWBYWWBRYYRROOGGBRWGGOBYWOGBYGYRRWRROOOBYGOGOGBYWWR  [score=9]
  B2 : WOGYWBYWWBROYROBYWGBRWGGWWRRRYGYBBWBGRRROOYOGYBOYBGOGO  [score=9]
  U  : BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY  [score=7]
  U' : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R' : BWRYWGYWRBYBYRRGRYGBYWGBWWWRROGYGGOOWRROOOOOGWGOBBYBBY  [score=7]
  R2 : BWYYWBYWWGYBRRYYRBGBOWGGWWORRBGYBGOWWRROOOOOGRGOGBYRBY  [score=7]
  F  : BWBYWBGORYRYWRRWYGWWGWGBRGRBYBGYBGOWWRROOROOYOGOGBYOBY  [score=7]
  F2 : BWBYWBYRRGRYORRRYGRWWGGWRBGWWYGYBGOWWRBOOYOOBOGOGBYOBY  [score=7]
  B  : YRGYWBYWWBRWYROBYGGBRWGGWWRRRYGYBWOOBRRWOOBOGOGOBBGYYO  [score=7]
  B' : OOWYWBYWWBRBYRWBYBGBRWGGWWRRRYGYBGRYGRROOOWOGOYYGBBOGO  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 54 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 54
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U

Current state:
BBWWWWBYYGBRYRRBYGWRRWGGWWRRRYGYBGOWOGOOOOOOGBRYGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  U  : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  F' : BBWWWWGYBYBRRRRRYGRGRRGWWWWOOGGYBGOWOGYOOYOOBBRYGBYOBY  [score=9]
  L  : WBWWWWWYYGBRYRRBYGRRRGGGGWRYRYYYBYOWOOGGOOOOOBRBGBWOBB  [score=9]
  B2 : WOGWWWBYYGBOYROBYOWRRWGGWWRRRYGYBWBBGGOROOROGYBOYBGYRB  [score=9]
  U2 : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]
  R  : BBOWWGBYBRRGBRYGYBWRWWGWWWYRRRGYGGOROGOOOOOOGWRYBBYYBY  [score=7]
  F  : BBWWWWGOOBBRYRRYYGWWWWGRRGRBYGGYBGOWOGROOROOYBRYGBYOBY  [score=7]
  F2 : BBWWWWYRRGBRORROYGRWWGGWRRWYYBGYBGOWOGBOOYOOGBRYGBYOBY  [score=7]
  D  : BBWWWWBYYGBRYRROBYWRRWGGBYGYBWRYORGGOGOOOOWWRBRYGBYOOG  [score=7]
  D' : BBWWWWBYYGBRYRRWWRWRRWGGOOGGGROYRWBYOGOOOOOBYBRYGBYBYG  [score=7]
  D2 : BBWWWWBYYGBRYRROOGWRRWGGOBYWOGBYGYRROGOOOOBYGBRYGBYWWR  [score=7]
  L' : YBWYWWYYYGBRYRRBYGBRRWGGBWRWRYWYBWOWOOOOOGGOOBRGGBGOBR  [score=7]
  L2 : RBWGWWGYYGBRYRRBYGYRRYGGYWRBRYWYBBOWGOOOOOOGOBRWGBWOBW  [score=7]
  B  : RRGWWWBYYGBWYROBYGWRRWGGWWRRRYGYBOOOWGOBOOBOGOGBBBRYYY  [score=7]
  B' : OOOWWWBYYGBBYRBBYWWRRWGGWWRRRYGYBGRRGGOOOOWOGYYYRBBBGO  [score=7]
  R' : BBRWWGBYRBYGYRBGRRWRYWGBWWWRROGYGGOBOGOOOOOOGYRYWBYWBY  [score=5]
  R2 : BBYWWBBYWGYBRRYRBGWROWGGWWBRRWGYWGOYOGOOOOOOGRRYGBYRBY  [score=5]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Fallback at Step 55, Retry 1

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (ordered by priority):

1.  **CYCLE AVOIDANCE**: If the user prompt explicitly specifies `FORBIDDEN_MOVE: <move_token>`, you MUST NOT select that specific move. If a move chosen by rules 2 or 3 is the `FORBIDDEN_MOVE`, you MUST disregard it and re-evaluate using the same rules, considering the `FORBIDDEN_MOVE` as if it were not available in the lookup table. If `FORBIDDEN_MOVE: None` is specified, no moves are forbidden.

2.  **Phase white_cross PREFERENCE**: (Applies only in `white_cross` phase)
    -   Identify all U-face moves (U, U', U2) in the lookup table.
    -   From these U-face moves, select any that have a score greater than or equal to `(current score - 2)` AND are NOT the `FORBIDDEN_MOVE` (if any).
    -   If multiple such U-face moves exist, pick the one with the highest score. If scores are equal, pick the first one listed in the table.
    -   If no U-face move satisfies this condition (score and not forbidden), proceed to rule 3.

3.  **BEST AVAILABLE MOVE**: Pick the first entry in the lookup table (which is always sorted by highest score) that is NOT the `FORBIDDEN_MOVE` (if any).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

FORBIDDEN_MOVE: {forbidden_move_token_or_None}
(If `FORBIDDEN_MOVE` is specified as a move token, that move MUST NOT be chosen. If `FORBIDDEN_MOVE: None`, all moves are permitted according to other rules.)

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

SELECTION: Follow the MOVE SELECTION RULES from the System Prompt carefully, prioritizing CYCLE AVOIDANCE.
Current `(current score - 2)` threshold for U-face moves is {current_score_minus_2}.

Here's the step-by-step reasoning process:
1.  **Check for U-face moves (U, U', U2) that are NOT `FORBIDDEN_MOVE` and meet the score threshold ({current_score_minus_2}):**
    *   Find all U-face moves in the table.
    *   Filter out any U-face moves that are the `FORBIDDEN_MOVE`.
    *   From the remaining U-face moves, select those with `score >= {current_score_minus_2}`.
    *   If any are found, pick the one with the highest score (or first listed if scores are tied). This is your chosen move.

2.  **If no such U-face move is found, then pick the highest scoring move from the entire table that is NOT `FORBIDDEN_MOVE`:**
    *   Go through the lookup table from top to bottom (highest score first).
    *   The first move you encounter that is NOT the `FORBIDDEN_MOVE` is your chosen move.

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

### Failed Predictions
- Agent cycle_detector: action=N/A, state=WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 55
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent cycle_detector: predicted action=N/A, predicted state=WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY, error=Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move.

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
## Analysis of Failure

The primary failure mode is a **cycle detected by the `cycle_detector` agent**. The `cycle_detector` explicitly states: "Cycle detected: state visited 4 times (limit 3). The agent is stuck in a loop. You MUST choose a completely different move."

The original `MOVE SELECTION RULE (white_cross phase)` is deterministic:
1.  Check U-face moves (U, U', U2) with `score >= (current score - 2)`.
2.  If any exist, pick one (highest score, or first if ties).
3.  Otherwise, pick the FIRST entry in the table.

For the given state:
*   `Current score: 13`. Threshold for U-face moves: `13 - 2 = 11`.
*   U-face moves in table: `U2 (score=9)`, `U (score=7)`. Neither meets the `score >= 11` condition.
*   Therefore, the rule dictates picking the **FIRST entry in the table**: `L` (score=17).

The failure indicates that choosing `L` resulted in a cycle. The existing rules provide no mechanism to avoid a move that leads to a detected cycle. The agents are blindly following the rules into a loop.

**Improvement Strategy:**
The improved prompts must:
1.  Introduce a **Cycle Avoidance** rule that takes precedence over other selection rules.
2.  Allow the system to pass a `FORBIDDEN_MOVE` token to the agent when a cycle is detected, instructing the agent to explicitly avoid that move.
3.  Modify the existing move selection logic to account for forbidden moves, effectively "removing" them from consideration during the evaluation process.
4.  Provide a clear, step-by-step guidance in the user prompt's `SELECTION` block, demonstrating how to apply these new rules.

---

<SYSTEM_PROMPT>
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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (ordered by priority):

1.  **CYCLE AVOIDANCE**: If the user prompt explicitly specifies `FORBIDDEN_MOVE: <move_token>`, you MUST NOT select that specific move. If a move chosen by rules 2 or 3 is the `FORBIDDEN_MOVE`, you MUST disregard it and re-evaluate using the same rules, considering the `FORBIDDEN_MOVE` as if it were not available in the lookup table. If `FORBIDDEN_MOVE: None` is specified, no moves are forbidden.

2.  **Phase white_cross PREFERENCE**: (Applies only in `white_cross` phase)
    -   Identify all U-face moves (U, U', U2) in the lookup table.
    -   From these U-face moves, select any that have a score greater than or equal to `(current score - 2)` AND are NOT the `FORBIDDEN_MOVE` (if any).
    -   If multiple such U-face moves exist, pick the one with the highest score. If scores are equal, pick the first one listed in the table.
    -   If no U-face move satisfies this condition (score and not forbidden), proceed to rule 3.

3.  **BEST AVAILABLE MOVE**: Pick the first entry in the lookup table (which is always sorted by highest score) that is NOT the `FORBIDDEN_MOVE` (if any).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: {previous_move}

Current state:
{current_state}

FORBIDDEN_MOVE: {forbidden_move_token_or_None}
(If `FORBIDDEN_MOVE` is specified as a move token, that move MUST NOT be chosen. If `FORBIDDEN_MOVE: None`, all moves are permitted according to other rules.)

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

SELECTION: Follow the MOVE SELECTION RULES from the System Prompt carefully, prioritizing CYCLE AVOIDANCE.
Current `(current score - 2)` threshold for U-face moves is {current_score_minus_2}.

Here's the step-by-step reasoning process:
1.  **Check for U-face moves (U, U', U2) that are NOT `FORBIDDEN_MOVE` and meet the score threshold ({current_score_minus_2}):**
    *   Find all U-face moves in the table.
    *   Filter out any U-face moves that are the `FORBIDDEN_MOVE`.
    *   From the remaining U-face moves, select those with `score >= {current_score_minus_2}`.
    *   If any are found, pick the one with the highest score (or first listed if scores are tied). This is your chosen move.

2.  **If no such U-face move is found, then pick the highest scoring move from the entire table that is NOT `FORBIDDEN_MOVE`:**
    *   Go through the lookup table from top to bottom (highest score first).
    *   The first move you encounter that is NOT the `FORBIDDEN_MOVE` is your chosen move.

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>
</USER_PROMPT>

---

## Actual LLM Prompt at Step 55 (fallback)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULES (ordered by priority):

1.  **CYCLE AVOIDANCE**: If the user prompt explicitly specifies `FORBIDDEN_MOVE: <move_token>`, you MUST NOT select that specific move. If a move chosen by rules 2 or 3 is the `FORBIDDEN_MOVE`, you MUST disregard it and re-evaluate using the same rules, considering the `FORBIDDEN_MOVE` as if it were not available in the lookup table. If `FORBIDDEN_MOVE: None` is specified, no moves are forbidden.

2.  **Phase white_cross PREFERENCE**: (Applies only in `white_cross` phase)
    -   Identify all U-face moves (U, U', U2) in the lookup table.
    -   From these U-face moves, select any that have a score greater than or equal to `(current score - 2)` AND are NOT the `FORBIDDEN_MOVE` (if any).
    -   If multiple such U-face moves exist, pick the one with the highest score. If scores are equal, pick the first one listed in the table.
    -   If no U-face move satisfies this condition (score and not forbidden), proceed to rule 3.

3.  **BEST AVAILABLE MOVE**: Pick the first entry in the lookup table (which is always sorted by highest score) that is NOT the `FORBIDDEN_MOVE` (if any).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

FORBIDDEN_MOVE: {forbidden_move_token_or_None}
(If `FORBIDDEN_MOVE` is specified as a move token, that move MUST NOT be chosen. If `FORBIDDEN_MOVE: None`, all moves are permitted according to other rules.)

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
{move_lookup_table}

SELECTION: Follow the MOVE SELECTION RULES from the System Prompt carefully, prioritizing CYCLE AVOIDANCE.
Current `(current score - 2)` threshold for U-face moves is {current_score_minus_2}.

Here's the step-by-step reasoning process:
1.  **Check for U-face moves (U, U', U2) that are NOT `FORBIDDEN_MOVE` and meet the score threshold ({current_score_minus_2}):**
    *   Find all U-face moves in the table.
    *   Filter out any U-face moves that are the `FORBIDDEN_MOVE`.
    *   From the remaining U-face moves, select those with `score >= {current_score_minus_2}`.
    *   If any are found, pick the one with the highest score (or first listed if scores are tied). This is your chosen move.

2.  **If no such U-face move is found, then pick the highest scoring move from the entire table that is NOT `FORBIDDEN_MOVE`:**
    *   Go through the lookup table from top to bottom (highest score first).
    *   The first move you encounter that is NOT the `FORBIDDEN_MOVE` is your chosen move.

Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Fallback at Step 55, Retry 2

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 55
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

### Failed Predictions
- Agent 55:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:3: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 55:9: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


## Original User Prompt
Step: 55
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

## Failed Predictions
  - Agent 55:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:3: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 55:9: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.

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

## Actual LLM Prompt at Step 55 (fallback)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 55
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

Step: 55
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 13
Previous move: U

Current state:
WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  L  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  L' : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  L2 : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  R  : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]
  D  : WWYBWYBWBWRRYRROBYOGOWGGBYGYBWRYORGGBRYOOOWWRGBRGBYOOG  [score=13]
  D' : WWYBWYBWBWRRYRRWWROGOWGGOOGGGROYRWBYBRYOOOOBYGBRGBYBYG  [score=13]
  D2 : WWYBWYBWBWRRYRROOGOGOWGGOBYWOGBYGYRRBRYOOOBYGGBRGBYWWR  [score=13]
  R' : WWOBWGBWRBYWYRRGRROGYWGBWWWRROGYGGOGBRYOOOOOGBBRYBYYBY  [score=11]
  R2 : WWYBWBBWWGYBRRYRRWOGOWGGWWGRRYGYYGOBBRYOOOOOGRBRGBYOBY  [score=11]
  F' : WWYBWYWYBYRRRRRRYGOGRGGWOWWYOGGYBGOWBRBOOWOOBGBRGBYOBY  [score=11]
  B2 : WOGBWYBWBWROYROBYBOGOWGGWWRRRYGYBYWWGRYROOROGYBOYBGRBG  [score=11]
  U2 : BWBYWBYWWBRYYRRBYGGBRWGGWWRRRYGYBGOWWRROOOOOGOGOGBYOBY  [score=9]
  F  : WWYBWYGOYBRRWRRBYGWWOWGGRGOBYWGYBGOWBRROOROOYGBRGBYOBY  [score=9]
  F2 : WWYBWYYRRGRRORRYYGRWWGGWOGOBWBGYBGOWBRBOOYOOWGBRGBYOBY  [score=9]
  B  : RRGBWYBWBWRWYROBYGOGOWGGWWRRRYGYBBOOYRYWOOWOGOGGBBBYYR  [score=9]
  B' : OOBBWYBWBWRWYRWBYYOGOWGGWWRRRYGYBGRRGRYOOOWOGRYYBBBGGO  [score=9]
  U  : YYBWWWWBBOGOYRRBYGBRYWGGWWRRRYGYBGOWGBROOOOOGWRRGBYOBY  [score=7]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 56 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 56
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: L

Current state:
OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW  [score=17]
  D  : OWYWWYWWBWRRYRROBWRGOGGGBYGYBWRYOYYRYOGROOGWRGBBGBBBOO  [score=17]
  D' : OWYWWYWWBWRRYRRGWRRGOGGGBOORYYOYRWBYYOGROOOBWGBBGBBBYG  [score=17]
  D2 : OWYWWYWWBWRRYRRBOORGOGGGOBWWORBYYYRYYOGROOBYGGBBGBBGWR  [score=17]
  R' : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  R2 : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  F  : OWYWWYOOGWRRWRRBYGGGRWGGRGOBYWYYBROWYOYRORBOYGBBGBBOBW  [score=15]
  F' : OWYWWYWYBYRRRRRYYGOGRGGWRGGGOOYYBROWYOBROWBOWGBBGBBOBW  [score=15]
  L  : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  L2 : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  B' : BRYWWYWWBWROYRWBYYRGOGGGGWRYRYYYBGRRROGOOOWOOBBWBBBGGO  [score=15]
  B2 : WORWWYWWBWRBYRRBYYRGOGGGGWRYRYYYBYWOGOGROOROOWBOBBGBBG  [score=15]
  F2 : OWYWWYYRYORRORRGYGRWGGGGOGRBWWYYBROWYOBROYBOWGBBGBBOBW  [score=13]
  B  : RRGWWYWWBWRWYROBYRRGOGGGGWRYRYYYBYRBYOGWOOOOOOGGBBBWBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 57 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 57
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO  [score=17]
  D' : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  D2 : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  R  : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  R2 : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  F  : OWOWWGOOGWRGWRYGYBGGRWGGBYYWRRYYGRORYOYRORBOOWBBBBBYBW  [score=15]
  L  : RWOGWGGWGRRGRRYWYBYGYYGYRWBWROBYGBORGOOOOOYRBWBWBBWYBO  [score=15]
  L2 : YWOYWGRWGRRGRRYWYBWGYBGYBWBOROWYGWOROOBOORGOYWBGBBGYBR  [score=15]
  B  : GYBWWGWWGRRRRROWYRRGYGGYGWBYROYYGYRBOOGWOOOOOYBWBBBWBB  [score=15]
  B' : BRYWWGWWGRRORRWWYORGYGGYGWBYROYYGBYGROGOOOROOBBWBBBWBY  [score=15]
  B2 : RORWWGWWGRRBRRRWYYRGYGGYGWBYROYYGOWOBOGYOOGOOWBYBBBBBW  [score=15]
  F' : OWOWWGRRWORGRRYYYBYYBGGWRGGGOOYYGRORYOGROWBOWWBBBBBYBW  [score=13]
  F2 : OWOWWGORYORGORYGYBBWGYGGYGRGWWYYGRORYOWRORBORWBBBBBYBW  [score=13]
  L' : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 58 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 58
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO  [score=17]
  D  : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  D2 : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  R  : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  R2 : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  F  : OWOWWGBOGWRGWRYGBWWGRYGGBYYYRRRYOYYRYOOROGGWRWBBBBBBOO  [score=15]
  L  : RWOGWGWWGRRGRRYYBWOGYRGYYYBOGRBYOBYRGOBOOWYRGWBWBBWBOO  [score=15]
  B  : GYWWWGWWGRRRRRYYBYRGYGGYWYBOGRRYOYRGOOGWOOOWBBBWOBBOBB  [score=15]
  B' : GRYWWGWWGRRORRWYBORGYGGYWYBOGRRYOWYGYOGYOORWBBBOBBOWBB  [score=15]
  F' : OWOWWGRRYRRGGRYOBWYYBGGYRGWGOBRYOYYRYOGROWGWWWBBBBBBOO  [score=13]
  F2 : OWOWWGRGOBRGORYGBWBYWYGGYGRGWWRYOYYRYOYRORGWRWBBBBBBOO  [score=13]
  L' : OWOBWGBWGRRGRRYYBWOGYWGYWYBRGRGYOWYRGRYWOOBOGWBYBBRBOO  [score=13]
  L2 : OWORWGYWGRRGRRYYBWOGYBGYBYBOGRWYOWYRBWGOORGOYWBWBBGBOR  [score=13]
  B2 : RYYWWGWWGRRGRRRYBYRGYGGYWYBOGRRYOOWOWOGYOOGWBOOBBBBBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 59 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 59
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB  [score=17]
  D' : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  D2 : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  R' : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  R2 : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  F  : OWYWWYBOGWRRWRRBYGWGRYGGRORWBYRYBYYWYOOROGGWBGBBGBBOOO  [score=15]
  L  : RWYGWYWWBYRRBRRWYGOGRRGOYYROGBBYBBYWGOBOOWYRGGBWGBWOOO  [score=15]
  B' : GRYWWYWWBYROBRWWYYRGRGGOWYROGBRYBGRRYOGYOOWWBBBOBBOGGO  [score=15]
  F' : OWYWWYYBWBRRGRROYGRORGGYRGWGOBRYBYYWYOBROWGWWGBBGBBOOO  [score=13]
  F2 : OWYWWYBGOBRRORRGYGRYWOGGRGRBWWRYBYYWYOWROBGWYGBBGBBOOO  [score=13]
  L' : OWYBWYBWBYRRBRRWYGOGRWGOWYRRGBGYBWYWGRYWOOBOGGBYGBROOO  [score=13]
  L2 : OWYRWYYWBYRRBRRWYGOGRBGOBYROGBWYBWYWBWGOORGOYGBWGBGOOR  [score=13]
  B  : RRGWWYWWBYRWBRYWYYRGRGGOWYROGBRYBYRGYOGWOOOWBOGGOBBOBB  [score=13]
  B2 : WYYWWYWWBYRGBRRWYYRGRGGOWYROGBRYBYWOGOGROORWBOOOBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 60 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 60
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWGWWGWWGRRORROYBORGYGGYWYBBBRGYOORGYOGROOWYRYBBYBBWWB  [score=17]
  D  : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  D2 : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  R' : OWRWWOWWGOBYORRORRRGWGGYWYYBBGGYGORGYOGROOWYRBBBYBBYWB  [score=15]
  R2 : OWWWWYWWYOOORRBRRYRGGGGGWYGBBYGYYORBYOGROOWYRGBBOBBRWB  [score=15]
  F  : OWYWWYROGWRRWRRBOOWGRYGGGOROBYGYYORYYOBROBWYWGBBGBBGWB  [score=15]
  L  : RWYGWYWWBYRRBRROOOBGRGGOOYGBBWBYYBRYGOROOYYRWGBWGBWGWO  [score=15]
  B' : WRYWWYWWBYROBRWOOYRGRGGOWYGBBWGYYORROOGROOYYRBBBBBWGGG  [score=15]
  F' : OWYWWYYBOWRRBRRBOOROGGGYRGWGORGYYORYYOBROWWYWGBBGBBGWB  [score=13]
  F2 : OWYWWYWBBRRRORRGOOGYWOGGRGRBWWGYYORYYOOROBWYYGBBGBBGWB  [score=13]
  L' : BWYBWYBWBYRRBRROOOOGRWGOWYGRBWGYYWRYWRYYOOROGGBOGBGGWB  [score=13]
  L2 : BWYGWYOWBYRRBRROOOBGRBGOBYGOBWWYYWRYRYWOORGOYGBWGBGGWR  [score=13]
  B  : RROWWYWWBYRYBRROOORGRGGOWYGBBWGYYYRWYOGWOOOYRGGGWBBBBB  [score=13]
  B2 : YROWWYWWBYRWBRROOYRGRGGOWYGBBWGYYYWOOOGROORYRBWGBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 61 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 61
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWGWWGWWGRRORROYBORGYGGYWYBBBRGYOORGYOGROOWYRYBBYBBWWB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWGWWGWWGRRORROWWBRGYGGYYBOROGBYRBGOYOGROOWYBYBBYBBWYR  [score=17]
  D' : OWGWWGWWGRRORROWYBRGYGGYWYROGBRYBGORYOGROOWWBYBBYBBYBO  [score=17]
  D2 : OWGWWGWWGRRORROWYRRGYGGYWWBGROOYGRBBYOGROOYBOYBBYBBWYB  [score=17]
  R  : OWWWWYWWYOOORRBRRYRGGGGGWYGBBYGYYORBYOGROOWYRGBBOBBRWB  [score=15]
  R2 : OWRWWOWWGOBYORRORRRGWGGYWYYBBGGYGORGYOGROOWYRBBBYBBYWB  [score=15]
  F  : OWGWWGROGWROWROGBOWGRYGGBYYYRRGYOORGYOBROBWYRYBBYBBWWB  [score=15]
  L  : RWGGWGWWGRRORROYBOBGYGGYOYBBBRBYOBRGGOROOYYRWYBWYBWWWO  [score=15]
  B' : WRYWWGWWGRRORRWYBGRGYGGYWYBBBRGYOOOOOOGROOGYRBBBBBWYYW  [score=15]
  F' : OWGWWGRRYRROBROBBOYYBGGYRGWGORGYOORGYOGROWWYWYBBYBBWWB  [score=13]
  F2 : OWGWWGRBBRROOROGBOBYWYGGYGRGWWGYOORGYOYRORWYRYBBYBBWWB  [score=13]
  L' : BWGBWGBWGRRORROYBOOGYWGYWYBRBRGYOWRGWRYYOOROGYBOYBGWWB  [score=13]
  L2 : BWGGWGOWGRRORROYBOBGYBGYBYBOBRWYOWRGRYWOORGOYYBWYBGWWR  [score=13]
  B  : OOOWWGWWGRRGRRRYBORGYGGYWYBBBRGYOYRWGOGWOOOYRWYYWBBBBB  [score=13]
  B2 : GROWWGWWGRRWRRRYBYRGYGGYWYBBBRGYOGWOOOGOOOOYRBWWBBYBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 62 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 62
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWGWWGWWGRRORROWWBRGYGGYYBOROGBYRBGOYOGROOWYBYBBYBBWYR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWOWRRWRRBOORGGGGRYBOROWBYYBGYYOGROOWYBGBBGBBGYR  [score=17]
  D  : OWGWWGWWGRRORROWYRRGYGGYWWBGROOYGRBBYOGROOYBOYBBYBBWYB  [score=17]
  D2 : OWGWWGWWGRRORROWYBRGYGGYWYROGBRYBGORYOGROOWWBYBBYBBYBO  [score=17]
  R  : OWWWWYWWYOOBRRWRRWRGGGGGYBGROYBYYBGOYOGROOWYBOBBRBBGYR  [score=15]
  R2 : OWGWWRWWOBWWORRORRRGWGGYYBYROGBYGBGGYOGROOWYBOBBYBBYYR  [score=15]
  F  : OWGWWGBOGWROWROGWBYGRBGGOYYWRRBYRBGOYORROOWYGYBBYBBWYR  [score=15]
  L  : RWGGWGYWGRRORROWWBRGYBGYBBOROGBYRBGOGOBOOYYRWYBWYBWWYO  [score=15]
  B' : WRYWWGWWGRRORRWWWGRGYGGYYBOROGBYRBOOBOGGOOOYBBBRBBYYYW  [score=15]
  F' : OWGWWGRRWGROORORWBYYOGGBRGYGOBBYRBGOYOGROWWYWYBBYBBWYR  [score=13]
  F2 : OWGWWGGORBROOROGWBOBYYGGYGRGWWBYRBGOYOWRORWYRYBBYBBWYR  [score=13]
  L' : RWGBWGBWGRRORROWWBOGYWGYWBOROGGYRYGOWRYYOOBOGYBBYBBWYR  [score=13]
  L2 : RWGBWGBWGRRORROWWBRGYBGYBBOOOGWYRWGOBYWOORGOYYBYYBGWYR  [score=13]
  B  : OOBWWGWWGRRORRGWWBRGYGGYYBOROGBYRYRWGOGWOOOYBWYYYBBRBB  [score=13]
  B2 : OGBWWGWWGRRWRRRWWYRGYGGYYBOROGBYRGWOBOGOOOOYBRYWBBYBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 63 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 63
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWOWRRWRRBOORGGGGRYBOROWBYYBGYYOGROOWYBGBBGBBGYR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWOWRRWRRGYRRGGGGRBOOWYYOYGRBBYOGROOYBOGBBGBBWYB  [score=17]
  D' : OWYWWYWWOWRRWRRYBORGGGGRWYBBBRGYOYYWYOGROOGYRGBBGBBBOO  [score=17]
  D2 : OWYWWYWWOWRRWRRWYBRGGGGRGYRYGBYYBWORYOGROOBOOGBBGBBYBO  [score=17]
  R' : OWGWWRWWOBWWORRORRRGWGGYYBYROGBYGBGGYOGROOWYBOBBYBBYYR  [score=15]
  R2 : OWWWWYWWYOOBRRWRRWRGGGGGYBGROYBYYBGOYOGROOWYBOBBRBBGYR  [score=15]
  F  : OWYWWYBOGWRRWRROOOYGRBGGORGBWWBYYBGYYORROOWYWGBBGBBGYR  [score=15]
  F' : OWYWWYWWBWRRORRROOGROGGBRGYGOBBYYBGYYOOROWWYWGBBGBBGYR  [score=15]
  L  : RWYGWYYWOWRRWRRBOORGGBGRBBOROWBYYBGYGOBOOYYRWGBWGBWGYO  [score=15]
  B' : WRYWWYWWOWROWRWBOYRGGGGRYBOROWBYYORRBOGGOOYYBBBRBBYGGG  [score=15]
  F2 : OWYWWYWORBRRORRGOOOBYRGGGGROWWBYYBGYYOBROWWYWGBBGBBGYR  [score=13]
  L' : RWYBWYBWOWRRWRRBOOOGGWGRWBOROWGYYYGYWRYYOOBOGGBBGBBGYR  [score=13]
  L2 : RWYBWYBWOWRRWRRBOORGGBGRBBOOOWWYYWGYBYWOORGOYGBYGBGGYR  [score=13]
  B  : RROWWYWWOWRYWRGBOBRGGGGRYBOROWBYYYRWYOGWOOOYBGGGYBBRBB  [score=13]
  B2 : YGBWWYWWOWRWWRRBOYRGGGGRYBOROWBYYYWOOOGROORYBRYGBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 64 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 64
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWOWRRWRRGYRRGGGGRBOOWYYOYGRBBYOGROOYBOGBBGBBWYB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWWWWGWWGRRRRRYWWGRGYGGYBOOWYGOYRRBOYOGROOYBOBBBGBBYYB  [score=17]
  D  : OWYWWYWWOWRRWRRWYBRGGGGRGYRYGBYYBWORYOGROOBOOGBBGBBYBO  [score=17]
  D2 : OWYWWYWWOWRRWRRYBORGGGGRWYBBBRGYOYYWYOGROOGYRGBBGBBBOO  [score=17]
  R' : OWGWWRWWOGWWYRRRRRRGYGGGBOBWYWOYGRBGYOGROOYBOOBBYBBYYB  [score=15]
  R2 : OWYWWGWWBRYGRRWRRWRGWGGGBOGWYYOYYRBOYOGROOYBOOBBRBBGYB  [score=15]
  F  : OWYWWYOOGWRRWRROYRBGROGGORGGWWOYGRBBYOWROYYBYGBBGBBWYB  [score=15]
  F' : OWYWWYWWGYRRYRRWYRGROGGORGBGOOOYGRBBYOOROWYBWGBBGBBWYB  [score=15]
  L  : RWYGWYBWOWRRWRRGYRWGGOGRROOBYYBYGBBBGOOOOBYRYGBWGBWWYO  [score=15]
  B' : YRYWWYWWOWROWRWGYYRGGGGRBOOWYYOYGRRRROGBOOBBOBBBBBYGGW  [score=15]
  F2 : OWYWWYYYWORRORRGYROOBRGGGGROWWOYGRBBYOGROWYBWGBBGBBWYB  [score=13]
  L' : BWYBWYBWOWRRWRRGYROGGWGRWOORYYGYGBBBYRYBOOOOGGBRGBOWYW  [score=13]
  L2 : WWYOWYRWOWRRWRRGYRBGGBGRBOOOYYWYGWBBOBYOORGOYGBBGBGWYR  [score=13]
  B  : RRRWWYWWOWRBWRBGYRRGGGGRBOOWYYOYGYRYYOGWOOOBOWGGYBBBBB  [score=13]
  B2 : BBRWWYWWOWRYWRRGYYRGGGGRBOOWYYOYGYWOROGROORBOBYWBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 65 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 65
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWWWWGWWGRRRRRYWWGRGYGGYBOOWYGOYRRBOYOGROOYBOBBBGBBYYB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWWWWGWWGRRRRRYYYBRGYGGYWWGGROYYBWORYOGROOBOOBBBGBBYBO  [score=17]
  D' : OWWWWGWWGRRRRRYBOORGYGGYYBOROWBYYORGYOGROOYYBBBBGBBWWG  [score=17]
  D2 : OWWWWGWWGRRRRRYYBORGYGGYYYBOBRRYOGYWYOGROOWWGBBBGBBBOO  [score=17]
  R  : OWYWWGWWBRYGRRWRRWRGWGGGBOGWYYOYYRBOYOGROOYBOOBBRBBGYB  [score=15]
  R2 : OWGWWRWWOGWWYRRRRRRGYGGGBOBWYWOYGRBGYOGROOYBOOBBYBBYYB  [score=15]
  F  : OWWWWGOOGWRRWRYGWGBGROGGOYYWRROYRRBOYOWROYYBGBBBGBBYYB  [score=15]
  L  : RWWGWGBWGRRRRRYWWGWGYOGYROOBYGBYRBBOGOOOOBYRYBBWGBWYYO  [score=15]
  B' : YRYWWGWWGRRORRWWWWRGYGGYBOOWYGOYRGYRROGBOOOBOBBBBBYBGY  [score=15]
  F' : OWWWWGRRWGRRYRYWWGYYOGGORGBGOOOYRRBOYOGROWYBWBBBGBBYYB  [score=13]
  F2 : OWWWWGGYWORRORYGWGOOBYGGYGRGWWOYRRBOYOWRORYBRBBBGBBYYB  [score=13]
  L' : BWWBWGBWGRRRRRYWWGOGYWGYWOORYGGYRBBOYRYBOOOOGBBRGBOYYW  [score=13]
  L2 : WWWOWGRWGRRRRRYWWGBGYBGYBOOOYGWYRWBOOBYOORGOYBBBGBGYYR  [score=13]
  B  : RYGWWGWWGRRORRBWWRRGYGGYBOOWYGOYRYRYWOGWOOOBOYGBYBBBBB  [score=13]
  B2 : OBRWWGWWGRRYRRRWWYRGYGGYBOOWYGOYRWWOGOGYOORBOBYYBBGBBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 66 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 66
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWWWWGWWGRRRRRYYYBRGYGGYWWGGROYYBWORYOGROOBOOBBBGBBYBO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWGYRRYRRBYRRGOGGBWWRGRYYYGWOBYOGROOBOOGBBGBBWBO  [score=17]
  D  : OWWWWGWWGRRRRRYYBORGYGGYYYBOBRRYOGYWYOGROOWWGBBBGBBBOO  [score=17]
  D2 : OWWWWGWWGRRRRRYBOORGYGGYYBOROWBYYORGYOGROOYYBBBBGBBWWG  [score=17]
  R  : OWYWWGWWBRYBRRYRRYRGWGGGWWGGRYYYYWOGYOGROOBOORBBBBBOBO  [score=15]
  R2 : OWOWWBWWRBYYYRRRRRRGYGGGWWBGRWYYGWOGYOGROOBOOGBBYBBYBO  [score=15]
  F  : OWWWWGOOGWRRWRYGYBWGRWGGGYYYRRYYBWORYOGRORBOOBBBGBBYBO  [score=15]
  L  : RWWGWGWWGRRRRRYYYBGGYYGYWWGOROBYBBORGOOOOOYRBBBWGBWYBO  [score=15]
  L2 : GWWYWGWWGRRRRRYYYBOGYBGYBWGOROWYBWOROOBOORGOYBBWGBGYBR  [score=15]
  B' : BRYWWGWWGRRORRWYYWRGYGGYWWGGROYYBBYRWOGOOOROOBBOBBBBGY  [score=15]
  B2 : ROWWWGWWGRRBRRRYYYRGYGGYWWGGROYYBWWOBOGYOOROOOBYBBGBBB  [score=15]
  F' : OWWWWGRRYORRRRYGYBYYGGGWRGWGOOYYBWORYOGROWBOWBBBGBBYBO  [score=13]
  F2 : OWWWWGORGORRORYGYBGWWYGGYGRGWWYYBWORYOYRORBORBBBGBBYBO  [score=13]
  L' : OWWBWGBWGRRRRRYYYBOGYWGYWWGRROGYBWORBRYOOOOOGBBWGBYYBG  [score=13]
  B  : RYBWWGWWGRRRRROYYWRGYGGYWWGGROYYBYRBWOGWOOOOOYGBBBBOBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 67 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 67
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWGYRRYRRBYRRGOGGBWWRGRYYYGWOBYOGROOBOOGBBGBBWBO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWGYRRYRRWBORGOGGBBYRYGBRYOGYWYOGROOWWRGBBGBBBOO  [score=17]
  D' : OWYWWYWWGYRRYRRWWRRGOGGBBOOWYGOYRBGYYOGROOWBOGBBGBBBYR  [score=17]
  D2 : OWYWWYWWGYRRYRRBOORGOGGBWBOBOWGYYYRGYOGROOBYRGBBGBBWWR  [score=17]
  R' : OWOWWBWWRBYYYRRRRRRGYGGGWWBGRWYYGWOGYOGROOBOOGBBYBBYBO  [score=15]
  R2 : OWYWWGWWBRYBRRYRRYRGWGGGWWGGRYYYYWOGYOGROOBOORBBBBBOBO  [score=15]
  F  : OWYWWYOOGWRRWRRGYRWGRWGGRBOBYYYYGWOBYOGRORBOYGBBGBBWBO  [score=15]
  L  : RWYGWYWWGYRRYRRBYRGGOYGBWWRORYBYGBOBGOOOOOYRBGBWGBWWBO  [score=15]
  L2 : GWYYWYWWGYRRYRRBYROGOBGBBWRORYWYGWOBOOBOORGOYGBWGBGWBR  [score=15]
  B' : BRYWWYWWGYROYRWBYYRGOGGBWWRGRYYYGRRRWOGOOOBOOBBOBBBGGW  [score=15]
  B2 : BOWWWYWWGYRBYRRBYYRGOGGBWWRGRYYYGYWOROGROOROOOBWBBGBBG  [score=15]
  F' : OWYWWYYYBYRRRRRGYROBRGGWRGWGOOYYGWOBYOGROWBOWGBBGBBWBO  [score=13]
  F2 : OWYWWYYRGORRORRGYRRWWBGGOGRGWWYYGWOBYOBROYBOYGBBGBBWBO  [score=13]
  L' : OWYBWYBWGYRRYRRBYROGOWGBWWRRRYGYGWOBBRYOOOOOGGBWGBYWBG  [score=13]
  B  : RRRWWYWWGYRBYROBYWRGOGGBWWRGRYYYGYRBYOGWOOOOOWGGBBBOBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 68 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 68
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWGYRRYRRWBORGOGGBBYRYGBRYOGYWYOGROOWWRGBBGBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWBWWGWWGRRORRBYYWRGYGGYBYGYGORYBGYRYOGROOWWRWBBOBBBOO  [score=17]
  D  : OWYWWYWWGYRRYRRBOORGOGGBWBOBOWGYYYRGYOGROOBYRGBBGBBWWR  [score=17]
  D2 : OWYWWYWWGYRRYRRWWRRGOGGBBOOWYGOYRBGYYOGROOWBOGBBGBBBYR  [score=17]
  R' : OWOWWBWWRWYYBRRORRRGBGGOBYWYGBRYGGYGYOGROOWWRGBBYBBYOO  [score=15]
  R2 : OWBWWOWWWOBWRRYRRYRGBGGGBYGYGYRYYGYGYOGROOWWRRBBBBBOOO  [score=15]
  F  : OWYWWYROGWRRWRRGBOBGRYGGRBOWYYRYOGYWYOYROGWWBGBBGBBBOO  [score=15]
  L  : RWYGWYBWGYRRYRRWBOYGORGBGYROGBBYOBYWGOROOWYRWGBWGBWBOO  [score=15]
  B' : WRYWWYWWGYROYRWWBYRGOGGBBYRYGBRYOORRGOGYOOWWRBBOBBOGGB  [score=15]
  F' : OWYWWYYYWBRRGRRYBOOBRGGYRGBGORRYOGYWYOGROWWWWGBBGBBBOO  [score=13]
  F2 : OWYWWYBGYRRRORRGBORYBBGGOGRGWWRYOGYWYOWROYWWYGBBGBBBOO  [score=13]
  L' : OWYBWYBWGYRRYRRWBOOGOWGBWYRRGBGYOBYWWRYWOOROGGBGGBRBOY  [score=13]
  L2 : YWYRWYGWGYRRYRRWBOOGOBGBBYROGBWYOWYWRWWOORGOYGBBGBGBOR  [score=13]
  B  : RROWWYWWGYRWYRYWBGRGOGGBBYRYGBRYOYRWYOGWOOOWRBGGOBBOBB  [score=13]
  B2 : WYGWWYWWGYRWYRRWBYRGOGGBBYRYGBRYOYWOOOGROORWROOBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 69 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 69
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWBWWGWWGRRORRBYYWRGYGGYBYGYGORYBGYRYOGROOWWRWBBOBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWBWWGWWGRRORRBBOORGYGGYYYWOBRGYYYRGYOGROOBYGWBBOBBWWR  [score=17]
  D' : OWBWWGWWGRRORRBBYGRGYGGYWWRGRYYYGRBOYOGROOBOOWBBOBBYYW  [score=17]
  D2 : OWBWWGWWGRRORRBWWRRGYGGYBOORYGBYROGYYOGROOYYWWBBOBBBYG  [score=17]
  R  : OWBWWOWWWOBWRRYRRYRGBGGGBYGYGYRYYGYGYOGROOWWRRBBBBBOOO  [score=15]
  R2 : OWOWWBWWRWYYBRRORRRGBGGOBYWYGBRYGGYGYOGROOWWRGBBYBBYOO  [score=15]
  F  : OWBWWGROGWROWRBGYWBGRYGGGYYYRRRYBGYRYOYROGWWOWBBOBBBOO  [score=15]
  L  : RWBGWGBWGRRORRBYYWYGYRGYGYGOGOBYBBYRGOROOWYRWWBWOBWBOO  [score=15]
  B' : WRYWWGWWGRRORRWYYBRGYGGYBYGYGORYBWBOGOGYOORWRBBOBBOWOB  [score=15]
  F' : OWBWWGRRYOROGRBYYWYYGGGYRGBGORRYBGYRYOGROWWWWWBBOBBBOO  [score=13]
  F2 : OWBWWGOGYRROORBGYWGYBYGGYGRGWWRYBGYRYOYRORWWRWBBOBBBOO  [score=13]
  L' : OWBBWGBWGRRORRBYYWOGYWGYWYGRGOGYBBYRWRYWOOROGWBGOBRBOY  [score=13]
  L2 : YWBRWGGWGRRORRBYYWOGYBGYBYGOGOWYBWYRRWWOORGOYWBBOBGBOR  [score=13]
  B  : OBWWWGWWGRRRRRYYYGRGYGGYBYGYGORYBYRWBOGWOOOWRBOWOBBOBB  [score=13]
  B2 : RYGWWGWWGRRWRRRYYYRGYGGYBYGYGORYBBWOWOGBOOOWROOBBBOBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 70 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 70
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWBWWGWWGRRORRBBOORGYGGYYYWOBRGYYYRGYOGROOBYGWBBOBBWWR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWWBRRORROBORGRGGYYYGOBWGYOYRWYOGROOBYGGBBGBBBWR  [score=17]
  D  : OWBWWGWWGRRORRBWWRRGYGGYBOORYGBYROGYYOGROOYYWWBBOBBBYG  [score=17]
  D2 : OWBWWGWWGRRORRBBYGRGYGGYWWRGRYYYGRBOYOGROOBOOWBBOBBYYW  [score=17]
  R  : OWWWWOWWWOBORRORRBRGBGGGYYGOBYGYYYRWYOGROOBYGGBBYBBRWR  [score=15]
  R2 : OWRWWYWWGOOBBRRORRRGWGGOYYWOBBGYGYRGYOGROOBYGWBBYBBYWR  [score=15]
  F  : OWBWWGGOGWROWRBGOOYGRYGGWYYBRRGYYYRGYOOROBBYRWBBOBBWWR  [score=15]
  L  : RWBGWGYWGRRORRBBOOOGYGGYYYWRBRBYYBRGGOGOOYYRBWBWOBWWWO  [score=15]
  B' : BRYWWGWWGRRORRWBOBRGYGGYYYWOBRGYYOBOYOGROOGYGBBRBBWWOW  [score=15]
  F' : OWBWWGRRBRROBRBOOOYYWGGYRGYGOGGYYYRGYOGROWBYWWBBOBBWWR  [score=13]
  F2 : OWBWWGRBOGROORBGOOWYYYGGYGRGWWGYYYRGYOBRORBYRWBBOBBWWR  [score=13]
  L' : RWBBWGBWGRRORRBBOOOGYWGYWYWRBRGYYYRGBRYYOOGOGWBYOBGWWO  [score=13]
  L2 : OWBGWGYWGRRORRBBOORGYBGYBYWOBRWYYWRGGYBOORGOYWBYOBGWWR  [score=13]
  B  : OBOWWGWWGRRGRRRBOYRGYGGYYYWOBRGYYYRBBOGWOOOYGWOWWBBRBB  [score=13]
  B2 : GRYWWGWWGRRBRRRBOYRGYGGYYYWOBRGYYBWOOOGBOOOYGRWWBBOBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 71 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 71
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWWBRRORROBORGRGGYYYGOBWGYOYRWYOGROOBYGGBBGBBBWR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWWBRRORRBWRRGRGGYOBOWOWBYROGYYOGROOYYGGBBGBBBYG  [score=17]
  D' : OWYWWYWWWBRRORRYYGRGRGGYBYGYGORYBWOWYOGROOBWRGBBGBBOBO  [score=17]
  D2 : OWYWWYWWWBRRORRBYGRGRGGYBWRWRYOYGWBOYOGROOOBOGBBGBBYYG  [score=17]
  R' : OWRWWYWWGOOBBRRORRRGWGGOYYWOBBGYGYRGYOGROOBYGWBBYBBYWR  [score=15]
  R2 : OWWWWOWWWOBORRORRBRGBGGGYYGOBYGYYYRWYOGROOBYGGBBYBBRWR  [score=15]
  F  : OWYWWYGOGWRRWRRWBOYGRYGGGYROOBGYOYRWYOOROBBYWGBBGBBBWR  [score=15]
  L  : RWYGWYYWWBRRORROBOOGRGGYYYGRBWBYOBRWGOGOOYYRBGBWGBWBWO  [score=15]
  B' : BRYWWYWWWBROORWOBYRGRGGYYYGOBWGYOORRYOGROOWYGBBRBBWGGB  [score=15]
  F' : OWYWWYBOOWRRBRROBORYGGGYRGYGOGGYOYRWYOWROWBYWGBBGBBBWR  [score=13]
  F2 : OWYWWYWBOGRRORRGBOGYYYGGRGRWWWGYOYRWYOOROOBYBGBBGBBBWR  [score=13]
  L' : RWYBWYBWWBRRORROBOOGRWGYWYGRBWGYOYRWBRYYOOGOGGBYGBGBWO  [score=13]
  L2 : OWYGWYYWWBRRORROBORGRBGYBYGOBWWYOWRWGYBOORGOYGBYGBGBWR  [score=13]
  B  : RROWWYWWWBRWORROBYRGRGGYYYGOBWGYOYRBYOGWOOOYGBGGWBBRBB  [score=13]
  B2 : WRYWWYWWWBRBORROBYRGRGGYYYGOBWGYOYWOOOGROORYGRWBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 72 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 72
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWWBRRORRBWRRGRGGYOBOWOWBYROGYYOGROOYYGGBBGBBBYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWBWWGWWGRRRRRWBOBRGYGGYOBWWORBYYOGOYOGROOYYGYBBRBBWYG  [score=17]
  D  : OWYWWYWWWBRRORRBYGRGRGGYBWRWRYOYGWBOYOGROOOBOGBBGBBYYG  [score=17]
  D2 : OWYWWYWWWBRRORRYYGRGRGGYBYGYGORYBWOWYOGROOBWRGBBGBBOBO  [score=17]
  R' : OWRWWYWWOBOBWRRRRRRGWGGROBYWOBBYGOGGYOGROOYYGWBBYBBYYG  [score=15]
  R2 : OWWWWRWWYRWBRRORRBRGBGGGOBGWOYBYYOGWYOGROOYYGOBBYBBRYG  [score=15]
  F  : OWYWWYGOGWRRWRRWWROGRBGGOYRBOBBYROGYYOWROOYYWGBBGBBBYG  [score=15]
  L  : RWYGWYOWWBRRORRBWRWGRBGYOBOGOWBYRBGYGOGOOYYRYGBWGBWBYO  [score=15]
  B' : YRYWWYWWWBROORWBWYRGRGGYOBOWOWBYRRRROOGGOOYYGBBGBBYGGB  [score=15]
  F' : OWYWWYBOBWRRORRWWRRYOGGBRGOGOGBYROGYYOWROWYYWGBBGBBBYG  [score=13]
  F2 : OWYWWYWOWGRRORRGWROBOYGGRGRWWWBYROGYYOBROOYYBGBBGBBBYG  [score=13]
  L' : GWYBWYBWWBRRORRBWROGRWGYWBOROWGYROGYYRYYOOGOGGBOGBBBYW  [score=13]
  L2 : WWYBWYOWWBRRORRBWRGGRBGYBBOOOWWYRWGYGYYOORGOYGBOGBGBYR  [score=13]
  B  : RRRWWYWWWBRYORGBWORGRGGYOBOWOWBYRYRYYOGWOOOYGBGGYBBGBB  [score=13]
  B2 : YGOWWYWWWBRYORRBWYRGRGGYOBOWOWBYRYWOROGROORYGGYBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 73 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 73
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWBWWGWWGRRRRRWBOBRGYGGYOBWWORBYYOGOYOGROOYYGYBBRBBWYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWBWWGWWGRRRRRWWYGRGYGGYBOBRYOOYGWBOYOGROOOBWYBBRBBYYG  [score=17]
  D' : OWBWWGWWGRRRRRWOBWRGYGGYYYGOBWGYOOYRYOGROOWYGYBBRBBBOB  [score=17]
  D2 : OWBWWGWWGRRRRRWYYGRGYGGYWYGOGOYYBROWYOGROOBOBYBBRBBOBW  [score=17]
  R  : OWWWWRWWYRWBRRORRBRGBGGGOBGWOYBYYOGWYOGROOYYGOBBYBBRYG  [score=15]
  R2 : OWRWWYWWOBOBWRRRRRRGWGGROBYWOBBYGOGGYOGROOYYGWBBYBBYYG  [score=15]
  F  : OWBWWGGOGWRRWRWGOBOGRBGGWYYBRRBYYOGOYOWROOYYRYBBRBBWYG  [score=15]
  L  : RWBGWGOWGRRRRRWBOBWGYBGYOBWGORBYYBGOGOGOOYYRYYBWRBWWYO  [score=15]
  B  : RWBWWGWWGRRORRGBOORGYGGYOBWWORBYYYRYBOGWOOOYGWRYYBBGBB  [score=15]
  B' : YRYWWGWWGRRORRWBOBRGYGGYOBWWORBYYBWROOGGOOOYGBBGBBYYRW  [score=15]
  F' : OWBWWGRRBRRRORWWOBYYWGGBRGOGOGBYYOGOYOGROWYYWYBBRBBWYG  [score=13]
  F2 : OWBWWGROWGRRORWGOBWBOYGGYGRGWWBYYOGOYOBRORYYRYBBRBBWYG  [score=13]
  L' : GWBBWGBWGRRRRRWBOBOGYWGYWBWRORGYYOGOYRYYOOGOGYBORBBWYW  [score=13]
  L2 : WWBBWGOWGRRRRRWBOBGGYBGYBBWOORWYYWGOGYYOORGOYYBORBGWYR  [score=13]
  B2 : OGOWWGWWGRRYRRRBOYRGYGGYOBWWORBYYBWOBOGWOORYGGYWBBRBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 74 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 74
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWBWWGWWGRRRRRWWYGRGYGGYBOBRYOOYGWBOYOGROOOBWYBBRBBYYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWBWRRYRRGWRRGOGGGBOORYYOYRWBYYOGROOOBWGBBGBBBYG  [score=17]
  D  : OWBWWGWWGRRRRRWYYGRGYGGYWYGOGOYYBROWYOGROOBOBYBBRBBOBW  [score=17]
  D2 : OWBWWGWWGRRRRRWOBWRGYGGYYYGOBWGYOOYRYOGROOWYGYBBRBBBOB  [score=17]
  R  : OWYWWRWWYRWGRRYRRWRGBGGGBOGRYYOYYWBBYOGROOOBWOBBGBBOYG  [score=15]
  R2 : OWOWWGWWOGYWWRRRRRRGYGGRBOYRYBOYGWBGYOGROOOBWBBBYBBYYG  [score=15]
  F  : OWBWWGWOGWRRWRWGYGBGROGGBYYWRROYGWBOYORROYOBOYBBRBBYYG  [score=15]
  L  : RWBGWGBWGRRRRRWWYGRGYOGYWOBGYOBYGBBOGOWOOBYROYBWRBWYYO  [score=15]
  B  : RWGWWGWWGRRORRBWYWRGYGGYBOBRYOOYGYROBOGWOOOBWYRYYBBGBB  [score=15]
  B' : ORYWWGWWGRRORRWWYBRGYGGYBOBRYOOYGGWRWOGBOOOBWBBGBBYYRY  [score=15]
  F' : OWBWWGRRWORRYRWRYGYYBGGORGBGOWOYGWBOYOGROWOBWYBBRBBYYG  [score=13]
  F2 : OWBWWGOYRWRRORWGYGBOBYGGYGRGWWOYGWBOYOWROROBRYBBRBBYYG  [score=13]
  L' : GWBBWGBWGRRRRRWWYGOGYWGYWOBRYOGYGBBOORYBOOWOGYBWRBOYYR  [score=13]
  L2 : RWBOWGWWGRRRRRWWYGGGYBGYBOBOYOWYGWBOWBOOORGOYYBBRBGYYR  [score=13]
  B2 : OBWWWGWWGRRORRRWYYRGYGGYBOBRYOOYGBWOGOGWOORBWGYYBBRBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 75 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 75
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWBWRRYRRGWRRGOGGGBOORYYOYRWBYYOGROOOBWGBBGBBBYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  D' : OWYWWYWWBWRRYRRBOORGOGGGOBWWORBYYYRYYOGROOBYGGBBGBBGWR  [score=17]
  D2 : OWYWWYWWBWRRYRROBWRGOGGGBYGYBWRYOYYRYOGROOGWRGBBGBBBOO  [score=17]
  R' : OWOWWGWWOGYWWRRRRRRGYGGRBOYRYBOYGWBGYOGROOOBWBBBYBBYYG  [score=15]
  R2 : OWYWWRWWYRWGRRYRRWRGBGGGBOGRYYOYYWBBYOGROOOBWOBBGBBOYG  [score=15]
  F  : OWYWWYWOGWRRWRRBWRBGROGGOGOGYWOYRWBYYORROYOBYGBBGBBBYG  [score=15]
  F' : OWYWWYWYGYRRYRRRWROGOGGORGBGOWOYRWBYYOBROWOBWGBBGBBBYG  [score=15]
  L  : RWYGWYBWBWRRYRRGWRRGOOGGWOOGYYBYRBBYGOWOOBYROGBWGBWBYO  [score=15]
  B' : ORYWWYWWBWROYRWGWYRGOGGGBOORYYOYRRRRWOGBOOYBWBBGBBYGGB  [score=15]
  F2 : OWYWWYYYRWRRORRGWROOBGGGOGRBWWOYRWBYYOGROYOBWGBBGBBBYG  [score=13]
  L' : GWYBWYBWBWRRYRRGWROGOWGGWOORYYGYRBBYORYBOOWOGGBWGBOBYR  [score=13]
  L2 : RWYOWYWWBWRRYRRGWRGGOBGGBOOOYYWYRWBYWBOOORGOYGBBGBGBYR  [score=13]
  B  : RRRWWYWWBWRYYRBGWWRGOGGGBOORYYOYRYROYOGWOOOBWBGGYBBGBB  [score=13]
  B2 : YBWWWYWWBWROYRRGWYRGOGGGBOORYYOYRYWOROGROORBWGYBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 76 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 76
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW  [score=17]
  D  : OWYWWYWWBWRRYRROBWRGOGGGBYGYBWRYOYYRYOGROOGWRGBBGBBBOO  [score=17]
  D2 : OWYWWYWWBWRRYRRBOORGOGGGOBWWORBYYYRYYOGROOBYGGBBGBBGWR  [score=17]
  R' : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  R2 : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  F  : OWYWWYOOGWRRWRRBYGGGRWGGRGOBYWYYBROWYOYRORBOYGBBGBBOBW  [score=15]
  F' : OWYWWYWYBYRRRRRYYGOGRGGWRGGGOOYYBROWYOBROWBOWGBBGBBOBW  [score=15]
  L  : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  L2 : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  B' : BRYWWYWWBWROYRWBYYRGOGGGGWRYRYYYBGRRROGOOOWOOBBWBBBGGO  [score=15]
  B2 : WORWWYWWBWRBYRRBYYRGOGGGGWRYRYYYBYWOGOGROOROOWBOBBGBBG  [score=15]
  F2 : OWYWWYYRYORRORRGYGRWGGGGOGRBWWYYBROWYOBROYBOWGBBGBBOBW  [score=13]
  L' : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  B  : RRGWWYWWBWRWYROBYRRGOGGGGWRYRYYYBYRBYOGWOOOOOOGGBBBWBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 77 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 77
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO  [score=17]
  D' : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  D2 : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  R  : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  R2 : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  F  : OWOWWGOOGWRGWRYGYBGGRWGGBYYWRRYYGRORYOYRORBOOWBBBBBYBW  [score=15]
  L  : RWOGWGGWGRRGRRYWYBYGYYGYRWBWROBYGBORGOOOOOYRBWBWBBWYBO  [score=15]
  L2 : YWOYWGRWGRRGRRYWYBWGYBGYBWBOROWYGWOROOBOORGOYWBGBBGYBR  [score=15]
  B  : GYBWWGWWGRRRRROWYRRGYGGYGWBYROYYGYRBOOGWOOOOOYBWBBBWBB  [score=15]
  B' : BRYWWGWWGRRORRWWYORGYGGYGWBYROYYGBYGROGOOOROOBBWBBBWBY  [score=15]
  B2 : RORWWGWWGRRBRRRWYYRGYGGYGWBYROYYGOWOBOGYOOGOOWBYBBBBBW  [score=15]
  F' : OWOWWGRRWORGRRYYYBYYBGGWRGGGOOYYGRORYOGROWBOWWBBBBBYBW  [score=13]
  F2 : OWOWWGORYORGORYGYBBWGYGGYGRGWWYYGRORYOWRORBORWBBBBBYBW  [score=13]
  L' : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 78 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 78
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO  [score=17]
  D  : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  D2 : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  R  : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  R2 : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  F  : OWOWWGBOGWRGWRYGBWWGRYGGBYYYRRRYOYYRYOOROGGWRWBBBBBBOO  [score=15]
  L  : RWOGWGWWGRRGRRYYBWOGYRGYYYBOGRBYOBYRGOBOOWYRGWBWBBWBOO  [score=15]
  B  : GYWWWGWWGRRRRRYYBYRGYGGYWYBOGRRYOYRGOOGWOOOWBBBWOBBOBB  [score=15]
  B' : GRYWWGWWGRRORRWYBORGYGGYWYBOGRRYOWYGYOGYOORWBBBOBBOWBB  [score=15]
  F' : OWOWWGRRYRRGGRYOBWYYBGGYRGWGOBRYOYYRYOGROWGWWWBBBBBBOO  [score=13]
  F2 : OWOWWGRGOBRGORYGBWBYWYGGYGRGWWRYOYYRYOYRORGWRWBBBBBBOO  [score=13]
  L' : OWOBWGBWGRRGRRYYBWOGYWGYWYBRGRGYOWYRGRYWOOBOGWBYBBRBOO  [score=13]
  L2 : OWORWGYWGRRGRRYYBWOGYBGYBYBOGRWYOWYRBWGOORGOYWBWBBGBOR  [score=13]
  B2 : RYYWWGWWGRRGRRRYBYRGYGGYWYBOGRRYOOWOWOGYOOGWBOOBBBBBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 79 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 79
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB  [score=17]
  D' : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  D2 : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  R' : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  R2 : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  F  : OWYWWYBOGWRRWRRBYGWGRYGGRORWBYRYBYYWYOOROGGWBGBBGBBOOO  [score=15]
  L  : RWYGWYWWBYRRBRRWYGOGRRGOYYROGBBYBBYWGOBOOWYRGGBWGBWOOO  [score=15]
  B' : GRYWWYWWBYROBRWWYYRGRGGOWYROGBRYBGRRYOGYOOWWBBBOBBOGGO  [score=15]
  F' : OWYWWYYBWBRRGRROYGRORGGYRGWGOBRYBYYWYOBROWGWWGBBGBBOOO  [score=13]
  F2 : OWYWWYBGOBRRORRGYGRYWOGGRGRBWWRYBYYWYOWROBGWYGBBGBBOOO  [score=13]
  L' : OWYBWYBWBYRRBRRWYGOGRWGOWYRRGBGYBWYWGRYWOOBOGGBYGBROOO  [score=13]
  L2 : OWYRWYYWBYRRBRRWYGOGRBGOBYROGBWYBWYWBWGOORGOYGBWGBGOOR  [score=13]
  B  : RRGWWYWWBYRWBRYWYYRGRGGOWYROGBRYBYRGYOGWOOOWBOGGOBBOBB  [score=13]
  B2 : WYYWWYWWBYRGBRRWYYRGRGGOWYROGBRYBYWOGOGROORWBOOOBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 80 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 80
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWGWWGWWGRRORROYBORGYGGYWYBBBRGYOORGYOGROOWYRYBBYBBWWB  [score=17]
  D  : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  D2 : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  R' : OWRWWOWWGOBYORRORRRGWGGYWYYBBGGYGORGYOGROOWYRBBBYBBYWB  [score=15]
  R2 : OWWWWYWWYOOORRBRRYRGGGGGWYGBBYGYYORBYOGROOWYRGBBOBBRWB  [score=15]
  F  : OWYWWYROGWRRWRRBOOWGRYGGGOROBYGYYORYYOBROBWYWGBBGBBGWB  [score=15]
  L  : RWYGWYWWBYRRBRROOOBGRGGOOYGBBWBYYBRYGOROOYYRWGBWGBWGWO  [score=15]
  B' : WRYWWYWWBYROBRWOOYRGRGGOWYGBBWGYYORROOGROOYYRBBBBBWGGG  [score=15]
  F' : OWYWWYYBOWRRBRRBOOROGGGYRGWGORGYYORYYOBROWWYWGBBGBBGWB  [score=13]
  F2 : OWYWWYWBBRRRORRGOOGYWOGGRGRBWWGYYORYYOOROBWYYGBBGBBGWB  [score=13]
  L' : BWYBWYBWBYRRBRROOOOGRWGOWYGRBWGYYWRYWRYYOOROGGBOGBGGWB  [score=13]
  L2 : BWYGWYOWBYRRBRROOOBGRBGOBYGOBWWYYWRYRYWOORGOYGBWGBGGWR  [score=13]
  B  : RROWWYWWBYRYBRROOORGRGGOWYGBBWGYYYRWYOGWOOOYRGGGWBBBBB  [score=13]
  B2 : YROWWYWWBYRWBRROOYRGRGGOWYGBBWGYYYWOOOGROORYRBWGBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 81 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 81
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWGWWGWWGRRORROYBORGYGGYWYBBBRGYOORGYOGROOWYRYBBYBBWWB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWGWWGWWGRRORROWWBRGYGGYYBOROGBYRBGOYOGROOWYBYBBYBBWYR  [score=17]
  D' : OWGWWGWWGRRORROWYBRGYGGYWYROGBRYBGORYOGROOWWBYBBYBBYBO  [score=17]
  D2 : OWGWWGWWGRRORROWYRRGYGGYWWBGROOYGRBBYOGROOYBOYBBYBBWYB  [score=17]
  R  : OWWWWYWWYOOORRBRRYRGGGGGWYGBBYGYYORBYOGROOWYRGBBOBBRWB  [score=15]
  R2 : OWRWWOWWGOBYORRORRRGWGGYWYYBBGGYGORGYOGROOWYRBBBYBBYWB  [score=15]
  F  : OWGWWGROGWROWROGBOWGRYGGBYYYRRGYOORGYOBROBWYRYBBYBBWWB  [score=15]
  L  : RWGGWGWWGRRORROYBOBGYGGYOYBBBRBYOBRGGOROOYYRWYBWYBWWWO  [score=15]
  B' : WRYWWGWWGRRORRWYBGRGYGGYWYBBBRGYOOOOOOGROOGYRBBBBBWYYW  [score=15]
  F' : OWGWWGRRYRROBROBBOYYBGGYRGWGORGYOORGYOGROWWYWYBBYBBWWB  [score=13]
  F2 : OWGWWGRBBRROOROGBOBYWYGGYGRGWWGYOORGYOYRORWYRYBBYBBWWB  [score=13]
  L' : BWGBWGBWGRRORROYBOOGYWGYWYBRBRGYOWRGWRYYOOROGYBOYBGWWB  [score=13]
  L2 : BWGGWGOWGRRORROYBOBGYBGYBYBOBRWYOWRGRYWOORGOYYBWYBGWWR  [score=13]
  B  : OOOWWGWWGRRGRRRYBORGYGGYWYBBBRGYOYRWGOGWOOOYRWYYWBBBBB  [score=13]
  B2 : GROWWGWWGRRWRRRYBYRGYGGYWYBBBRGYOGWOOOGOOOOYRBWWBBYBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 82 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 82
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWGWWGWWGRRORROWWBRGYGGYYBOROGBYRBGOYOGROOWYBYBBYBBWYR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWOWRRWRRBOORGGGGRYBOROWBYYBGYYOGROOWYBGBBGBBGYR  [score=17]
  D  : OWGWWGWWGRRORROWYRRGYGGYWWBGROOYGRBBYOGROOYBOYBBYBBWYB  [score=17]
  D2 : OWGWWGWWGRRORROWYBRGYGGYWYROGBRYBGORYOGROOWWBYBBYBBYBO  [score=17]
  R  : OWWWWYWWYOOBRRWRRWRGGGGGYBGROYBYYBGOYOGROOWYBOBBRBBGYR  [score=15]
  R2 : OWGWWRWWOBWWORRORRRGWGGYYBYROGBYGBGGYOGROOWYBOBBYBBYYR  [score=15]
  F  : OWGWWGBOGWROWROGWBYGRBGGOYYWRRBYRBGOYORROOWYGYBBYBBWYR  [score=15]
  L  : RWGGWGYWGRRORROWWBRGYBGYBBOROGBYRBGOGOBOOYYRWYBWYBWWYO  [score=15]
  B' : WRYWWGWWGRRORRWWWGRGYGGYYBOROGBYRBOOBOGGOOOYBBBRBBYYYW  [score=15]
  F' : OWGWWGRRWGROORORWBYYOGGBRGYGOBBYRBGOYOGROWWYWYBBYBBWYR  [score=13]
  F2 : OWGWWGGORBROOROGWBOBYYGGYGRGWWBYRBGOYOWRORWYRYBBYBBWYR  [score=13]
  L' : RWGBWGBWGRRORROWWBOGYWGYWBOROGGYRYGOWRYYOOBOGYBBYBBWYR  [score=13]
  L2 : RWGBWGBWGRRORROWWBRGYBGYBBOOOGWYRWGOBYWOORGOYYBYYBGWYR  [score=13]
  B  : OOBWWGWWGRRORRGWWBRGYGGYYBOROGBYRYRWGOGWOOOYBWYYYBBRBB  [score=13]
  B2 : OGBWWGWWGRRWRRRWWYRGYGGYYBOROGBYRGWOBOGOOOOYBRYWBBYBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 83 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 83
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWOWRRWRRBOORGGGGRYBOROWBYYBGYYOGROOWYBGBBGBBGYR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWOWRRWRRGYRRGGGGRBOOWYYOYGRBBYOGROOYBOGBBGBBWYB  [score=17]
  D' : OWYWWYWWOWRRWRRYBORGGGGRWYBBBRGYOYYWYOGROOGYRGBBGBBBOO  [score=17]
  D2 : OWYWWYWWOWRRWRRWYBRGGGGRGYRYGBYYBWORYOGROOBOOGBBGBBYBO  [score=17]
  R' : OWGWWRWWOBWWORRORRRGWGGYYBYROGBYGBGGYOGROOWYBOBBYBBYYR  [score=15]
  R2 : OWWWWYWWYOOBRRWRRWRGGGGGYBGROYBYYBGOYOGROOWYBOBBRBBGYR  [score=15]
  F  : OWYWWYBOGWRRWRROOOYGRBGGORGBWWBYYBGYYORROOWYWGBBGBBGYR  [score=15]
  F' : OWYWWYWWBWRRORRROOGROGGBRGYGOBBYYBGYYOOROWWYWGBBGBBGYR  [score=15]
  L  : RWYGWYYWOWRRWRRBOORGGBGRBBOROWBYYBGYGOBOOYYRWGBWGBWGYO  [score=15]
  B' : WRYWWYWWOWROWRWBOYRGGGGRYBOROWBYYORRBOGGOOYYBBBRBBYGGG  [score=15]
  F2 : OWYWWYWORBRRORRGOOOBYRGGGGROWWBYYBGYYOBROWWYWGBBGBBGYR  [score=13]
  L' : RWYBWYBWOWRRWRRBOOOGGWGRWBOROWGYYYGYWRYYOOBOGGBBGBBGYR  [score=13]
  L2 : RWYBWYBWOWRRWRRBOORGGBGRBBOOOWWYYWGYBYWOORGOYGBYGBGGYR  [score=13]
  B  : RROWWYWWOWRYWRGBOBRGGGGRYBOROWBYYYRWYOGWOOOYBGGGYBBRBB  [score=13]
  B2 : YGBWWYWWOWRWWRRBOYRGGGGRYBOROWBYYYWOOOGROORYBRYGBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 84 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 84
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWOWRRWRRGYRRGGGGRBOOWYYOYGRBBYOGROOYBOGBBGBBWYB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWWWWGWWGRRRRRYWWGRGYGGYBOOWYGOYRRBOYOGROOYBOBBBGBBYYB  [score=17]
  D  : OWYWWYWWOWRRWRRWYBRGGGGRGYRYGBYYBWORYOGROOBOOGBBGBBYBO  [score=17]
  D2 : OWYWWYWWOWRRWRRYBORGGGGRWYBBBRGYOYYWYOGROOGYRGBBGBBBOO  [score=17]
  R' : OWGWWRWWOGWWYRRRRRRGYGGGBOBWYWOYGRBGYOGROOYBOOBBYBBYYB  [score=15]
  R2 : OWYWWGWWBRYGRRWRRWRGWGGGBOGWYYOYYRBOYOGROOYBOOBBRBBGYB  [score=15]
  F  : OWYWWYOOGWRRWRROYRBGROGGORGGWWOYGRBBYOWROYYBYGBBGBBWYB  [score=15]
  F' : OWYWWYWWGYRRYRRWYRGROGGORGBGOOOYGRBBYOOROWYBWGBBGBBWYB  [score=15]
  L  : RWYGWYBWOWRRWRRGYRWGGOGRROOBYYBYGBBBGOOOOBYRYGBWGBWWYO  [score=15]
  B' : YRYWWYWWOWROWRWGYYRGGGGRBOOWYYOYGRRRROGBOOBBOBBBBBYGGW  [score=15]
  F2 : OWYWWYYYWORRORRGYROOBRGGGGROWWOYGRBBYOGROWYBWGBBGBBWYB  [score=13]
  L' : BWYBWYBWOWRRWRRGYROGGWGRWOORYYGYGBBBYRYBOOOOGGBRGBOWYW  [score=13]
  L2 : WWYOWYRWOWRRWRRGYRBGGBGRBOOOYYWYGWBBOBYOORGOYGBBGBGWYR  [score=13]
  B  : RRRWWYWWOWRBWRBGYRRGGGGRBOOWYYOYGYRYYOGWOOOBOWGGYBBBBB  [score=13]
  B2 : BBRWWYWWOWRYWRRGYYRGGGGRBOOWYYOYGYWOROGROORBOBYWBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 85 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 85
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWWWWGWWGRRRRRYWWGRGYGGYBOOWYGOYRRBOYOGROOYBOBBBGBBYYB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWWWWGWWGRRRRRYYYBRGYGGYWWGGROYYBWORYOGROOBOOBBBGBBYBO  [score=17]
  D' : OWWWWGWWGRRRRRYBOORGYGGYYBOROWBYYORGYOGROOYYBBBBGBBWWG  [score=17]
  D2 : OWWWWGWWGRRRRRYYBORGYGGYYYBOBRRYOGYWYOGROOWWGBBBGBBBOO  [score=17]
  R  : OWYWWGWWBRYGRRWRRWRGWGGGBOGWYYOYYRBOYOGROOYBOOBBRBBGYB  [score=15]
  R2 : OWGWWRWWOGWWYRRRRRRGYGGGBOBWYWOYGRBGYOGROOYBOOBBYBBYYB  [score=15]
  F  : OWWWWGOOGWRRWRYGWGBGROGGOYYWRROYRRBOYOWROYYBGBBBGBBYYB  [score=15]
  L  : RWWGWGBWGRRRRRYWWGWGYOGYROOBYGBYRBBOGOOOOBYRYBBWGBWYYO  [score=15]
  B' : YRYWWGWWGRRORRWWWWRGYGGYBOOWYGOYRGYRROGBOOOBOBBBBBYBGY  [score=15]
  F' : OWWWWGRRWGRRYRYWWGYYOGGORGBGOOOYRRBOYOGROWYBWBBBGBBYYB  [score=13]
  F2 : OWWWWGGYWORRORYGWGOOBYGGYGRGWWOYRRBOYOWRORYBRBBBGBBYYB  [score=13]
  L' : BWWBWGBWGRRRRRYWWGOGYWGYWOORYGGYRBBOYRYBOOOOGBBRGBOYYW  [score=13]
  L2 : WWWOWGRWGRRRRRYWWGBGYBGYBOOOYGWYRWBOOBYOORGOYBBBGBGYYR  [score=13]
  B  : RYGWWGWWGRRORRBWWRRGYGGYBOOWYGOYRYRYWOGWOOOBOYGBYBBBBB  [score=13]
  B2 : OBRWWGWWGRRYRRRWWYRGYGGYBOOWYGOYRWWOGOGYOORBOBYYBBGBBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 86 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 86
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWWWWGWWGRRRRRYYYBRGYGGYWWGGROYYBWORYOGROOBOOBBBGBBYBO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWGYRRYRRBYRRGOGGBWWRGRYYYGWOBYOGROOBOOGBBGBBWBO  [score=17]
  D  : OWWWWGWWGRRRRRYYBORGYGGYYYBOBRRYOGYWYOGROOWWGBBBGBBBOO  [score=17]
  D2 : OWWWWGWWGRRRRRYBOORGYGGYYBOROWBYYORGYOGROOYYBBBBGBBWWG  [score=17]
  R  : OWYWWGWWBRYBRRYRRYRGWGGGWWGGRYYYYWOGYOGROOBOORBBBBBOBO  [score=15]
  R2 : OWOWWBWWRBYYYRRRRRRGYGGGWWBGRWYYGWOGYOGROOBOOGBBYBBYBO  [score=15]
  F  : OWWWWGOOGWRRWRYGYBWGRWGGGYYYRRYYBWORYOGRORBOOBBBGBBYBO  [score=15]
  L  : RWWGWGWWGRRRRRYYYBGGYYGYWWGOROBYBBORGOOOOOYRBBBWGBWYBO  [score=15]
  L2 : GWWYWGWWGRRRRRYYYBOGYBGYBWGOROWYBWOROOBOORGOYBBWGBGYBR  [score=15]
  B' : BRYWWGWWGRRORRWYYWRGYGGYWWGGROYYBBYRWOGOOOROOBBOBBBBGY  [score=15]
  B2 : ROWWWGWWGRRBRRRYYYRGYGGYWWGGROYYBWWOBOGYOOROOOBYBBGBBB  [score=15]
  F' : OWWWWGRRYORRRRYGYBYYGGGWRGWGOOYYBWORYOGROWBOWBBBGBBYBO  [score=13]
  F2 : OWWWWGORGORRORYGYBGWWYGGYGRGWWYYBWORYOYRORBORBBBGBBYBO  [score=13]
  L' : OWWBWGBWGRRRRRYYYBOGYWGYWWGRROGYBWORBRYOOOOOGBBWGBYYBG  [score=13]
  B  : RYBWWGWWGRRRRROYYWRGYGGYWWGGROYYBYRBWOGWOOOOOYGBBBBOBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 87 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 87
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWGYRRYRRBYRRGOGGBWWRGRYYYGWOBYOGROOBOOGBBGBBWBO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWGYRRYRRWBORGOGGBBYRYGBRYOGYWYOGROOWWRGBBGBBBOO  [score=17]
  D' : OWYWWYWWGYRRYRRWWRRGOGGBBOOWYGOYRBGYYOGROOWBOGBBGBBBYR  [score=17]
  D2 : OWYWWYWWGYRRYRRBOORGOGGBWBOBOWGYYYRGYOGROOBYRGBBGBBWWR  [score=17]
  R' : OWOWWBWWRBYYYRRRRRRGYGGGWWBGRWYYGWOGYOGROOBOOGBBYBBYBO  [score=15]
  R2 : OWYWWGWWBRYBRRYRRYRGWGGGWWGGRYYYYWOGYOGROOBOORBBBBBOBO  [score=15]
  F  : OWYWWYOOGWRRWRRGYRWGRWGGRBOBYYYYGWOBYOGRORBOYGBBGBBWBO  [score=15]
  L  : RWYGWYWWGYRRYRRBYRGGOYGBWWRORYBYGBOBGOOOOOYRBGBWGBWWBO  [score=15]
  L2 : GWYYWYWWGYRRYRRBYROGOBGBBWRORYWYGWOBOOBOORGOYGBWGBGWBR  [score=15]
  B' : BRYWWYWWGYROYRWBYYRGOGGBWWRGRYYYGRRRWOGOOOBOOBBOBBBGGW  [score=15]
  B2 : BOWWWYWWGYRBYRRBYYRGOGGBWWRGRYYYGYWOROGROOROOOBWBBGBBG  [score=15]
  F' : OWYWWYYYBYRRRRRGYROBRGGWRGWGOOYYGWOBYOGROWBOWGBBGBBWBO  [score=13]
  F2 : OWYWWYYRGORRORRGYRRWWBGGOGRGWWYYGWOBYOBROYBOYGBBGBBWBO  [score=13]
  L' : OWYBWYBWGYRRYRRBYROGOWGBWWRRRYGYGWOBBRYOOOOOGGBWGBYWBG  [score=13]
  B  : RRRWWYWWGYRBYROBYWRGOGGBWWRGRYYYGYRBYOGWOOOOOWGGBBBOBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 88 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 88
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWGYRRYRRWBORGOGGBBYRYGBRYOGYWYOGROOWWRGBBGBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWBWWGWWGRRORRBYYWRGYGGYBYGYGORYBGYRYOGROOWWRWBBOBBBOO  [score=17]
  D  : OWYWWYWWGYRRYRRBOORGOGGBWBOBOWGYYYRGYOGROOBYRGBBGBBWWR  [score=17]
  D2 : OWYWWYWWGYRRYRRWWRRGOGGBBOOWYGOYRBGYYOGROOWBOGBBGBBBYR  [score=17]
  R' : OWOWWBWWRWYYBRRORRRGBGGOBYWYGBRYGGYGYOGROOWWRGBBYBBYOO  [score=15]
  R2 : OWBWWOWWWOBWRRYRRYRGBGGGBYGYGYRYYGYGYOGROOWWRRBBBBBOOO  [score=15]
  F  : OWYWWYROGWRRWRRGBOBGRYGGRBOWYYRYOGYWYOYROGWWBGBBGBBBOO  [score=15]
  L  : RWYGWYBWGYRRYRRWBOYGORGBGYROGBBYOBYWGOROOWYRWGBWGBWBOO  [score=15]
  B' : WRYWWYWWGYROYRWWBYRGOGGBBYRYGBRYOORRGOGYOOWWRBBOBBOGGB  [score=15]
  F' : OWYWWYYYWBRRGRRYBOOBRGGYRGBGORRYOGYWYOGROWWWWGBBGBBBOO  [score=13]
  F2 : OWYWWYBGYRRRORRGBORYBBGGOGRGWWRYOGYWYOWROYWWYGBBGBBBOO  [score=13]
  L' : OWYBWYBWGYRRYRRWBOOGOWGBWYRRGBGYOBYWWRYWOOROGGBGGBRBOY  [score=13]
  L2 : YWYRWYGWGYRRYRRWBOOGOBGBBYROGBWYOWYWRWWOORGOYGBBGBGBOR  [score=13]
  B  : RROWWYWWGYRWYRYWBGRGOGGBBYRYGBRYOYRWYOGWOOOWRBGGOBBOBB  [score=13]
  B2 : WYGWWYWWGYRWYRRWBYRGOGGBBYRYGBRYOYWOOOGROORWROOBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 89 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 89
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWBWWGWWGRRORRBYYWRGYGGYBYGYGORYBGYRYOGROOWWRWBBOBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWBWWGWWGRRORRBBOORGYGGYYYWOBRGYYYRGYOGROOBYGWBBOBBWWR  [score=17]
  D' : OWBWWGWWGRRORRBBYGRGYGGYWWRGRYYYGRBOYOGROOBOOWBBOBBYYW  [score=17]
  D2 : OWBWWGWWGRRORRBWWRRGYGGYBOORYGBYROGYYOGROOYYWWBBOBBBYG  [score=17]
  R  : OWBWWOWWWOBWRRYRRYRGBGGGBYGYGYRYYGYGYOGROOWWRRBBBBBOOO  [score=15]
  R2 : OWOWWBWWRWYYBRRORRRGBGGOBYWYGBRYGGYGYOGROOWWRGBBYBBYOO  [score=15]
  F  : OWBWWGROGWROWRBGYWBGRYGGGYYYRRRYBGYRYOYROGWWOWBBOBBBOO  [score=15]
  L  : RWBGWGBWGRRORRBYYWYGYRGYGYGOGOBYBBYRGOROOWYRWWBWOBWBOO  [score=15]
  B' : WRYWWGWWGRRORRWYYBRGYGGYBYGYGORYBWBOGOGYOORWRBBOBBOWOB  [score=15]
  F' : OWBWWGRRYOROGRBYYWYYGGGYRGBGORRYBGYRYOGROWWWWWBBOBBBOO  [score=13]
  F2 : OWBWWGOGYRROORBGYWGYBYGGYGRGWWRYBGYRYOYRORWWRWBBOBBBOO  [score=13]
  L' : OWBBWGBWGRRORRBYYWOGYWGYWYGRGOGYBBYRWRYWOOROGWBGOBRBOY  [score=13]
  L2 : YWBRWGGWGRRORRBYYWOGYBGYBYGOGOWYBWYRRWWOORGOYWBBOBGBOR  [score=13]
  B  : OBWWWGWWGRRRRRYYYGRGYGGYBYGYGORYBYRWBOGWOOOWRBOWOBBOBB  [score=13]
  B2 : RYGWWGWWGRRWRRRYYYRGYGGYBYGYGORYBBWOWOGBOOOWROOBBBOBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 90 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 90
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWBWWGWWGRRORRBBOORGYGGYYYWOBRGYYYRGYOGROOBYGWBBOBBWWR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWWBRRORROBORGRGGYYYGOBWGYOYRWYOGROOBYGGBBGBBBWR  [score=17]
  D  : OWBWWGWWGRRORRBWWRRGYGGYBOORYGBYROGYYOGROOYYWWBBOBBBYG  [score=17]
  D2 : OWBWWGWWGRRORRBBYGRGYGGYWWRGRYYYGRBOYOGROOBOOWBBOBBYYW  [score=17]
  R  : OWWWWOWWWOBORRORRBRGBGGGYYGOBYGYYYRWYOGROOBYGGBBYBBRWR  [score=15]
  R2 : OWRWWYWWGOOBBRRORRRGWGGOYYWOBBGYGYRGYOGROOBYGWBBYBBYWR  [score=15]
  F  : OWBWWGGOGWROWRBGOOYGRYGGWYYBRRGYYYRGYOOROBBYRWBBOBBWWR  [score=15]
  L  : RWBGWGYWGRRORRBBOOOGYGGYYYWRBRBYYBRGGOGOOYYRBWBWOBWWWO  [score=15]
  B' : BRYWWGWWGRRORRWBOBRGYGGYYYWOBRGYYOBOYOGROOGYGBBRBBWWOW  [score=15]
  F' : OWBWWGRRBRROBRBOOOYYWGGYRGYGOGGYYYRGYOGROWBYWWBBOBBWWR  [score=13]
  F2 : OWBWWGRBOGROORBGOOWYYYGGYGRGWWGYYYRGYOBRORBYRWBBOBBWWR  [score=13]
  L' : RWBBWGBWGRRORRBBOOOGYWGYWYWRBRGYYYRGBRYYOOGOGWBYOBGWWO  [score=13]
  L2 : OWBGWGYWGRRORRBBOORGYBGYBYWOBRWYYWRGGYBOORGOYWBYOBGWWR  [score=13]
  B  : OBOWWGWWGRRGRRRBOYRGYGGYYYWOBRGYYYRBBOGWOOOYGWOWWBBRBB  [score=13]
  B2 : GRYWWGWWGRRBRRRBOYRGYGGYYYWOBRGYYBWOOOGBOOOYGRWWBBOBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 91 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 91
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWWBRRORROBORGRGGYYYGOBWGYOYRWYOGROOBYGGBBGBBBWR

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWWBRRORRBWRRGRGGYOBOWOWBYROGYYOGROOYYGGBBGBBBYG  [score=17]
  D' : OWYWWYWWWBRRORRYYGRGRGGYBYGYGORYBWOWYOGROOBWRGBBGBBOBO  [score=17]
  D2 : OWYWWYWWWBRRORRBYGRGRGGYBWRWRYOYGWBOYOGROOOBOGBBGBBYYG  [score=17]
  R' : OWRWWYWWGOOBBRRORRRGWGGOYYWOBBGYGYRGYOGROOBYGWBBYBBYWR  [score=15]
  R2 : OWWWWOWWWOBORRORRBRGBGGGYYGOBYGYYYRWYOGROOBYGGBBYBBRWR  [score=15]
  F  : OWYWWYGOGWRRWRRWBOYGRYGGGYROOBGYOYRWYOOROBBYWGBBGBBBWR  [score=15]
  L  : RWYGWYYWWBRRORROBOOGRGGYYYGRBWBYOBRWGOGOOYYRBGBWGBWBWO  [score=15]
  B' : BRYWWYWWWBROORWOBYRGRGGYYYGOBWGYOORRYOGROOWYGBBRBBWGGB  [score=15]
  F' : OWYWWYBOOWRRBRROBORYGGGYRGYGOGGYOYRWYOWROWBYWGBBGBBBWR  [score=13]
  F2 : OWYWWYWBOGRRORRGBOGYYYGGRGRWWWGYOYRWYOOROOBYBGBBGBBBWR  [score=13]
  L' : RWYBWYBWWBRRORROBOOGRWGYWYGRBWGYOYRWBRYYOOGOGGBYGBGBWO  [score=13]
  L2 : OWYGWYYWWBRRORROBORGRBGYBYGOBWWYOWRWGYBOORGOYGBYGBGBWR  [score=13]
  B  : RROWWYWWWBRWORROBYRGRGGYYYGOBWGYOYRBYOGWOOOYGBGGWBBRBB  [score=13]
  B2 : WRYWWYWWWBRBORROBYRGRGGYYYGOBWGYOYWOOOGROORYGRWBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 92 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 92
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWWBRRORRBWRRGRGGYOBOWOWBYROGYYOGROOYYGGBBGBBBYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWBWWGWWGRRRRRWBOBRGYGGYOBWWORBYYOGOYOGROOYYGYBBRBBWYG  [score=17]
  D  : OWYWWYWWWBRRORRBYGRGRGGYBWRWRYOYGWBOYOGROOOBOGBBGBBYYG  [score=17]
  D2 : OWYWWYWWWBRRORRYYGRGRGGYBYGYGORYBWOWYOGROOBWRGBBGBBOBO  [score=17]
  R' : OWRWWYWWOBOBWRRRRRRGWGGROBYWOBBYGOGGYOGROOYYGWBBYBBYYG  [score=15]
  R2 : OWWWWRWWYRWBRRORRBRGBGGGOBGWOYBYYOGWYOGROOYYGOBBYBBRYG  [score=15]
  F  : OWYWWYGOGWRRWRRWWROGRBGGOYRBOBBYROGYYOWROOYYWGBBGBBBYG  [score=15]
  L  : RWYGWYOWWBRRORRBWRWGRBGYOBOGOWBYRBGYGOGOOYYRYGBWGBWBYO  [score=15]
  B' : YRYWWYWWWBROORWBWYRGRGGYOBOWOWBYRRRROOGGOOYYGBBGBBYGGB  [score=15]
  F' : OWYWWYBOBWRRORRWWRRYOGGBRGOGOGBYROGYYOWROWYYWGBBGBBBYG  [score=13]
  F2 : OWYWWYWOWGRRORRGWROBOYGGRGRWWWBYROGYYOBROOYYBGBBGBBBYG  [score=13]
  L' : GWYBWYBWWBRRORRBWROGRWGYWBOROWGYROGYYRYYOOGOGGBOGBBBYW  [score=13]
  L2 : WWYBWYOWWBRRORRBWRGGRBGYBBOOOWWYRWGYGYYOORGOYGBOGBGBYR  [score=13]
  B  : RRRWWYWWWBRYORGBWORGRGGYOBOWOWBYRYRYYOGWOOOYGBGGYBBGBB  [score=13]
  B2 : YGOWWYWWWBRYORRBWYRGRGGYOBOWOWBYRYWOROGROORYGGYBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 93 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 93
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWBWWGWWGRRRRRWBOBRGYGGYOBWWORBYYOGOYOGROOYYGYBBRBBWYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWBWWGWWGRRRRRWWYGRGYGGYBOBRYOOYGWBOYOGROOOBWYBBRBBYYG  [score=17]
  D' : OWBWWGWWGRRRRRWOBWRGYGGYYYGOBWGYOOYRYOGROOWYGYBBRBBBOB  [score=17]
  D2 : OWBWWGWWGRRRRRWYYGRGYGGYWYGOGOYYBROWYOGROOBOBYBBRBBOBW  [score=17]
  R  : OWWWWRWWYRWBRRORRBRGBGGGOBGWOYBYYOGWYOGROOYYGOBBYBBRYG  [score=15]
  R2 : OWRWWYWWOBOBWRRRRRRGWGGROBYWOBBYGOGGYOGROOYYGWBBYBBYYG  [score=15]
  F  : OWBWWGGOGWRRWRWGOBOGRBGGWYYBRRBYYOGOYOWROOYYRYBBRBBWYG  [score=15]
  L  : RWBGWGOWGRRRRRWBOBWGYBGYOBWGORBYYBGOGOGOOYYRYYBWRBWWYO  [score=15]
  B  : RWBWWGWWGRRORRGBOORGYGGYOBWWORBYYYRYBOGWOOOYGWRYYBBGBB  [score=15]
  B' : YRYWWGWWGRRORRWBOBRGYGGYOBWWORBYYBWROOGGOOOYGBBGBBYYRW  [score=15]
  F' : OWBWWGRRBRRRORWWOBYYWGGBRGOGOGBYYOGOYOGROWYYWYBBRBBWYG  [score=13]
  F2 : OWBWWGROWGRRORWGOBWBOYGGYGRGWWBYYOGOYOBRORYYRYBBRBBWYG  [score=13]
  L' : GWBBWGBWGRRRRRWBOBOGYWGYWBWRORGYYOGOYRYYOOGOGYBORBBWYW  [score=13]
  L2 : WWBBWGOWGRRRRRWBOBGGYBGYBBWOORWYYWGOGYYOORGOYYBORBGWYR  [score=13]
  B2 : OGOWWGWWGRRYRRRBOYRGYGGYOBWWORBYYBWOBOGWOORYGGYWBBRBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 94 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 94
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWBWWGWWGRRRRRWWYGRGYGGYBOBRYOOYGWBOYOGROOOBWYBBRBBYYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWBWRRYRRGWRRGOGGGBOORYYOYRWBYYOGROOOBWGBBGBBBYG  [score=17]
  D  : OWBWWGWWGRRRRRWYYGRGYGGYWYGOGOYYBROWYOGROOBOBYBBRBBOBW  [score=17]
  D2 : OWBWWGWWGRRRRRWOBWRGYGGYYYGOBWGYOOYRYOGROOWYGYBBRBBBOB  [score=17]
  R  : OWYWWRWWYRWGRRYRRWRGBGGGBOGRYYOYYWBBYOGROOOBWOBBGBBOYG  [score=15]
  R2 : OWOWWGWWOGYWWRRRRRRGYGGRBOYRYBOYGWBGYOGROOOBWBBBYBBYYG  [score=15]
  F  : OWBWWGWOGWRRWRWGYGBGROGGBYYWRROYGWBOYORROYOBOYBBRBBYYG  [score=15]
  L  : RWBGWGBWGRRRRRWWYGRGYOGYWOBGYOBYGBBOGOWOOBYROYBWRBWYYO  [score=15]
  B  : RWGWWGWWGRRORRBWYWRGYGGYBOBRYOOYGYROBOGWOOOBWYRYYBBGBB  [score=15]
  B' : ORYWWGWWGRRORRWWYBRGYGGYBOBRYOOYGGWRWOGBOOOBWBBGBBYYRY  [score=15]
  F' : OWBWWGRRWORRYRWRYGYYBGGORGBGOWOYGWBOYOGROWOBWYBBRBBYYG  [score=13]
  F2 : OWBWWGOYRWRRORWGYGBOBYGGYGRGWWOYGWBOYOWROROBRYBBRBBYYG  [score=13]
  L' : GWBBWGBWGRRRRRWWYGOGYWGYWOBRYOGYGBBOORYBOOWOGYBWRBOYYR  [score=13]
  L2 : RWBOWGWWGRRRRRWWYGGGYBGYBOBOYOWYGWBOWBOOORGOYYBBRBGYYR  [score=13]
  B2 : OBWWWGWWGRRORRRWYYRGYGGYBOBRYOOYGBWOGOGWOORBWGYYBBRBBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 95 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 95
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWBWRRYRRGWRRGOGGGBOORYYOYRWBYYOGROOOBWGBBGBBBYG

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW  [score=17]
  D' : OWYWWYWWBWRRYRRBOORGOGGGOBWWORBYYYRYYOGROOBYGGBBGBBGWR  [score=17]
  D2 : OWYWWYWWBWRRYRROBWRGOGGGBYGYBWRYOYYRYOGROOGWRGBBGBBBOO  [score=17]
  R' : OWOWWGWWOGYWWRRRRRRGYGGRBOYRYBOYGWBGYOGROOOBWBBBYBBYYG  [score=15]
  R2 : OWYWWRWWYRWGRRYRRWRGBGGGBOGRYYOYYWBBYOGROOOBWOBBGBBOYG  [score=15]
  F  : OWYWWYWOGWRRWRRBWRBGROGGOGOGYWOYRWBYYORROYOBYGBBGBBBYG  [score=15]
  F' : OWYWWYWYGYRRYRRRWROGOGGORGBGOWOYRWBYYOBROWOBWGBBGBBBYG  [score=15]
  L  : RWYGWYBWBWRRYRRGWRRGOOGGWOOGYYBYRBBYGOWOOBYROGBWGBWBYO  [score=15]
  B' : ORYWWYWWBWROYRWGWYRGOGGGBOORYYOYRRRRWOGBOOYBWBBGBBYGGB  [score=15]
  F2 : OWYWWYYYRWRRORRGWROOBGGGOGRBWWOYRWBYYOGROYOBWGBBGBBBYG  [score=13]
  L' : GWYBWYBWBWRRYRRGWROGOWGGWOORYYGYRBBYORYBOOWOGGBWGBOBYR  [score=13]
  L2 : RWYOWYWWBWRRYRRGWRGGOBGGBOOOYYWYRWBYWBOOORGOYGBBGBGBYR  [score=13]
  B  : RRRWWYWWBWRYYRBGWWRGOGGGBOORYYOYRYROYOGWOOOBWBGGYBBGBB  [score=13]
  B2 : YBWWWYWWBWROYRRGWYRGOGGGBOORYYOYRYWOROGROORBWGYBBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 96 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 96
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWBWRRYRRBYGRGOGGGGWRYRYYYBROWYOGROOBOOGBBGBBOBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW  [score=17]
  D  : OWYWWYWWBWRRYRROBWRGOGGGBYGYBWRYOYYRYOGROOGWRGBBGBBBOO  [score=17]
  D2 : OWYWWYWWBWRRYRRBOORGOGGGOBWWORBYYYRYYOGROOBYGGBBGBBGWR  [score=17]
  R' : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  R2 : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  F  : OWYWWYOOGWRRWRRBYGGGRWGGRGOBYWYYBROWYOYRORBOYGBBGBBOBW  [score=15]
  F' : OWYWWYWYBYRRRRRYYGOGRGGWRGGGOOYYBROWYOBROWBOWGBBGBBOBW  [score=15]
  L  : RWYGWYGWBWRRYRRBYGYGOYGGRWRWRYBYBBOWGOOOOOYRBGBWGBWOBO  [score=15]
  L2 : YWYYWYRWBWRRYRRBYGWGOBGGBWRORYWYBWOWOOBOORGOYGBGGBGOBR  [score=15]
  B' : BRYWWYWWBWROYRWBYYRGOGGGGWRYRYYYBGRRROGOOOWOOBBWBBBGGO  [score=15]
  B2 : WORWWYWWBWRBYRRBYYRGOGGGGWRYRYYYBYWOGOGROOROOWBOBBGBBG  [score=15]
  F2 : OWYWWYYRYORRORRGYGRWGGGGOGRBWWYYBROWYOBROYBOWGBBGBBOBW  [score=13]
  L' : WWYBWYBWBWRRYRRBYGOGOWGGWWRRRYGYBGOWBRYOOOOOGGBRGBYOBY  [score=13]
  B  : RRGWWYWWBWRWYROBYRRGOGGGGWRYRYYYBYRBYOGWOOOOOOGGBBBWBB  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 97 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 97
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R

Current state:
OWOWWGWWGRRGRRYWYBRGYGGYGWBYROYYGRORYOGROOBOOWBBBBBYBW

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO  [score=17]
  D' : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  D2 : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  R  : OWYWWBWWWGYBRRYRRWRGOGGGGWGYRYYYYROBYOGROOBOORBBGBBOBW  [score=15]
  R2 : OWOWWGWWRBYWYRRGRRRGYGGBGWWYROYYGROGYOGROOBOOBBBYBBYBW  [score=15]
  F  : OWOWWGOOGWRGWRYGYBGGRWGGBYYWRRYYGRORYOYRORBOOWBBBBBYBW  [score=15]
  L  : RWOGWGGWGRRGRRYWYBYGYYGYRWBWROBYGBORGOOOOOYRBWBWBBWYBO  [score=15]
  L2 : YWOYWGRWGRRGRRYWYBWGYBGYBWBOROWYGWOROOBOORGOYWBGBBGYBR  [score=15]
  B  : GYBWWGWWGRRRRROWYRRGYGGYGWBYROYYGYRBOOGWOOOOOYBWBBBWBB  [score=15]
  B' : BRYWWGWWGRRORRWWYORGYGGYGWBYROYYGBYGROGOOOROOBBWBBBWBY  [score=15]
  B2 : RORWWGWWGRRBRRRWYYRGYGGYGWBYROYYGOWOBOGYOOGOOWBYBBBBBW  [score=15]
  F' : OWOWWGRRWORGRRYYYBYYBGGWRGGGOOYYGRORYOGROWBOWWBBBBBYBW  [score=13]
  F2 : OWOWWGORYORGORYGYBBWGYGGYGRGWWYYGRORYOWRORBORWBBBBBYBW  [score=13]
  L' : WWOBWGBWGRRGRRYWYBOGYWGYWWBRROGYGGORBRYOOOOOGWBRBBYYBY  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 98 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 98
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWOWWGWWGRRGRRYYBWRGYGGYWYBOGRRYOYYRYOGROOGWBWBBBBBBOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R' : OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO  [score=17]
  D  : OWOWWGWWGRRGRRYBOORGYGGYYBWRORGYYORYYOGROOWYBWBBBBBGWB  [score=17]
  D2 : OWOWWGWWGRRGRRYGWBRGYGGYBOORYYOYRRGOYOGROOYBWWBBBBBWYB  [score=17]
  R  : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  R2 : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  F  : OWOWWGBOGWRGWRYGBWWGRYGGBYYYRRRYOYYRYOOROGGWRWBBBBBBOO  [score=15]
  L  : RWOGWGWWGRRGRRYYBWOGYRGYYYBOGRBYOBYRGOBOOWYRGWBWBBWBOO  [score=15]
  B  : GYWWWGWWGRRRRRYYBYRGYGGYWYBOGRRYOYRGOOGWOOOWBBBWOBBOBB  [score=15]
  B' : GRYWWGWWGRRORRWYBORGYGGYWYBOGRRYOWYGYOGYOORWBBBOBBOWBB  [score=15]
  F' : OWOWWGRRYRRGGRYOBWYYBGGYRGWGOBRYOYYRYOGROWGWWWBBBBBBOO  [score=13]
  F2 : OWOWWGRGOBRGORYGBWBYWYGGYGRGWWRYOYYRYOYRORGWRWBBBBBBOO  [score=13]
  L' : OWOBWGBWGRRGRRYYBWOGYWGYWYBRGRGYOWYRGRYWOOBOGWBYBBRBOO  [score=13]
  L2 : OWORWGYWGRRGRRYYBWOGYBGYBYBOGRWYOWYRBWGOORGOYWBWBBGBOR  [score=13]
  B2 : RYYWWGWWGRRGRRRYBYRGYGGYWYBOGRRYOOWOWOGYOOGWBOOBBBBBBW  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 99 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 99
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: R'

Current state:
OWYWWYWWBYRRBRRWYGRGRGGOWYROGBRYBYYWYOGROOGWBGBBGBBOOO

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  D  : OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB  [score=17]
  D' : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  D2 : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  R' : OWRWWOWWRWBYYRRGRRRGBGGBWYWOGORYGYYGYOGROOGWBBBBYBBYOO  [score=15]
  R2 : OWBWWBWWWGYWRRBRRYRGOGGGWYGOGYRYYYYBYOGROOGWBRBBOBBROO  [score=15]
  F  : OWYWWYBOGWRRWRRBYGWGRYGGRORWBYRYBYYWYOOROGGWBGBBGBBOOO  [score=15]
  L  : RWYGWYWWBYRRBRRWYGOGRRGOYYROGBBYBBYWGOBOOWYRGGBWGBWOOO  [score=15]
  B' : GRYWWYWWBYROBRWWYYRGRGGOWYROGBRYBGRRYOGYOOWWBBBOBBOGGO  [score=15]
  F' : OWYWWYYBWBRRGRROYGRORGGYRGWGOBRYBYYWYOBROWGWWGBBGBBOOO  [score=13]
  F2 : OWYWWYBGOBRRORRGYGRYWOGGRGRBWWRYBYYWYOWROBGWYGBBGBBOOO  [score=13]
  L' : OWYBWYBWBYRRBRRWYGOGRWGOWYRRGBGYBWYWGRYWOOBOGGBYGBROOO  [score=13]
  L2 : OWYRWYYWBYRRBRRWYGOGRBGOBYROGBWYBWYWBWGOORGOYGBWGBGOOR  [score=13]
  B  : RRGWWYWWBYRWBRYWYYRGRGGOWYROGBRYBYRGYOGWOOOWBOGGOBBOBB  [score=13]
  B2 : WYYWWYWWBYRGBRRWYYRGRGGOWYROGBRYBYWOGOGROORWBOOOBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 100 (default)

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

STRATEGY:
- Phase white_cross: get W at U positions 1,3,5,7 and matching side edges.
- Phase full_solve: match current state to solved state.

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata (score after applying the move).

MOVE SELECTION RULE (white_cross phase):
- U-face moves (U, U', U2) rotate white edge stickers directly onto the U face. PREFER them.
- If ANY U-face move (U, U', U2) appears in the table with score >= (current score - 2), pick it.
- Otherwise, pick the FIRST entry in the table.

MOVE SELECTION RULE (full_solve phase):
- Pick the FIRST entry in the table (highest score).

COPY RULE:
- Copy next_state EXACTLY: the 54-character string that appears BETWEEN ": " and "  [score=" on the chosen line.
- Do NOT compute or modify next_state — copy it character-by-character from the table.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 100
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 17
Previous move: D

Current state:
OWYWWYWWBYRRBRROOORGRGGOWYGBBWGYYORYYOGROOWYRGBBGBBGWB

MOVE LOOKUP TABLE (sorted best-first; first entry is the best move):
  R  : OWGWWGWWGRRORROYBORGYGGYWYBBBRGYOORGYOGROOWYRYBBYBBWWB  [score=17]
  D  : OWYWWYWWBYRRBRRGWBRGRGGOOOOWYYBYRBGOYOGROOWYGGBBGBBWYR  [score=17]
  D2 : OWYWWYWWBYRRBRRWYRRGRGGOGWBYROYYGWBBYOGROOOOOGBBGBBWYG  [score=17]
  R' : OWRWWOWWGOBYORRORRRGWGGYWYYBBGGYGORGYOGROOWYRBBBYBBYWB  [score=15]
  R2 : OWWWWYWWYOOORRBRRYRGGGGGWYGBBYGYYORBYOGROOWYRGBBOBBRWB  [score=15]
  F  : OWYWWYROGWRRWRRBOOWGRYGGGOROBYGYYORYYOBROBWYWGBBGBBGWB  [score=15]
  L  : RWYGWYWWBYRRBRROOOBGRGGOOYGBBWBYYBRYGOROOYYRWGBWGBWGWO  [score=15]
  B' : WRYWWYWWBYROBRWOOYRGRGGOWYGBBWGYYORROOGROOYYRBBBBBWGGG  [score=15]
  F' : OWYWWYYBOWRRBRRBOOROGGGYRGWGORGYYORYYOBROWWYWGBBGBBGWB  [score=13]
  F2 : OWYWWYWBBRRRORRGOOGYWOGGRGRBWWGYYORYYOOROBWYYGBBGBBGWB  [score=13]
  L' : BWYBWYBWBYRRBRROOOOGRWGOWYGRBWGYYWRYWRYYOOROGGBOGBGGWB  [score=13]
  L2 : BWYGWYOWBYRRBRROOOBGRBGOBYGOBWWYYWRYRYWOORGOYGBWGBGGWR  [score=13]
  B  : RROWWYWWBYRYBRROOORGRGGOWYGBBWGYYYRWYOGWOOOYRGGGWBBBBB  [score=13]
  B2 : YROWWYWWBYRWBRROOYRGRGGOWYGBBWGYYYWOOOGROORYRBWGBBGBBG  [score=13]

SELECTION: In white_cross phase, check if any U/U'/U2 entry scores >= (current score - 2). If yes, pick the U-face move. Otherwise pick FIRST entry.
Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <chosen move token>
next_state = <54-char string copied from table before [score=>

---
