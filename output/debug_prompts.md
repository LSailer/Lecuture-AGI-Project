
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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

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
Current score: 3
Previous move: None
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


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
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


### User Prompt
Step: 2
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 5
Previous move: R'
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


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
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


### User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


---

## Fallback at Step 3, Retry 1

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your primary task is twofold:
1. Identify the *single best next move* from the 'Allowed moves' list to advance towards the specified 'Goal' for the current 'Phase'.
2. *Accurately compute the resulting cube state* after applying your chosen move, strictly following the provided permutation algorithm.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM - ADHERE STRICTLY):
1. Create a `next_state` string variable.
2. Initialize `next_state` by making an exact copy of `current_state` (all 54 characters). This is your starting point for modifications.
3. Look up the permutation table for your chosen move below.
4. For *each* "old_index→new_index" pair in the table:
   Set `next_state[new_index] = current_state[old_index]`.
   IMPORTANT: Always read the character from the *original current_state* string. Never read from the partially-built `next_state`.
5. Positions NOT listed in the table stay unchanged (due to step 2).
6. *Self-check*: After applying all permutations, quickly verify the calculated `next_state` for any obvious errors (e.g., character counts). Cube state calculations are prone to subtle mistakes.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Your final output MUST contain only two lines.
- The first line MUST be: move = <one move token>
- The second line MUST be: next_state = <54-character string>
- No additional text, explanations, or markdown (e.g., code blocks) are allowed.

### User Prompt
Your task is to select the most effective move from the 'Allowed moves' list to progress towards the 'Goal' of solving the Rubik's Cube. After selecting a move, meticulously calculate the 'next_state' using the provided permutation algorithm.

Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
      OOR
      GWB
      GYY
BRR WGG ORG YWW
YOR WGG ORW BBO
YOG ORW BBB YWO
      WYR
      BYY
      BGR

Think step-by-step to choose the optimal move and then apply the permutation table with extreme care. Double-check your calculation for next_state. Your final response must strictly adhere to the specified output format.

### Failed Predictions
- Agent 3:1: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:2: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:3: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:4: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:5: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:6: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:7: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:8: action=None, state=None, error=Inconsistent prediction: next_state does not match current_state + move.
- Agent 3:9: action=None, state=None, error=Could not find move or next_state in the response.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


## Original User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


## Failed Predictions
  - Agent 3:1: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:2: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:3: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:4: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:5: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:6: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:7: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:8: predicted action=None, predicted state=None, error=Inconsistent prediction: next_state does not match current_state + move.
  - Agent 3:9: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.

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
You are a highly precise Rubik's Cube solver assistant. Your primary task is twofold:
1. Identify the *single best next move* from the 'Allowed moves' list to advance towards the specified 'Goal' for the current 'Phase'.
2. *Accurately compute the resulting cube state* after applying your chosen move, strictly following the provided permutation algorithm.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM - ADHERE STRICTLY):
1. Create a `next_state` string variable.
2. Initialize `next_state` by making an exact copy of `current_state` (all 54 characters). This is your starting point for modifications.
3. Look up the permutation table for your chosen move below.
4. For *each* "old_index→new_index" pair in the table:
   Set `next_state[new_index] = current_state[old_index]`.
   IMPORTANT: Always read the character from the *original current_state* string. Never read from the partially-built `next_state`.
5. Positions NOT listed in the table stay unchanged (due to step 2).
6. *Self-check*: After applying all permutations, quickly verify the calculated `next_state` for any obvious errors (e.g., character counts). Cube state calculations are prone to subtle mistakes.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Your final output MUST contain only two lines.
- The first line MUST be: move = <one move token>
- The second line MUST be: next_state = <54-character string>
- No additional text, explanations, or markdown (e.g., code blocks) are allowed.
</SYSTEM_PROMPT>

<USER_PROMPT>
Your task is to select the most effective move from the 'Allowed moves' list to progress towards the 'Goal' of solving the Rubik's Cube. After selecting a move, meticulously calculate the 'next_state' using the provided permutation algorithm.

Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: {previous_move}
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
{current_state}
{state_visual}

Think step-by-step to choose the optimal move and then apply the permutation table with extreme care. Double-check your calculation for next_state. Your final response must strictly adhere to the specified output format.
</USER_PROMPT>

---

## Actual LLM Prompt at Step 3 (fallback)

### System Prompt
You are a highly precise Rubik's Cube solver assistant. Your primary task is twofold:
1. Identify the *single best next move* from the 'Allowed moves' list to advance towards the specified 'Goal' for the current 'Phase'.
2. *Accurately compute the resulting cube state* after applying your chosen move, strictly following the provided permutation algorithm.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM - ADHERE STRICTLY):
1. Create a `next_state` string variable.
2. Initialize `next_state` by making an exact copy of `current_state` (all 54 characters). This is your starting point for modifications.
3. Look up the permutation table for your chosen move below.
4. For *each* "old_index→new_index" pair in the table:
   Set `next_state[new_index] = current_state[old_index]`.
   IMPORTANT: Always read the character from the *original current_state* string. Never read from the partially-built `next_state`.
5. Positions NOT listed in the table stay unchanged (due to step 2).
6. *Self-check*: After applying all permutations, quickly verify the calculated `next_state` for any obvious errors (e.g., character counts). Cube state calculations are prone to subtle mistakes.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Your final output MUST contain only two lines.
- The first line MUST be: move = <one move token>
- The second line MUST be: next_state = <54-character string>
- No additional text, explanations, or markdown (e.g., code blocks) are allowed.

### User Prompt
Your task is to select the most effective move from the 'Allowed moves' list to progress towards the 'Goal' of solving the Rubik's Cube. After selecting a move, meticulously calculate the 'next_state' using the provided permutation algorithm.

Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
      OOR
      GWB
      GYY
BRR WGG ORG YWW
YOR WGG ORW BBO
YOG ORW BBB YWO
      WYR
      BYY
      BGR

Think step-by-step to choose the optimal move and then apply the permutation table with extreme care. Double-check your calculation for next_state. Your final response must strictly adhere to the specified output format.

---

## Fallback at Step 3, Retry 2

### System Prompt
YOUR SOLE AND STRICT TASK:
You MUST output your response in the EXACT FORMAT of two lines, and ONLY two lines.
Absolutely NO other text, explanations, markdown formatting (e.g., code blocks), or conversational elements are allowed.
1. The first line MUST be: move = <one move token>
2. The second line MUST be: next_state = <54-character string>

You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

### User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: {allowed_moves}

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Select the single best move from the 'Allowed moves' list to make progress towards the goal.
Then, using the provided permutation tables, compute the exact next state after applying your chosen move.

Output your chosen move and the computed next state by STRICTLY filling in this template, and NOTHING else:
move = <YOUR_CHOSEN_MOVE>
next_state = <THE_COMPUTED_54_CHARACTER_STRING>

### Failed Predictions
- Agent 3:1: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:2: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:3: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:4: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:5: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:6: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:7: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:8: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:9: action=None, state=None, error=Could not find move or next_state in the response.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


## Original User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


## Failed Predictions
  - Agent 3:1: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:2: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:3: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:4: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:5: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:6: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:7: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:8: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:9: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.

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
The agents failed because they did not adhere to the strict output format requirements, specifically producing exactly two lines: `move = <move_token>` and `next_state = <54-char_string>`. The error "Could not find move or next_state in the response" indicates a parsing failure, likely due to extraneous text, explanations, or incorrect formatting (e.g., markdown code blocks) in the agent's output. The `/no_think` directive might also have prevented agents from performing sufficient internal processing to accurately compute the next state, leading them to produce no output or malformed output rather than an incorrect state.

The improved prompts focus on:
1.  **Extreme Clarity and Prominence of Output Requirements:** The system prompt now starts with the strict output requirements, emphasizing that absolutely no other text or formatting is allowed.
2.  **Explicit Output Template:** The user prompt provides an exact template for the output, instructing the agent to fill it in directly.
3.  **Removing `/no_think`:** This allows the agent to potentially perform more internal reasoning steps to accurately compute the `next_state`, while the strict output format instructions should still prevent any internal thoughts from being output.

<SYSTEM_PROMPT>
YOUR SOLE AND STRICT TASK:
You MUST output your response in the EXACT FORMAT of two lines, and ONLY two lines.
Absolutely NO other text, explanations, markdown formatting (e.g., code blocks), or conversational elements are allowed.
1. The first line MUST be: move = <one move token>
2. The second line MUST be: next_state = <54-character string>

You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: {previous_move}
Allowed moves: {allowed_moves}

Current state:
{current_state}

Select the single best move from the 'Allowed moves' list to make progress towards the goal.
Then, using the provided permutation tables, compute the exact next state after applying your chosen move.

Output your chosen move and the computed next state by STRICTLY filling in this template, and NOTHING else:
move = <YOUR_CHOSEN_MOVE>
next_state = <THE_COMPUTED_54_CHARACTER_STRING>
</USER_PROMPT>

---

## Actual LLM Prompt at Step 3 (fallback)

### System Prompt
YOUR SOLE AND STRICT TASK:
You MUST output your response in the EXACT FORMAT of two lines, and ONLY two lines.
Absolutely NO other text, explanations, markdown formatting (e.g., code blocks), or conversational elements are allowed.
1. The first line MUST be: move = <one move token>
2. The second line MUST be: next_state = <54-character string>

You are a Rubik's Cube solver assistant.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

### User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: {allowed_moves}

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Select the single best move from the 'Allowed moves' list to make progress towards the goal.
Then, using the provided permutation tables, compute the exact next state after applying your chosen move.

Output your chosen move and the computed next state by STRICTLY filling in this template, and NOTHING else:
move = <YOUR_CHOSEN_MOVE>
next_state = <THE_COMPUTED_54_CHARACTER_STRING>

---

## Fallback at Step 3, Retry 3

### System Prompt
REQUIREMENTS (STRICT - Read FIRST and adhere to PRECISELY):
- Your entire response MUST consist of EXACTLY TWO LINES. No empty lines, no markdown (e.g., code blocks), no explanations, no reasoning, no preamble, no postamble.
- The FIRST line MUST be in the format: move = <one move token>
- The SECOND line MUST be in the format: next_state = <54-character string>
- The <one move token> must be a valid move from the 'Allowed moves' list provided in the user prompt.
- The <54-character string> must be the result of applying that chosen move to the current state, computed precisely using the MANDATORY ALGORITHM below.

You are a Rubik's Cube solver assistant. Your primary task is to choose an optimal move from the allowed list to progress towards the current puzzle goal, and then accurately compute the resulting cube state using the provided permutation tables.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2
Allowed moves: {allowed_moves}

Current cube state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

      OOR
      GWB
      GYY
BRR WGG ORG YWW
YOR WGG ORW BBO
YOG ORW BBB YWO
      WYR
      BYY
      BGR

Your task is to analyze the current state and the goal. Choose the single best move from the 'Allowed moves' list that you believe most effectively brings the cube closer to solving the '{phase}' goal.
Once you have chosen your move, apply it precisely to the 'Current cube state' using the permutation tables provided in your system prompt to calculate the exact 'next_state'.
Output your chosen move and the calculated next state. Remember the strict format requirements.

### Failed Predictions
- Agent 3:1: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:2: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:3: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:4: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:5: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:6: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:7: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:8: action=None, state=None, error=Could not find move or next_state in the response.
- Agent 3:9: action=None, state=None, error=Could not find move or next_state in the response.

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

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW
move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).


## Original User Prompt
Step: 3
Phase: white_cross
Goal: Solve the WHITE CROSS on the U face (white).
Current score: 7
Previous move: U2
Allowed moves: U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2

Current state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Use the permutation table for your chosen move to compute next_state.
Remember: output EXACTLY TWO LINES:
move = <...>
next_state = <...>
/no_think


## Failed Predictions
  - Agent 3:1: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:2: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:3: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:4: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:5: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:6: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:7: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:8: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.
  - Agent 3:9: predicted action=None, predicted state=None, error=Could not find move or next_state in the response.

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
REQUIREMENTS (STRICT - Read FIRST and adhere to PRECISELY):
- Your entire response MUST consist of EXACTLY TWO LINES. No empty lines, no markdown (e.g., code blocks), no explanations, no reasoning, no preamble, no postamble.
- The FIRST line MUST be in the format: move = <one move token>
- The SECOND line MUST be in the format: next_state = <54-character string>
- The <one move token> must be a valid move from the 'Allowed moves' list provided in the user prompt.
- The <54-character string> must be the result of applying that chosen move to the current state, computed precisely using the MANDATORY ALGORITHM below.

You are a Rubik's Cube solver assistant. Your primary task is to choose an optimal move from the allowed list to progress towards the current puzzle goal, and then accurately compute the resulting cube state using the provided permutation tables.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB
</SYSTEM_PROMPT>

<USER_PROMPT>
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: {previous_move}
Allowed moves: {allowed_moves}

Current cube state:
{current_state}

{state_visual}

Your task is to analyze the current state and the goal. Choose the single best move from the 'Allowed moves' list that you believe most effectively brings the cube closer to solving the '{phase}' goal.
Once you have chosen your move, apply it precisely to the 'Current cube state' using the permutation tables provided in your system prompt to calculate the exact 'next_state'.
Output your chosen move and the calculated next state. Remember the strict format requirements.
</USER_PROMPT>

---

## Actual LLM Prompt at Step 3 (fallback)

### System Prompt
REQUIREMENTS (STRICT - Read FIRST and adhere to PRECISELY):
- Your entire response MUST consist of EXACTLY TWO LINES. No empty lines, no markdown (e.g., code blocks), no explanations, no reasoning, no preamble, no postamble.
- The FIRST line MUST be in the format: move = <one move token>
- The SECOND line MUST be in the format: next_state = <54-character string>
- The <one move token> must be a valid move from the 'Allowed moves' list provided in the user prompt.
- The <54-character string> must be the result of applying that chosen move to the current state, computed precisely using the MANDATORY ALGORITHM below.

You are a Rubik's Cube solver assistant. Your primary task is to choose an optimal move from the allowed list to progress towards the current puzzle goal, and then accurately compute the resulting cube state using the provided permutation tables.

State encoding:
- The cube state is a SINGLE 54-character string over letters: W,R,G,Y,O,B.
- Face order is EXACTLY: U(0-8), R(9-17), F(18-26), D(27-35), L(36-44), B(45-53).
- Within each face indices are row-major:
  0 1 2
  3 4 5
  6 7 8
- IMPORTANT invariant: each letter W,R,G,Y,O,B must appear EXACTLY 9 times.

Reference solved state:
WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

HOW TO COMPUTE next_state (MANDATORY ALGORITHM):
1. Copy current_state character by character into next_state (all 54 positions).
2. Look up the permutation table for your chosen move below.
3. For each "old→new" pair: set next_state[new] = current_state[old].
   IMPORTANT: Always read from original current_state, never partially-built next_state.
4. Output next_state. Positions NOT listed in the table stay unchanged.

PERMUTATION TABLES (old_index → new_index; unlisted positions unchanged):
U:  0→6, 1→3, 2→0, 3→7, 5→1, 6→8, 7→5, 8→2, 9→45, 10→46, 11→47, 18→9, 19→10, 20→11, 36→18, 37→19, 38→20, 45→36, 46→37, 47→38
U': 0→2, 1→5, 2→8, 3→1, 5→7, 6→0, 7→3, 8→6, 9→18, 10→19, 11→20, 18→36, 19→37, 20→38, 36→45, 37→46, 38→47, 45→9, 46→10, 47→11
U2: 0→8, 1→7, 2→6, 3→5, 5→3, 6→2, 7→1, 8→0, 9→36, 10→37, 11→38, 18→45, 19→46, 20→47, 36→9, 37→10, 38→11, 45→18, 46→19, 47→20
R:  2→20, 5→23, 8→26, 9→15, 10→12, 11→9, 12→16, 14→10, 15→17, 16→14, 17→11, 20→29, 23→32, 26→35, 29→51, 32→48, 35→45, 45→8, 48→5, 51→2
R': 2→51, 5→48, 8→45, 9→11, 10→14, 11→17, 12→10, 14→16, 15→9, 16→12, 17→15, 20→2, 23→5, 26→8, 29→20, 32→23, 35→26, 45→35, 48→32, 51→29
R2: 2→29, 5→32, 8→35, 9→17, 10→16, 11→15, 12→14, 14→12, 15→11, 16→10, 17→9, 20→51, 23→48, 26→45, 29→2, 32→5, 35→8, 45→26, 48→23, 51→20
F:  6→9, 7→12, 8→15, 9→29, 12→28, 15→27, 18→20, 19→23, 20→26, 21→19, 23→25, 24→18, 25→21, 26→24, 27→38, 28→41, 29→44, 38→8, 41→7, 44→6
F': 6→44, 7→41, 8→38, 9→6, 12→7, 15→8, 18→24, 19→21, 20→18, 21→25, 23→19, 24→26, 25→23, 26→20, 27→15, 28→12, 29→9, 38→27, 41→28, 44→29
F2: 6→29, 7→28, 8→27, 9→44, 12→41, 15→38, 18→26, 19→25, 20→24, 21→23, 23→21, 24→20, 25→19, 26→18, 27→8, 28→7, 29→6, 38→15, 41→12, 44→9
D:  15→24, 16→25, 17→26, 24→42, 25→43, 26→44, 27→33, 28→30, 29→27, 30→34, 32→28, 33→35, 34→32, 35→29, 42→51, 43→52, 44→53, 51→15, 52→16, 53→17
D': 15→51, 16→52, 17→53, 24→15, 25→16, 26→17, 27→29, 28→32, 29→35, 30→28, 32→34, 33→27, 34→30, 35→33, 42→24, 43→25, 44→26, 51→42, 52→43, 53→44
D2: 15→42, 16→43, 17→44, 24→51, 25→52, 26→53, 27→35, 28→34, 29→33, 30→32, 32→30, 33→29, 34→28, 35→27, 42→15, 43→16, 44→17, 51→24, 52→25, 53→26
L:  0→53, 3→50, 6→47, 18→0, 21→3, 24→6, 27→18, 30→21, 33→24, 36→42, 37→39, 38→36, 39→43, 41→37, 42→44, 43→41, 44→38, 47→33, 50→30, 53→27
L': 0→18, 3→21, 6→24, 18→27, 21→30, 24→33, 27→53, 30→50, 33→47, 36→38, 37→41, 38→44, 39→37, 41→43, 42→36, 43→39, 44→42, 47→6, 50→3, 53→0
L2: 0→27, 3→30, 6→33, 18→53, 21→50, 24→47, 27→0, 30→3, 33→6, 36→44, 37→43, 38→42, 39→41, 41→39, 42→38, 43→37, 44→36, 47→24, 50→21, 53→18
B:  0→42, 1→39, 2→36, 11→0, 14→1, 17→2, 33→17, 34→14, 35→11, 36→33, 39→34, 42→35, 45→47, 46→50, 47→53, 48→46, 50→52, 51→45, 52→48, 53→51
B': 0→11, 1→14, 2→17, 11→35, 14→34, 17→33, 33→36, 34→39, 35→42, 36→2, 39→1, 42→0, 45→51, 46→48, 47→45, 48→52, 50→46, 51→53, 52→50, 53→47
B2: 0→35, 1→34, 2→33, 11→42, 14→39, 17→36, 33→2, 34→1, 35→0, 36→17, 39→14, 42→11, 45→53, 46→52, 47→51, 48→50, 50→48, 51→47, 52→46, 53→45

SOLUTION PATH EXAMPLES (10-move scramble R,U,R',U',F2,D,L,B',U2,R solved by R',U2,B,L',D',F2,U,R,U',R'):
Step 1:
current_state = YYYBWBROWRWBRRBBOBYWGWGGOROWYWBYGBGWORGYORYOGRGGYBORWO
move = R'
next_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO

Step 2:
current_state = YYGBWGROOBRRORWBBBYWWWGGORWWYRBYYBGRORGYORYOGWGGBBOYWO
move = U2
next_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

Step 3:
current_state = OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO
move = B
next_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW

Step 4:
current_state = GWBGWBGYYORRORGBBBWGGWGGORWWYRBYYBYYRRROOROOGYBYWBWOOW
move = L'
next_state = WWBWWBYYYORRORGBBBGGGGGGGRWWYRWYYOYYOOROORGRRYBBWBBOOW

Step 5:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

move = D'
next_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB

Step 6:
current_state = WWBWWBYYYORRORGGRWGGGGGGGRROWWYYYYYROOROOROOWYBBWBBBBB
move = F2
next_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB

Step 7:
current_state = WWBWWBWWOWRRRRGRRWRRGGGGGGGYYYYYYYYROOGOOOOOOYBBWBBBBB
move = U
next_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB

Step 8:
current_state = BBOWWWWWWRRGRRGRRWOOGGGGGGGYYYYYYYYRYBBOOOOOOWRRWBBBBB
move = R
next_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB

Step 9:
current_state = BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB

Step 10:
current_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
move = R'
next_state = WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

### User Prompt
Step: {step_number}
Phase: {phase}
Goal: {goal}
Current score: {current_score}
Previous move: U2
Allowed moves: {allowed_moves}

Current cube state:
OORGWBGYYORGORWBBBWGGWGGORWWYRBYYBGRBRRYORYOGYWWBBOYWO

      OOR
      GWB
      GYY
BRR WGG ORG YWW
YOR WGG ORW BBO
YOG ORW BBB YWO
      WYR
      BYY
      BGR

Your task is to analyze the current state and the goal. Choose the single best move from the 'Allowed moves' list that you believe most effectively brings the cube closer to solving the '{phase}' goal.
Once you have chosen your move, apply it precisely to the 'Current cube state' using the permutation tables provided in your system prompt to calculate the exact 'next_state'.
Output your chosen move and the calculated next state. Remember the strict format requirements.

---
