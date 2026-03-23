
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 1
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: None

Current state:
WYOOWRRWBRWBBRRWWOBGWOGYOGOGYGRYBRGWRBYWOGGYYYOGBBOBRY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R' : WYWOWYRWOWBRWRWORBBGGOGBOGWGYBRYBRGYRBYWOGGYYBOGRBOORY  [score=17]
  B2 : WGROWRRWBRWGBRWWWRBGWOGYOGOGYGRYBOYWOBYROGBYYYRBOBBGOY  [score=17]
  U2 : BWRRWOOYWRBYBRRWWOYOGOGYOGOGYGRYBRGWRWBWOGGYYBGWBBOBRY  [score=16]
  D  : WYOOWRRWBRWBBRRBRYBGWOGYWWOGBWYYGGRRRBYWOGOGOYOGBBOGYY  [score=16]
  L  : BYOOWROWBRWBBRRWWOGGWRGYRGOYYGOYBGGWYGYBOYRWGYORBBOBRW  [score=16]
  L2 : GYORWRRWBRWBBRRWWOYGWOGYGGOWYGOYBRGWYYGGOWYBRYOOBBOBRB  [score=16]
  U  : ORBYWWWORBGWBRRWWORBYOGYOGOGYGRYBRGWYOGWOGGYYRWBBBOBRY  [score=15]
  R  : WYBOWBRWYBROWRWRBWBGOOGROGBGYWRYYRGORBYWOGGYYWOGBBOGRY  [score=15]
  F' : WYOOWRRBWGWBYRRGWOWYOGGGBOOYGYRYBRGWRBBWOWGYRYOGBBOBRY  [score=15]
  B  : BROOWRRWBRWWBRGWWRBGWOGYOGOGYGRYBRWGOBYYOGWYYBBYRBOYOG  [score=15]
  U' : ROWWWYBROYOGBRRWWORWBOGYOGOGYGRYBRGWBGWWOGGYYRBYBBOBRY  [score=14]
  R2 : WYGOWBRWWOWWRRBBWRBGBOGBOGYGYORYRRGBRBYWOGGYYOOGYBOWRY  [score=14]
  D' : WYOOWRRWBRWBBRROGOBGWOGYGYYRRGGYYWBGRBYWOGBRYYOGBBOWWO  [score=14]
  D2 : WYOOWRRWBRWBBRRGYYBGWOGYBRYWGRBYRGYGRBYWOGWWOYOGBBOOGO  [score=14]
  L' : YYOOWRGWBRWBBRRWWOWGWOGYRGOBYGOYBOGWGWRYOBYGYYORBBRBRG  [score=14]
  B' : GWROWRRWBRWWBRYWWOBGWOGYOGOGYGRYBORBRBYGOGWYYGOYOBRYBB  [score=14]
  F  : WYOOWRYGYRWBWRRBWOOOBGGGOYWWBRRYBRGWRBGWOYGYGYOGBBOBRY  [score=13]
  F2 : WYOOWRGYGYWBGRRYWOOGOYGOWGBBWRRYBRGWRBWWOBGYRYOGBBOBRY  [score=12]

Algorithm: step 1 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 2
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: R

Current state:
WYBOWBRWYBROWRWRBWBGOOGROGBGYWRYYRGORBYWOGGYYWOGBBOGRY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U2 : YWRBWOBYWRBYWRWRBWWOGOGROGBGYWRYYRGOBROWOGGYYBGOBBOGRY  [score=17]
  R2 : WYWOWYRWOWBRWRWORBBGGOGBOGWGYBRYBRGYRBYWOGGYYBOGRBOORY  [score=17]
  B  : OWWOWBRWYBROWRGRBRBGOOGROGBGYWRYYRWGBBYYOGWYYGBWRBOYOG  [score=17]
  B2 : OGROWBRWYBRGWRWRBRBGOOGROGBGYWRYYBYWWBYWOGOYYYRGOBBGOW  [score=17]
  L  : BYBOWBOWYBROWRWRBWGGORGRRGBYYWOYYGGOYGYBOYRWGWORBBOGRW  [score=16]
  L2 : GYBRWBRWYBROWRWRBWYGOOGRGGBWYWOYYRGOYYGGOWYBRWOOBBOGRB  [score=16]
  B' : GWROWBRWYBRWWRYRBBBGOOGROGBGYWRYYWWORBYGOGOYYGOYOBRWBG  [score=16]
  U  : BBYYWWWORBGOWRWRBWRBYOGROGBGYWRYYRGOWOGWOGGYYBROBBOGRY  [score=15]
  U' : ROWWWYYBBWOGWRWRBWBROOGROGBGYWRYYRGOBGOWOGGYYRBYBBOGRY  [score=15]
  F' : WYBOWBBWRWROYRWGBWORBGGGBOOYGYRYYRGORBYWOWGYRWOGBBOGRY  [score=15]
  D  : WYBOWBRWYBROWRWGRYBGOOGRRBWWYOYYGGRRRBYWOGOGBWOGBBOGYY  [score=15]
  D' : WYBOWBRWYBROWRWOGBBGOOGRGYYRRGGYYOYWRBYWOGGRYWOGBBORBW  [score=15]
  D2 : WYBOWBRWYBROWRWGYYBGOOGRGRYOGRYYRWYGRBYWOGRBWWOGBBOOGB  [score=15]
  R  : WYGOWBRWWOWWRRBBWRBGBOGBOGYGYORYRRGBRBYWOGGYYOOGYBOWRY  [score=14]
  F2 : WYBOWBWYGYROGRWYBWBGORGOOGBYWRRYYRGORBRWOWGYBWOGBBOGRY  [score=14]
  L' : YYBOWBGWYBROWRWRBWWGOOGRRGBBYWOYYOGOGWRYOBYGYWORBBRGRG  [score=14]
  F  : WYBOWBYGYRROWRWYBWOOBGGGBRORWBRYYRGORBGWOYGYWWOGBBOGRY  [score=13]

Algorithm: step 2 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 3
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: U2

Current state:
YWRBWOBYWRBYWRWRBWWOGOGROGBGYWRYYRGOBROWOGGYYBGOBBOGRY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : WWROWOOYWRBYWRWRBWGOGRGRRGBYYWOYYOGOOGYROYBWGBGBBBBGRY  [score=22]
  B' : GWBBWOBYWRBYWRWRBRWOGOGROGBGYWRYYWWYRROGOGOYYOOYGBRBBG  [score=20]
  B  : YWWBWOBYWRBOWRGRBRWOGOGROGBGYWRYYBWGRROWOGYYYGBBRBGYOO  [score=19]
  L2 : GWRRWORYWRBYWRWRBWYOGOGROGBYYWBYYBGOYYGGOWORBBGOBBOGRW  [score=18]
  D  : YWRBWOBYWRBYWRWGRYWOGOGRRBWWYOYYGGRRBROWOGOGBBGOBBOGYY  [score=17]
  D' : YWRBWOBYWRBYWRWOGBWOGOGRGYYRRGGYYOYWBROWOGGRYBGOBBORBW  [score=17]
  D2 : YWRBWOBYWRBYWRWGYYWOGOGRGRYOGRYYRWYGBROWOGRBWBGOBBOOGB  [score=17]
  L' : YWROWOOYWRBYWRWRBWYOGBGRBGBWYWOYYOGOGWBYORYGOBGRBBRGRG  [score=17]
  B2 : OGRBWOBYWRBGWRWRBBWOGOGROGBGYWRYYRWYWROWOGYYYYRGOBBOGB  [score=17]
  U  : ROWWWYYBBWOGWRWRBWBROOGROGBGYWRYYRGOBGOWOGGYYRBYBBOGRY  [score=15]
  U' : BBYYWWWORBGOWRWRBWRBYOGROGBGYWRYYRGOWOGWOGGYYBROBBOGRY  [score=15]
  R2 : YWWBWYBYOWBRWRWYBRWOGOGBOGBGYRRYORGWBROWOGGYYBGORBOGRY  [score=15]
  F' : YWRBWORWRWBYYRWGBWGRBOGGWOOOGYRYYRGOBRWWOYGYBBGOBBOGRY  [score=14]
  F2 : YWRBWOWYGYBYGRWOBWBGORGOGOWWYBRYYRGOBRRWOWGYRBGOBBOGRY  [score=14]
  R  : YWGBWBBYBYWWBRBRWRWOROGOOGWGYGRYRRGBBROWOGGYYOGOYBOWRY  [score=12]
  R' : YWGBWRBYBRWRBRBWWYWOWOGYOGOGYGRYBRGBBROWOGGYYWGOOBORRY  [score=12]
  F  : YWRBWOYGOBBYYRWWBWOOWGGOBRGRWRRYYRGOBRGWOYGYWBGOBBOGRY  [score=12]

Algorithm: step 3 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 4
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: D'

Current state:
YWRBWOBYWRBYWRWOGBWOGOGRGYYRRGGYYOYWBROWOGGRYBGOBBORBW

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : WWROWOGYWRBYWRWOGBROGGGROYYWRGOYYOYWOGYRORBWGBGBBBBRBY  [score=20]
  B' : GWBBWOBYWRBYWRWOGRWOGOGRGYYRRGGYYBWYOROYOGWRYOOWGBBBBR  [score=19]
  F' : YWRBWORWOGBYRRWRGBGRYOGYWOGOGYGYYOYWBRWWOYGRBBGOBBORBW  [score=18]
  D' : YWRBWOBYWRBYWRWGYYWOGOGRGRYOGRYYRWYGBROWOGRBWBGOBBOOGB  [score=17]
  D2 : YWRBWOBYWRBYWRWGRYWOGOGRRBWWYOYYGGRRBROWOGOGBBGOBBOGYY  [score=17]
  L' : WWROWOOYWRBYWRWOGBYOGBGRBYYWRGOYYGYWGWBRORYGOBGOBBGRBR  [score=17]
  L2 : RWRGWOOYWRBYWRWOGBWOGOGROYYYRGBYYBYWYRGGOWORBBGGBBORBW  [score=17]
  B2 : WYOBWOBYWRBGWRWOGBWOGOGRGYYRRGGYYRWYBROWOGYRYWBROBBOGB  [score=17]
  F2 : YWRBWOGRRYBYGRWOGBYYGRGOGOWWYBGYYOYWBROWOWGRRBGOBBORBW  [score=16]
  B  : YWBBWOBYWRBWWRYOGOWOGOGRGYYRRGGYYBWGRROWOGYRYRBBBBGWOO  [score=16]
  U  : ROWWWYYBBWOGWRWOGBBROOGRGYYRRGGYYOYWBGOWOGGRYRBYBBORBW  [score=15]
  U' : BBYYWWWORBGOWRWOGBRBYOGRGYYRRGGYYOYWWOGWOGGRYBROBBORBW  [score=15]
  U2 : WYBOWBRWYBROWRWOGBBGOOGRGYYRRGGYYOYWRBYWOGGRYWOGBBORBW  [score=15]
  F  : YWRBWOYGOBBYYRWWGBGOWYGOYRGOWRGYYOYWBRRWORGRGBGOBBORBW  [score=14]
  R  : YWRBWBBYBYWBBRGRWOWOROGOGYWRRGGYROYYBROWOGGRYWGOYBOGBW  [score=13]
  R' : YWGBWRBYYOWRGRBBWYWOGOGYGYWRRRGYBOYBBROWOGGRYWGOOBORBW  [score=13]
  R2 : YWGBWYBYWBGOWRWYBRWOROGBGYBRRRGYOOYWBROWOGGRYYGORBOGBW  [score=13]

Algorithm: step 4 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 5
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 19
Previous move: B'

Current state:
GWBBWOBYWRBYWRWOGRWOGOGRGYYRRGGYYBWYOROYOGWRYOOWGBBBBR

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : WWBOWOGYWRBYWRWOGRROGGGRBYYRRGBYYWWYOGYROROYWOOBGBBBBG  [score=21]
  F' : GWBBWORWOGBYRRWRGRGRYOGYWOGOGYGYYBWYORWYOYWRBOOWGBBBBR  [score=20]
  L' : RWBBWOWYWRBYWRWOGRGOGBGRBYYWRGOYYGWYWYORORYGOOOBGBGBBR  [score=20]
  U  : BOWWWYGBBWOGWRWOGROROOGRGYYRRGGYYBWYOOWYOGWRYRBYGBBBBR  [score=18]
  F2 : GWBBWOGRRYBYGRWOGRYYGRGOGOWWYBGYYBWYOROYOWWRROOWGBBBBR  [score=18]
  D  : GWBBWOBYWRBYWRWBBRWOGOGROGRGYYRYWRGBOROYOGGYYOOWGBBWRY  [score=17]
  D2 : GWBBWOBYWRBYWRWWRYWOGOGRBBRYWBYYGGRROROYOGOGROOWGBBGYY  [score=17]
  L2 : RWBGWOBYWRBYWRWOGRROGBGRWYYGRGBYYBWYYRWGOYOROOOGGBOBBW  [score=17]
  B' : WYOBWOBYWRBGWRWOGBWOGOGRGYYRRGGYYRWYBROWOGYRYWBROBBOGB  [score=17]
  U' : BBGYWWWOBOOWWRWOGRRBYOGRGYYRRGGYYBWYWOGYOGWRYOROGBBBBR  [score=16]
  U2 : WYBOWBBWGOROWRWOGROOWOGRGYYRRGGYYBWYRBYYOGWRYWOGGBBBBR  [score=16]
  R' : GWGBWRBYYOWRGRBRWYWOGOGYGYYRRBGYGBWOOROYOGWRYWOWOBBBBR  [score=16]
  F  : GWBBWOYGOBBYYRWWGRGOWYGOYRGOWRGYYBWYORRYORWRGOOWGBBBBR  [score=16]
  B2 : YWBBWOBYWRBWWRYOGOWOGOGRGYYRRGGYYBWGRROWOGYRYRBBBBGWOO  [score=16]
  R  : GWBBWGBYOYWRBRGRWOWOBOGOGYWRRGGYRBWYOROYOGWRYYOWYBBGBR  [score=15]
  R2 : GWGBWYBYYRGOWRWYBRWOBOGGGYORRBGYOBWWOROYOGWRYYOWRBBGBR  [score=15]
  D' : GWBBWOBYWRBYWRWGYYWOGOGRWRYBGRWYRYYGOROYOGBBROOWGBBOGR  [score=15]

Algorithm: step 5 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 6
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: L2

Current state:
RWBGWOBYWRBYWRWOGRROGBGRWYYGRGBYYBWYYRWGOYOROOOGGBOBBW

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L' : WWBOWOGYWRBYWRWOGRROGGGRBYYRRGBYYWWYOGYROROYWOOBGBBBBG  [score=21]
  L  : RWBBWOWYWRBYWRWOGRGOGBGRBYYWRGOYYGWYWYORORYGOOOBGBGBBR  [score=20]
  U  : BOWWWYRGBROGWRWOGRYRWBGRWYYGRGBYYBWYOOGGOYORORBYGBOBBW  [score=19]
  U2 : WYBOWGBWRYRWWRWOGROOGBGRWYYGRGBYYBWYRBYGOYOROROGGBOBBW  [score=17]
  F' : RWBGWORWOGBYRRWGGRGRYOGYRBWWYOBYYBWYYRWGOYORBOOGGBOBBW  [score=17]
  U' : BGRYWWWOBOOGWRWOGRRBYBGRWYYGRGBYYBWYROGGOYOROYRWGBOBBW  [score=16]
  F2 : RWBGWOGRGOBYYRWWGRYYWRGBGORWYBBYYBWYYROGOWORROOGGBOBBW  [score=16]
  F  : RWBGWOOYWBBYYRWWGRWBRYGOYRGOWRBYYBWYYRGGORORGOOGGBOBBW  [score=15]
  B  : YWRGWOBYWRBYWRWOGBROGBGRWYYGRGBYYYGOBRWWOYRROBGOBBOWOG  [score=15]
  B' : OGYGWOBYWRBRWRWOGBROGBGRWYYGRGBYYRWYBRWWOYYROGOWOBBOGB  [score=15]
  R' : RWGGWRBYYOWRGRBRWYROGBGYWYYGRBBYGBWOYRWGOYOROWOGOBOBBW  [score=14]
  D2 : RWBGWOBYWRBYWRWOROROGBGRBBWYWBYYBGRGYRWGOYOGROOGGBOWYY  [score=14]
  B2 : YWBGWOBYWRBOWRGOGYROGBGRWYYGRGBYYBWRRRWWOYYROWBBOBGGOO  [score=14]
  R  : RWBGWGBYOYWRBRGRWOROBBGOWYWGRGBYRBWYYRWGOYOROYOGYBOGBW  [score=13]
  R2 : RWGGWYBYYRGOWRWYBRROBBGGWYOGRBBYOBWWYRWGOYOROYOGRBOGBW  [score=13]
  D  : RWBGWOBYWRBYWRWBBWROGBGROGRGYYRYWGBBYRWGOYWYYOOGGBOORO  [score=13]
  D' : RWBGWOBYWRBYWRWWYYROGBGROROBBGWYRYYGYRWGOYBBWOOGGBOOGR  [score=12]

Algorithm: step 6 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 7
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 19
Previous move: U

Current state:
BOWWWYRGBROGWRWOGRYRWBGRWYYGRGBYYBWYOOGGOYORORBYGBOBBW

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : YOWBWYWGBROGWRWOGRGRWBGRBYYWRGOYYYWYGYOOOROGORBRGBWBBB  [score=22]
  L' : WOWOWYYGBROGWRWOGRBRWWGRRYYYRGBYYWWYOGOROOOYGRBBGBBBBG  [score=22]
  F' : BOWWWYRWOGOGRRWGGRWRYRGYYBWGYOBYYBWYOOBGOGORRRBYGBOBBW  [score=20]
  L2 : GOWBWYBGBROGWRWOGRWRWOGRYYYBRGWYYRWYOROYOGGOORBWGBBBBY  [score=19]
  R' : BOWWWRRGYOWRGRORWGYRGBGYWYYGRBBYGBWROOGGOYOROBBYYBOWBW  [score=18]
  F  : BOWWWYOYGROGGRWBGRWBYYGRYRWOWRBYYBWYOOGGORORGRBYGBOBBW  [score=18]
  F2 : BOWWWYGRGOOGYRWGGRYYWRGBWRYBGRBYYBWYOOOGOWORRRBYGBOBBW  [score=18]
  U  : WYBOWGBWRYRWWRWOGROOGBGRWYYGRGBYYBWYRBYGOYOROROGGBOBBW  [score=17]
  R2 : BOGWWYRGYRGOWRWGORYRBBGGWYRGRWBYYBWBOOGGOYOROYBYRBOWBW  [score=17]
  U2 : BGRYWWWOBOOGWRWOGRRBYBGRWYYGRGBYYBWYROGGOYOROYRWGBOBBW  [score=16]
  R  : BOBWWGRGRGWRORGRWOYRWBGYWYBGRWBYRBWYOOGGOYOROYBYYBOGBW  [score=16]
  D2 : BOWWWYRGBROGWRWOROYRWBGRBBWYWBYYBGRGOOGGOYOGRRBYGBOWYY  [score=16]
  B  : GWRWWYRGBROYWRWOGBYRWBGRWYYGRGBYYOGOWOGOOYBROBGRBBBWOY  [score=16]
  D  : BOWWWYRGBROGWRWBBWYRWBGROGRGYYRYWGBBOOGGOYWYYRBYGBOORO  [score=15]
  B2 : YWBWWYRGBROOWRGOGOYRWBGRWYYGRGBYYWOBROGWOYGROWBBOBGYBR  [score=15]
  D' : BOWWWYRGBROGWRWWYYYRWBGROROBBGWYRYYGOOGGOYBBWRBYGBOOGR  [score=14]
  B' : OGOWWYRGBROBWROOGWYRWBGRWYYGRGBYYRWGBOGWOYYROYOWBBBRGB  [score=14]

Algorithm: step 7 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 8
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 16
Previous move: B

Current state:
GWRWWYRGBROYWRWOGBYRWBGRWYYGRGBYYOGOWOGOOYBROBGRBBBWOY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : GWRWWYRWOGOYRRWGGBWRYRGYYBWGYOBYYOGOWOBOOGBRRBGRBBBWOY  [score=17]
  D  : GWRWWYRGBROYWRWWOYYRWBGROGBGYORYGGBOWOGOOYWYYBGRBBBBRO  [score=17]
  D' : GWRWWYRGBROYWRWWYYYRWBGRBROOBGGYROYGWOGOOYWOYBGRBBBOGB  [score=17]
  D2 : GWRWWYRGBROYWRWBROYRWBGRWOYOGOYYBGRGWOGOOYOGBBGRBBBWYY  [score=17]
  L  : YWRBWYWGBROYWRWOGBGRWBGROYYYRGBYYRGOGYOOORWOBBGRBBWWOG  [score=17]
  L' : YWRBWYRGBROYWRWOGBGRWWGRRYYYRGBYYWGOBOWROOOYGBGOBBBWOG  [score=17]
  R' : GWWWWRRGYOWRGROBWYYRGBGYWYOGRWBYBOGBWOGOOYBROBGRYBBROY  [score=16]
  U  : RYBWWGGWRYRWWRWOGBWOGBGRWYYGRGBYYOGOBGROOYBROROYBBBWOY  [score=15]
  U2 : BGRYWWRWGWOGWRWOGBBGRBGRWYYGRGBYYOGOROYOOYBROYRWBBBWOY  [score=15]
  R  : GWWWWBRGBYWBORGRWOYRRBGYWYBGRWBYROGYWOGOOYBROOGRYBBGOY  [score=15]
  F  : GWRWWYOYGROYGRWBGBWBYYGRYRWOWRBYYOGOWOGOORBRGBGRBBBWOY  [score=15]
  F2 : GWRWWYGRGOOYYRWGGBYYWRGBWRYBGRBYYOGOWOOOOWBRRBGRBBBWOY  [score=15]
  L2 : GWRBWYOGBROYWRWOGBYRWBGRRYYGRGWYYRGOORBYOOGOWBGWBBBWOY  [score=15]
  B  : YWBWWYRGBROOWRGOGOYRWBGRWYYGRGBYYWOBROGWOYGROWBBOBGYBR  [score=15]
  U' : RWGGWWBYRBGRWRWOGBROYBGRWYYGRGBYYOGOYRWOOYBROWOGBBBWOY  [score=14]
  R2 : GWGWWYRGOBGOWRWYORYRWBGBWYBGRRBYYOGBWOGOOYBROYGRRBBWOY  [score=14]
  B2 : OGOWWYRGBROBWROOGWYRWBGRWYYGRGBYYRWGBOGWOYYROYOWBBBRGB  [score=14]

Algorithm: step 8 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 9
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: D'

Current state:
GWRWWYRGBROYWRWWYYYRWBGRBROOBGGYROYGWOGOOYWOYBGRBBBOGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : GWRWWYRWWGOYBRWOYYWRORGRYBBGYYGYROYGWOBOOGWORBGRBBBOGB  [score=20]
  B' : WOWWWYRGBROGWRWWYRYRWBGRBROOBGGYRYWYOOGYOYGOYRBBGBGBBO  [score=20]
  R' : GWWWWRRGOWWRYROYWYYRGBGRBRGOBOGYBOYBWOGOOYWOYBGRYBBRGB  [score=19]
  F  : GWRWWYYYGROYGRWBYYBBYRGRORWWWRGYROYGWOOOOBWOGBGRBBBOGB  [score=18]
  D' : GWRWWYRGBROYWRWBROYRWBGRWOYOGOYYBGRGWOGOOYOGBBGRBBBWYY  [score=17]
  D2 : GWRWWYRGBROYWRWWOYYRWBGROGBGYORYGGBOWOGOOYWYYBGRBBBBRO  [score=17]
  U  : RYBWWGGWRYRWWRWWYYWOGBGRBROOBGGYROYGBGROOYWOYROYBBBOGB  [score=16]
  U2 : BGRYWWRWGWOGWRWWYYBGRBGRBROOBGGYROYGROYOOYWOYYRWBBBOGB  [score=16]
  R2 : GWGWWRRGGYYWWRWYORYROBGBBRBOBRGYYOYBWOGOOYWOYOGRRBBWGB  [score=16]
  F2 : GWRWWYGBOYOYYRWGYYORBRGBWRYBGRGYROYGWOWOOWWORBGRBBBOGB  [score=16]
  L' : BWRBWYRGBROYWRWWYYGRWWGRRROYBGBYRBYGWOWOOOYYGBGOBBGOGO  [score=16]
  L2 : OWRGWYOGBROYWRWWYYBRWBGRRROGBGWYRRYGYOWYOOGOWBGBBBBOGY  [score=16]
  U' : RWGGWWBYRBGRWRWWYYROYBGRBROOBGGYROYGYRWOOYWOYWOGBBBOGB  [score=15]
  R  : GWOWWBRGBYWYORYRWWYRRBGYBRBOBWGYROYOWOGOOYWOYGGRRBBGGB  [score=15]
  L  : YWRBWYBGBROYWRWWYYORWGGROROBBGBYRRYGGYYOOOWOWBGRBBWOGG  [score=15]
  B  : YWYWWYRGBROGWRYWYOYRWBGRBROOBGGYRWOWROGWOYGOYOBBGBGBBR  [score=15]
  B2 : GYOWWYRGBROWWROWYWYRWBGRBROOBGGYRRWGYOGWOYYOYBGOBBBRGB  [score=14]

Algorithm: step 9 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 10
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 19
Previous move: R'

Current state:
GWWWWRRGOWWRYROYWYYRGBGRBRGOBOGYBOYBWOGOOYWOYBGRYBBRGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F  : GWWWWRYYGRWRGROOWYBBYRGRGRGYYWGYBOYBWOOOOBWOOBGRYBBRGB  [score=24]
  F' : GWWWWRWYYOWRBROOWYGRGRGRYBBGYYGYBOYBWOOOOGWORBGRYBBRGB  [score=23]
  F2 : GWWWWROBOYWRYROGWYGRBRGBGRYOGRGYBOYBWOYOOYWOWBGRYBBRGB  [score=19]
  D2 : GWWWWRRGOWWRYROWOYYRGBGRRGBBYOBYGOBOWOGOOYYWYBGRYBBBRG  [score=18]
  L' : BWWBWRRGOWWRYROYWYGRGWGRRRGYBOBYBBYBWOWOOOYYGBGOYBGRGO  [score=18]
  L2 : OWWGWROGOWWRYROYWYBRGBGRRRGGBOWYBRYBYOWYOOGOWBGBYBBRGY  [score=18]
  B' : WOWWWRRGOWWGYRWYWWYRGBGRBRGOBOGYBYOROOGYOYBOYRBBGBGBYR  [score=18]
  U  : WROWWGGWRYRGYROYWYWOGBGRBRGOBOGYBOYBBGROOYWOYWWRYBBRGB  [score=17]
  D  : GWWWWRRGOWWRYRORGBYRGBGRYWYOBBBYYOGOWOGOOYBRGBGRYBBWOY  [score=17]
  D' : GWWWWRRGOWWRYROBRGYRGBGRWOYOGOYYBBBOWOGOOYRGBBGRYBBYWY  [score=17]
  L  : YWWBWRBGOWWRYROYWYORGGGRORGBBOBYBRYBGYYOOOWOWBGRYBWRGG  [score=17]
  U' : RWGGWWORWBGRYROYWYWWRBGRBRGOBOGYBOYBYRGOOYWOYWOGYBBRGB  [score=16]
  U2 : OGRRWWWWGWOGYROYWYBGRBGRBRGOBOGYBOYBWWROOYWOYYRGYBBRGB  [score=16]
  R' : GWGWWRRGGYYWWRWYORYROBGBBRBOBRGYYOYBWOGOOYWOYOGRRBBWGB  [score=16]
  R2 : GWOWWBRGBYWYORYRWWYRRBGYBRBOBWGYROYOWOGOOYWOYGGRRBBGGB  [score=15]
  B2 : BYOWWRRGOWWWYROYWWYRGBGRBRGOBOGYBWWGYOGOOYROYBGRBBYRGB  [score=15]
  B  : ROYWWRRGOWWBYRYYWOYRGBGRBRGOBOGYBWOWWOGWOYGOYRYBGBGBBR  [score=14]

Algorithm: step 10 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 11
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 16
Previous move: U2

Current state:
OGRRWWWWGWOGYROYWYBGRBGRBRGOBOGYBOYBWWROOYWOYYRGYBBRGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  B' : WOWRWWWWGWOOYRGYWRBGRBGRBRGOBOGYBYOGOWRYOYBOYGBBRBGYYR  [score=19]
  F  : OGRRWWYYRWOGWROGWYBBBRGGGRRYYWGYBOYBWWOOOBWOOYRGYBBRGB  [score=18]
  U' : WROWWGGWRYRGYROYWYWOGBGRBRGOBOGYBOYBBGROOYWOYWWRYBBRGB  [score=17]
  R  : OGRRWYWWYGOYORWWYYBGRBGWBRGOBRGYROYGWWROOYWOYBRGBBBOGB  [score=17]
  F' : OGRRWWWYYOOGBROOWYRRGGGRBBBRYYGYBOYBWWGOOWWOWYRGYBBRGB  [score=17]
  L2 : OGRGWWOWGWOGYROYWYBGRBGRGRGOBORYBWYBYOWYOORWWYRBYBBRGB  [score=17]
  U  : RWGGWWORWBGRYROYWYWWRBGRBRGOBOGYBOYBYRGOOYWOYWOGYBBRGB  [score=16]
  R' : OGRRWRWWGYYWWROYOGBGOBGBBRBOBRGYYOYYWWROOYWOYGRGWBBRGB  [score=16]
  F2 : OGRRWWOBOYOGYRORWYGRBRGBRGBGWWGYBOYBWWYOOYWOWYRGYBBRGB  [score=15]
  D2 : OGRRWWWWGWOGYROWOYBGRBGRRGBBYOBYGOBOWWROOYYWYYRGYBBBRG  [score=15]
  B  : GOYRWWWWGWOBYRYYWOBGRBGRBRGOBOGYBWOWRWRGOYOOYRYYGBRBBG  [score=15]
  B2 : BYORWWWWGWOWYROYWWBGRBGRBRGOBOGYBRGOYWROOYGOYBGRBBYGRY  [score=15]
  R2 : OGORWBWWBYWYORYGOWBGRBGYBRYOBRGYWOYGWWROOYWOYGRGRBBRGB  [score=14]
  D  : OGRRWWWWGWOGYRORGBBGRBGRYWYOBBBYYOGOWWROOYBRGYRGYBBWOY  [score=14]
  D' : OGRRWWWWGWOGYROBRGBGRBGRWOYOGOYYBBBOWWROOYRGBYRGYBBYWY  [score=14]
  L  : BGRBWWBWGWOGYROYWYOGRGGRORGBBOBYBGYBRYYWOOWOWYRWYBRRGO  [score=14]
  L' : BGRBWWGWGWOGYROYWYOGRRGRWRGBBOBYBBYBWOWOOWYYRYROYBGRGO  [score=13]

Algorithm: step 11 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 12
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: B

Current state:
GOYRWWWWGWOBYRYYWOBGRBGRBRGOBOGYBWOWRWRGOYOOYRYYGBRBBG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L2 : OOYGWWWWGWOBYRYYWOGGRRGRYRGGBORYBWOWYOOYOGRWRRYBGBBBBB  [score=19]
  B2 : WOWRWWWWGWOOYRGYWRBGRBGRBRGOBOGYBYOGOWRYOYBOYGBBRBGYYR  [score=19]
  U2 : GWWWWRYOGRWRYRYYWORYYBGRBRGOBOGYBWOWWOBGOYOOYBGRGBRBBG  [score=18]
  F  : GOYRWWYYRWOBWRYGWOBBBRGGGRRYYWGYBWOWRWOGOBOOORYYGBRBBG  [score=17]
  U  : YWGOWWGRWBGRYRYYWORWRBGRBRGOBOGYBWOWRYYGOYOOYWOBGBRBBG  [score=16]
  F' : GOYRWWWYYOOBBRYOWORRGGGRBBBRYYGYBWOWRWGGOWOOWRYYGBRBBG  [score=16]
  L  : BOYBWWBWGWOBYRYYWOOGRGGRWRGGBORYBYOWRYYWOORGORYWGBRBBG  [score=16]
  U' : WRGWWOGWYRYYYRYYWOWOBBGRBRGOBOGYBWOWBGRGOYOOYRWRGBRBBG  [score=15]
  R2 : GOORWBWWWOWYYRYBOWBGBBGGBRROBYGYWWOGRWRGOYOOYGYYRBRRBG  [score=15]
  L' : GOYRWWYWGWOBYRYYWOGGRRGRWRGBBOBYBBOWOGROOWYYRRYWGBGBBO  [score=15]
  B  : BYORWWWWGWOWYROYWWBGRBGRBRGOBOGYBRGOYWROOYGOYBGRBBYGRY  [score=15]
  R  : GOBRWGWWRBYOORWWYYBGYBGWBRGOBRGYRWOGRWRGOYOOYWYYBBROBG  [score=14]
  F2 : GOYRWWOBOYOBYRYRWOGRBRGBRGBGWWGYBWOWRWYGOYOOWRYYGBRBBG  [score=14]
  D2 : GOYRWWWWGWOBYRYOOYBGRBGRBBGWOWBYGOBORWRGOYYWORYYGBRBRG  [score=13]
  R' : GORRWRWWGYYWWROOYBBGOBGBBRWOBBGYGWORRWRGOYOOYGYYWBRYBG  [score=12]
  D' : GOYRWWWWGWOBYRYBRGBGRBGROOYWGOOYBWBORWRGOYBBGRYYGBRYWO  [score=11]
  D  : GOYRWWWWGWOBYRYBBGBGRBGRYWOOBWBYOOGWRWRGOYBRGRYYGBROOY  [score=10]

Algorithm: step 12 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 13
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: L'

Current state:
GOYRWWYWGWOBYRYYWOGGRRGRWRGBBOBYBBOWOGROOWYYRRYWGBGBBO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L' : OOYGWWWWGWOBYRYYWOGGRRGRYRGGBORYBWOWYOOYOGRWRRYBGBBBBB  [score=19]
  F  : GOYRWWRWRYOBWRYGWOWRGRGGGRRYYWBYBBOWOGBOOBYYORYWGBGBBO  [score=18]
  F2 : GOYRWWOBBROBWRYRWOGRWRGRRGGGWYBYBBOWOGYOOYYYWRYWGBGBBO  [score=17]
  L2 : BOYBWWBWGWOBYRYYWOOGRGGRWRGGBORYBYOWRYYWOORGORYWGBRBBG  [score=16]
  B2 : WOBRWWYWGWOYYROYWOGGRRGRWRGBBOBYBYOGOGRYOWBYROBBGBGWYR  [score=16]
  U  : YWGOWWGRYGGRYRYYWOOGRRGRWRGBBOBYBBOWRYWOOWYYRWOBGBGBBO  [score=15]
  R2 : GOORWBYWWOWYYRYBOWGGBRGGWRRBBYBYWBOGOGROOWYYRGYWRBGRBO  [score=15]
  F' : GOYRWWWYYOOBBRYBWORRGGGRGRWRWRBYBBOWOGGOOWYYYRYWGBGBBO  [score=15]
  B  : BYORWWYWGWOWYROYWBGGRRGRWRGBBOBYBOOYYGROOWGYRBGRBBYOGW  [score=15]
  B' : YOORWWYWGWOGYROYWYGGRRGRWRGBBOBYBOYBBGROOWWYRWGOYBBRGB  [score=15]
  U2 : GWYWWRYOGOGRYRYYWORYWRGRWRGBBOBYBBOWWOBOOWYYRGGRGBGBBO  [score=14]
  R  : GOBRWGYWRBYOORWWYYGGYRGWWRGBBRBYRBOGOGROOWYYRWYWBBGOBO  [score=14]
  D' : GOYRWWYWGWOBYRYWRGGGRRGRYYRBBBOYBWBOOGROOWBBORYWGBGYWO  [score=14]
  D2 : GOYRWWYWGWOBYRYYYRGGRRGRBBOWOBBYBOBBOGROOWYWORYWGBGWRG  [score=14]
  U' : YRGWWOGWYRYWYRYYWOWOBRGRWRGBBOBYBBOWGGROOWYYROGRGBGBBO  [score=13]
  R' : GORRWRYWGYYWWROOYBGGORGBWRWBBBBYGBOROGROOWYYRGYWWBGYBO  [score=12]
  D  : GOYRWWYWGWOBYRYBBOGGRRGRYWOOBWBYOBBBOGROOWWRGRYWGBGYYR  [score=12]

Algorithm: step 13 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 14
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 14
Previous move: D'

Current state:
GOYRWWYWGWOBYRYWRGGGRRGRYYRBBBOYBWBOOGROOWBBORYWGBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L' : OOYGWWWWGWOBYRYWRGGGRRGRYYRGBBRYBYBOBOOBOGOWRRYWGBOYWB  [score=17]
  R  : GOYRWGYWRBYGORRWYWGGYRGWYYGBBROYRWBROGROOWBBOOYWBBGBWO  [score=16]
  L2 : BOYOWWWWGWOBYRYWRGOGRGGRWYRGBBRYBYBOOBBWOORGORYYGBRYWG  [score=16]
  R2 : GOBRWBYWOGRWYRYBOWGGYRGGYYRBBYOYWWBGOGROOWBBORYWRBGRWO  [score=15]
  U  : YWGOWWGRYGGRYRYWRGOGRRGRYYRBBBOYBWBORYWOOWBBOWOBGBGYWO  [score=14]
  R' : GORRWRYWRWYWRROGYBGGBRGBYYOBBYOYGWBROGROOWBBOGYWWBGYWO  [score=14]
  F  : GOYRWWOWRYOBWRYGRGYRGYGGRRRWYWOYBWBOOGBOOBBBBRYWGBGYWO  [score=14]
  F' : GOYRWWWYWBOBBRYBRGRRRGGYGRYRWOOYBWBOOGGOOWBBYRYWGBGYWO  [score=14]
  F2 : GOYRWWBBBOOBWRYRRGRYYRGRRGGGWYOYBWBOOGWOOYBBWRYWGBGYWO  [score=14]
  D' : GOYRWWYWGWOBYRYYYRGGRRGRBBOWOBBYBOBBOGROOWYWORYWGBGWRG  [score=14]
  B' : BOORWWYWGWOGYROWRYGGRRGRYYRBBBOYBGYBWGRBOWOBOWGOYBWRGY  [score=14]
  B2 : OBWRWWYWGWOBYROWROGGRRGRYYRBBBOYBYOGGGRYOWBBOOWYGBGWYR  [score=14]
  U2 : GWYWWRYOGOGRYRYWRGRYWRGRYYRBBBOYBWBOWOBOOWBBOGGRGBGYWO  [score=13]
  L  : GOYRWWYWGWOBYRYWRGBGROGRWYROBBGYBWBORWOGOBOOBRYYGBRYWG  [score=13]
  B  : BYGRWWYWGWOOYRBWRWGGRRGRYYRBBBOYBOOBYGROOWGBOYGRWBYOGW  [score=13]
  U' : YRGWWOGWYRYWYRYWRGWOBRGRYYRBBBOYBWBOGGROOWBBOOGRGBGYWO  [score=12]
  D2 : GOYRWWYWGWOBYRYBBOGGRRGRYWOOBWBYOBBBOGROOWWRGRYWGBGYYR  [score=12]

Algorithm: step 14 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 15
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 14
Previous move: F2

Current state:
GOYRWWBBBOOBWRYRRGRYYRGRRGGGWYOYBWBOOGWOOYBBWRYWGBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U  : YWBOWBGRBRYYWRYRRGOGWRGRRGGGWYOYBWBORYWOOYBBWOOBGBGYWO  [score=16]
  L  : ROYRWWRBBOOBWRYRRGGYYOGRWGGOWYGYBWBOWYWGOBOOBRYBGBRYWG  [score=16]
  L' : OOYGWWWBBOOBWRYRRGGYYRGRBGGRWYRYBRBOBOOBOGWYWRYWGBOYWG  [score=16]
  L2 : GOYOWWWBBOOBWRYRRGOYYGGRWGGGWYRYBBBOWBBYOOWGORYRGBRYWR  [score=16]
  U2 : BBBWWRYOGOGWWRYRRGRYWRGRRGGGWYOYBWBOOOBOOYBBWRYYGBGYWO  [score=15]
  U' : BRGBWOBWYRYWWRYRRGOOBRGRRGGGWYOYBWBORYYOOYBBWOGWGBGYWO  [score=14]
  F  : GOYRWWWYWBOBBRYBRGRRRGGYGRYRWOOYBWBOOGGOOWBBYRYWGBGYWO  [score=14]
  F' : GOYRWWOWRYOBWRYGRGYRGYGGRRRWYWOYBWBOOGBOOBBBBRYWGBGYWO  [score=14]
  B' : BOORWWBBBOOGWRORRYRYYRGRRGGGWYOYBGYBWGWBOYOBWWGOYBWRGY  [score=14]
  B2 : OBWRWWBBBOOBWRORRORYYRGRRGGGWYOYBYOGGGWYOYBBWOWYGBGWYR  [score=14]
  R  : GOYRWGBBRBYGORROWRRYYRGWRGBGWYOYRWBGOGWOOYBBWOYWBBGYWO  [score=13]
  R' : GOYRWRBBGRWORROGYBRYYRGBRGOGWYOYGWBROGWOOYBBWBYWWBGYWO  [score=13]
  R2 : GOYRWBBBOGRRYRWBOORYYRGGRGRGWYOYWWBBOGWOOYBBWGYWRBGYWO  [score=13]
  D  : GOYRWWBBBOOBWRYYWORYYRGRRRGYBOWYBGOWOGWOOYRGGRYWGBGBBW  [score=13]
  B  : BYGRWWBBBOOOWRBRRWRYYRGRRGGGWYOYBOOBYGWOOYGBWYGRWBYOGW  [score=13]
  D' : GOYRWWBBBOOBWRYRGGRYYRGRBBWWOGBYWOBYOGWOOYYWORYWGBGRRG  [score=12]
  D2 : GOYRWWBBBOOBWRYBBWRYYRGRYWOOBWBYOYWGOGWOOYRRGRYWGBGRGG  [score=10]

Algorithm: step 15 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 16
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 16
Previous move: U

Current state:
YWBOWBGRBRYYWRYRRGOGWRGRRGGGWYOYBWBORYWOOYBBWOOBGBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R' : YWWOWRGRGRWRRRYGYYOGYRGBRGOGWYOYGWBORYWOOYBBWBOBBBGBWO  [score=19]
  L2 : GWBOWBWRBRYYWRYRRGOGWGGRBGGYWYOYBGBOWBBYOOWYROORGBRYWO  [score=18]
  B' : BOROWBGRBRYYWRWRRBOGWRGRRGGGWYOYBGYYWYWBOYOBWBGOOBWOGY  [score=17]
  B2 : OBWOWBGRBRYBWRORRROGWRGRRGGGWYOYBBWYGYWYOYYBWOWYGBGBOO  [score=17]
  F  : YWBOWBWYWGYYRRYBRGRROGGGGRWRWROYBWBORYGOOWBBYOOBGBGYWO  [score=16]
  L  : OWBRWBRRBRYYWRYRRGGGWOGRWGGOWYGYBBBOWYWYOBROBOOGGBOYWY  [score=16]
  L' : OWBGWBBRBRYYWRYRRGYGWOGRGGGOWYRYBRBOBORBOYWYWOOWGBOYWG  [score=16]
  U  : BBBWWRYOGOGWWRYRRGRYWRGRRGGGWYOYBWBOOOBOOYBBWRYYGBGYWO  [score=15]
  R  : YWYOWGGROYYGYRRRWROGBRGBRGBGWWOYRWBGRYWOOYBBWOOBBBGYWO  [score=15]
  R2 : YWYOWBGROGRRYRWYYROGYRGGRGOGWBOYBWBBRYWOOYBBWGOBRBGWWO  [score=15]
  F' : YWBOWBRWRYYYWRYGRGWRGGGGORRWYWOYBWBORYBOORBBGOOBGBGYWO  [score=15]
  D  : YWBOWBGRBRYYWRYYWOOGWRGRRRGYBOWYBGOWRYWOOYRGGOOBGBGBBW  [score=15]
  U2 : BRGBWOBWYRYWWRYRRGOOBRGRRGGGWYOYBWBORYYOOYBBWOGWGBGYWO  [score=14]
  F2 : YWBOWBYWGWYYYRYWRGGGRRGRWGOBRGOYBWBORYROOWBBROOBGBGYWO  [score=14]
  D' : YWBOWBGRBRYYWRYRGGOGWRGRBBWWOGBYWOBYRYWOOYYWOOOBGBGRRG  [score=14]
  B  : YYGOWBGRBRYOWRBRRWOGWRGRRGGGWYOYBROBBYWWOYYBWYGOWBOOGB  [score=14]
  D2 : YWBOWBGRBRYYWRYBBWOGWRGRYWOOBWBYOYWGRYWOOYRRGOOBGBGRGG  [score=12]

Algorithm: step 16 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 17
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: R

Current state:
YWYOWGGROYYGYRRRWROGBRGBRGBGWWOYRWBGRYWOOYBBWOOBBBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R2 : YWWOWRGRGRWRRRYGYYOGYRGBRGOGWYOYGWBORYWOOYBBWBOBBBGBWO  [score=19]
  F  : YWYOWGWYWGYGRRROWRRROGGGBBBRYYOYRWBGRYGOOWBBWOOBBBGYWO  [score=19]
  L2 : GWYOWGWROYYGYRRRWROGBGGBBGBYWWOYRGBGWBBYOOWYROORBBRYWO  [score=17]
  F' : YWYOWGYYRWYGWRRGWRBBBGGGORRWYWOYRWBGRYOOORBBGOOBBBGYWO  [score=16]
  F2 : YWYOWGWWGWYGYRRWWRBGRBGRBGOORGOYRWBGRYROOYBBYOOBBBGYWO  [score=16]
  U  : YGOWWRYOGOGBYRRRWRRYWRGBRGBGWWOYRWBGOOBOOYBBWYYGBBGYWO  [score=15]
  U' : GOYRWWOGYOOBYRRRWRYYGRGBRGBGWWOYRWBGOGBOOYBBWRYWBBGYWO  [score=15]
  U2 : ORGGWOYWYRYWYRRRWROOBRGBRGBGWWOYRWBGYYGOOYBBWOGBBBGYWO  [score=15]
  R  : YWYOWBGROGRRYRWYYROGYRGGRGOGWBOYBWBBRYWOOYBBWGOBRBGWWO  [score=15]
  L  : OWYRWGRROYYGYRRRWRGGBOGBWGBOWWGYRBBGWYWYOBROBOOGBBOYWY  [score=15]
  L' : OWYGWGBROYYGYRRRWRYGBOGBGGBOWWRYRRBGBORBOYWYWOOWBBOYWG  [score=15]
  B2 : GBWOWGGROYYBYRORWROGBRGBRGBGWWOYRYWYRYWROYGBWOWYGBBBOO  [score=15]
  D  : YWYOWGGROYYGYRRYWOOGBRGBRWRWRGWYBGOWRYWOOYRGBOOBBBGBBW  [score=14]
  D' : YWYOWGGROYYGYRRRGBOGBRGBBBWWOGBYWGRWRYWOOYYWOOOBBBGRWR  [score=14]
  D2 : YWYOWGGROYYGYRRBBWOGBRGBYWOGBWRYOWWGRYWOOYRWROOBBBGRGB  [score=13]
  B  : GRROWGGROYYGYRBRWWOGBRGBRGBGWWOYRROBYYWWOYYBWYBOWBOOGB  [score=11]
  B' : BOROWGGROYYYYRWRWYOGBRGBRGBGWWOYRRRGWYWBOYGBWBGOOBWOBY  [score=11]

Algorithm: step 17 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 18
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: U'

Current state:
GOYRWWOGYOOBYRRRWRYYGRGBRGBGWWOYRWBGOGBOOYBBWRYWBBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F2 : GOYRWWWWGWOBYRRBWRBGRBGRGYYYGOOYRWBGOGROOYBBORYWBBGYWO  [score=18]
  L' : OOYGWWWGYOOBYRRRWRGYGRGBOGBYWWRYRRBGBOOBOGWYBRYWBBOYWG  [score=18]
  R2 : GOWRWROGGRWRRRYBOOYYYRGBRGRGWYOYWWBYOGBOOYBBWBYWBBGGWO  [score=17]
  L2 : GOYOWWWGYOOBYRRRWROYGGGBWGBGWWRYROBGWBBYOOBGORYRBBRYWY  [score=17]
  F  : GOYRWWWYBOOBGRRYWRRRYGGYBBGRYOOYRWBGOGGOOWBBWRYWBBGYWO  [score=16]
  F' : GOYRWWOYRWOBWRRGWRGBBYGGYRRBYWOYRWBGOGYOOGBBORYWBBGYWO  [score=16]
  L  : YOYRWWRGYOOBYRRRWRGYGOGBWGBOWWGYRWBGBYWGOBOOBRYOBBRYWG  [score=16]
  U' : ORGGWOYWYRYWYRRRWROOBRGBRGBGWWOYRWBGYYGOOYBBWOGBBBGYWO  [score=15]
  U2 : YGOWWRYOGOGBYRRRWRRYWRGBRGBGWWOYRWBGOOBOOYBBWYYGBBGYWO  [score=15]
  R' : GOGRWBOGBRYOWRORRBYYWRGRRGGGWYOYBWBROGBOOYBBWYYWWBGYWO  [score=14]
  D  : GOYRWWOGYOOBYRRYWOYYGRGBRWRWRGWYBGOWOGBOOYRGBRYWBBGBBW  [score=14]
  D' : GOYRWWOGYOOBYRRRGBYYGRGBBBWWOGBYWGRWOGBOOYYWORYWBBGRWR  [score=14]
  D2 : GOYRWWOGYOOBYRRBBWYYGRGBYWOGBWRYOWWGOGBOOYRWRRYWBBGRGB  [score=13]
  B2 : GBWRWWOGYOOBYRORWOYYGRGBRGBGWWOYRYOGRGBROYBBWOWYGBBWYR  [score=13]
  R  : GOYRWBOGRBRRORWOYRYYYRGWRGYGWGOYBWBBOGBOOYBBWGYWRBGWWO  [score=12]
  B  : BRRRWWOGYOOGYRBRWWYYGRGBRGBGWWOYROOBYGBOOYGBWYBRWBYOGW  [score=12]
  B' : BOORWWOGYOOGYRORWYYYGRGBRGBGWWOYRRRBWGBBOYGBWWGOYBWRBY  [score=11]

Algorithm: step 18 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 19
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 14
Previous move: R'

Current state:
GOGRWBOGBRYOWRORRBYYWRGRRGGGWYOYBWBROGBOOYBBWYYWWBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R' : GOWRWROGGRWRRRYBOOYYYRGBRGRGWYOYWWBYOGBOOYBBWBYWBBGGWO  [score=17]
  L' : OOGGWBWGBRYOWRORRBGYWRGROGGYWYRYBRBRBOOBOGWYBYYWWBOYWG  [score=17]
  L2 : GOGOWBWGBRYOWRORRBOYWGGRWGGGWYRYBOBRWBBYOOBGOYYRWBRYWY  [score=16]
  L  : YOGRWBRGBRYOWRORRBGYWOGRWGGOWYGYBWBRBYWGOBOOBYYOWBRYWG  [score=15]
  B2 : RBWRWBOGBRYBWRORROYYWRGRRGGGWYOYBGOGBGBOOYOBWOWYGBWWYY  [score=15]
  F' : GOGRWBRWRYYOWROGRBWRGYGGYRRBYWOYBWBROGBOOGBBOYYWWBGYWO  [score=14]
  B  : OOBRWBOGBRYRWRBRRWYYWRGRRGGGWYOYBOOBGGBOOYGBWYWYWBYOGW  [score=14]
  U  : GBBOWGGROYYWWRORRBOGBRGRRGGGWYOYBWBRYYWOOYBBWRYOWBGYWO  [score=13]
  U' : ORGGWOBBGYYWWRORRBRYORGRRGGGWYOYBWBRYYWOOYBBWOGBWBGYWO  [score=13]
  U2 : BGOBWRGOGOGBWRORRBYYWRGRRGGGWYOYBWBRRYOOOYBBWYYWWBGYWO  [score=13]
  D' : GOGRWBOGBRYOWRORGGYYWRGRBBWWOGBYWRBYOGBOOYYWOYYWWBGRRB  [score=13]
  R2 : GOYRWBOGRBRRORWOYRYYYRGWRGYGWGOYBWBBOGBOOYBBWGYWRBGWWO  [score=12]
  F  : GOGRWBWYBOYOGROBRBRRYGGYGRWRWROYBWBROGGOOWBBYYYWWBGYWO  [score=12]
  F2 : GOGRWBYWGWYOYROBRBGGRRGRWYYBGOOYBWBROGROOWBBRYYWWBGYWO  [score=12]
  D  : GOGRWBOGBRYOWROYWOYYWRGRRRBYBRWYBGOWOGBOOYRGGYYWWBGBBW  [score=12]
  B' : BOORWBOGBRYGWRORRGYYWRGRRGGGWYOYBBOOWGBBOYRBWWGOYBWYWY  [score=12]
  D2 : GOGRWBOGBRYOWROBBWYYWRGRYWORBWBYOYWGOGBOOYRRBYYWWBGRGG  [score=10]

Algorithm: step 19 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 20
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 13
Previous move: U2

Current state:
BGOBWRGOGOGBWRORRBYYWRGRRGGGWYOYBWBRRYOOOYBBWYYWWBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : YGORWRROGOGBWRORRBGYWOGRWGGOWYGYBWBROYWYOBROBYYGWBBYWB  [score=16]
  L' : OGOGWRWOGOGBWRORRBBYWBGRGGGYWYRYBRBRBORBOYWYOYYWWBOYWG  [score=16]
  L2 : GGOOWRWOGOGBWRORRBOYWGGRWGGBWYBYBGBRWBBYOOOYRYYRWBRYWY  [score=15]
  B2 : RBWBWRGOGOGBWRORRRYYWRGRRGGGWYOYBOGBBYOOOYBBWOWYGBWWYY  [score=15]
  R  : BGYBWWGOYBOBGRROWRYYORGRRGGGWWOYRWBGRYOOOYBBWRYWBBGYWO  [score=14]
  R' : BGWBWRGOGRWORRGBOBYYYRGBRGRGWYOYWWBYRYOOOYBBWGYWRBGOWO  [score=14]
  B  : BOBBWRGOGOGRWRBRRWYYWRGRRGGGWYOYBROBOYOGOYBBWYWYWBYOGW  [score=14]
  U  : ORGGWOBBGYYWWRORRBRYORGRRGGGWYOYBWBRYYWOOYBBWOGBWBGYWO  [score=13]
  U' : GBBOWGGROYYWWRORRBOGBRGRRGGGWYOYBWBRYYWOOYBBWRYOWBGYWO  [score=13]
  F' : BGOBWROWRYGBWROGRBWRGYGGYRROYWOYBWBRRYGOOOBBGYYWWBGYWO  [score=13]
  F2 : BGOBWRYWGWGBYROORBGGRRGRWYYGOGOYBWBRRYROOWBBOYYWWBGYWO  [score=12]
  D' : BGOBWRGOGOGBWRORGGYYWRGRBBWWOGBYWRBYRYOOOYYWOYYWWBGRRB  [score=12]
  B' : BORBWRGOGOGBWRGRROYYWRGRRGGGWYOYBBOBWYOBOYRBWWGOYBWYWY  [score=12]
  R2 : BGYBWBGORBRRORWBGOYYYRGWRGYGWOOYRWBGRYOOOYBBWGYWRBGWWO  [score=11]
  F  : BGOBWRWYOGGBOROGRBRRYGGYGRWRWOOYBWBRRYGOOWBBYYYWWBGYWO  [score=11]
  D  : BGOBWRGOGOGBWROYWOYYWRGRRRBYBRWYBGOWRYOOOYRGGYYWWBGBBW  [score=11]
  D2 : BGOBWRGOGOGBWROBBWYYWRGRYWORBWBYOYWGRYOOOYRRBYYWWBGRGG  [score=9]

Algorithm: step 20 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 21
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 13
Previous move: F'

Current state:
BGOBWROWRYGBWROGRBWRGYGGYRROYWOYBWBRRYGOOOBBGYYWWBGYWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  D' : BGOBWROWRYGBWROYRRWRGYGGBBGWOOBYYRBWRYGOOOYWOYYWWBGGRB  [score=17]
  L  : WGOYWRYWRYGBWROGRBORGOGGWRROYWGYBWBRGOGYOBROBYYOWBBYWB  [score=16]
  L' : OGOGWRWWRYGBWROGRBBRGBGGORRWYWYYBYBRBORBOYGOGYYWWBOYWO  [score=16]
  U  : ORRGWWBBOWRGWROGRBRYGYGGYRROYWOYBWBRYYWOOOBBGYGBWBGYWO  [score=15]
  D  : BGOBWROWRYGBWROYWOWRGYGGGRBWBRYYBOOWRYGOOOYRRYYWWBGBBG  [score=15]
  L2 : OGOOWRWWRYGBWROGRBORGGGGWRRBYWBYBOBRGBBOOOGYRYYYWBYYWW  [score=15]
  B2 : RBWBWROWRYGBWROGRRWRGYGGYRROYWOYBOGBBYGOOOBBGOWYGBWWYY  [score=15]
  B  : BOBBWROWRYGRWRBGRWWRGYGGYRROYWOYBROBOYGGOOBBGYWYWBYOGW  [score=14]
  U' : OBBWWGRROYYWWROGRBYGBYGGYRROYWOYBWBRWRGOOOBBGRYGWBGYWO  [score=13]
  U2 : RWORWBOGBRYGWROGRBYYWYGGYRROYWOYBWBRYGBOOOBBGWRGWBGYWO  [score=13]
  R  : BGYBWWOWYBOBGRRYWGWROYGRYRROYGOYGWBRRYGOOOBBGRYWBBGWWO  [score=13]
  R' : BGGBWGOWRGWYRRGBOBWRWYGBYRROYYOYWWBYRYGOOOBBGRYWRBGOWO  [score=13]
  R2 : BGWBWBOWRBRGORWBGYWRYYGWYRYOYOOYRWBRRYGOOOBBGRYWGBGGWO  [score=12]
  F' : BGOBWRYWGWGBYROORBGGRRGRWYYGOGOYBWBRRYROOWBBOYYWWBGYWO  [score=12]
  D2 : BGOBWROWRYGBWROBBGWRGYGGYWORBWBYOWYORYGOOOGRBYYWWBGYRR  [score=12]
  B' : BORBWROWRYGBWRGGROWRGYGGYRROYWOYBBOBWYGBOORBGWGOYBWYWY  [score=12]
  F2 : BGOBWRWYOGGBOROGRBRRYGGYGRWRWOOYBWBRRYGOOWBBYYYWWBGYWO  [score=11]

Algorithm: step 21 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 22
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 12
Previous move: R2

Current state:
BGWBWBOWRBRGORWBGYWRYYGWYRYOYOOYRWBRRYGOOOBBGRYWGBGGWO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  D' : BGWBWBOWRBRGORWYRYWRYYGWBBGWOOBYYRRORYGOOOGWORYWGBGBGY  [score=16]
  D  : BGWBWBOWRBRGORWGWOWRYYGWBGYORRYYBOOWRYGOOOYRYRYWGBGBBG  [score=15]
  L  : WGWYWBYWRBRGORWBGYORYOGWWRYOYOGYRWBRGOGYOBROBRYOGBBGWB  [score=15]
  L' : OGWGWBWWRBRGORWBGYBRYBGWORYWYOYYRYBRBORBOYGOGRYWGBOGWO  [score=15]
  U  : WBRGWWBBOWRYORWBGYRYGYGWYRYOYOOYRWBRRYWOOOBBGBRGGBGGWO  [score=14]
  L2 : OGWOWBWWRBRGORWBGYORYGGWWRYBYOBYROBRGBBOOOGYRRYYGBYGWW  [score=14]
  U' : OBBWWGRBWRYWORWBGYBRGYGWYRYOYOOYRWBRWRYOOOBBGRYGGBGGWO  [score=13]
  R  : BGGBWGOWRGWYRRGBOBWRWYGBYRROYYOYWWBYRYGOOOBBGRYWRBGOWO  [score=13]
  R' : BGYBWWOWYBOBGRRYWGWROYGRYRROYGOYGWBRRYGOOOBBGRYWBBGWWO  [score=13]
  D2 : BGWBWBOWRBRGORWBBGWRYYGWGWORBWRYOOYORYGOOOBGYRYWGBGYRY  [score=13]
  U2 : RWOBWBWGBRYGORWBGYRYWYGWYRYOYOOYRWBRBRGOOOBBGWRYGBGGWO  [score=12]
  F  : BGWBWBGOGORGWRWRGYYYWRGRYWYBOBOYRWBRRYOOOYBBORYWGBGGWO  [score=12]
  B  : GWYBWBOWRBRRORBBGWWRYYGWYRYOYOOYRROBWYGGOOBBGGGRWBYOGW  [score=12]
  B2 : RBWBWBOWRBRBOROBGRWRYYGWYRYOYOOYRWGBYYGWOOGBGOWGGBGWYR  [score=12]
  B' : BORBWBOWRBRBORGBGWWRYYGWYRYOYOOYRYWGWYGBOORBGWGOYBWRGG  [score=11]
  F' : BGWBWBBOBORGYRWOGYYWYRGRWYYGOGOYRWBRRYROOWBBORYWGBGGWO  [score=10]
  F2 : BGWBWBOYOGRGORWGGYYRYWGYYRWRWOOYRWBRRYBOOOBBBRYWGBGGWO  [score=10]

Algorithm: step 22 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 23
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 14
Previous move: L2

Current state:
OGWOWBWWRBRGORWBGYORYGGWWRYBYOBYROBRGBBOOOGYRRYYGBYGWW

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U' : WOOWWGRBWRYYORWBGYBRGGGWWRYBYOBYROBRORYOOOGYRGBBGBYGWW  [score=18]
  D' : OGWOWBWWRBRGORWWRYORYGGWGYROBBBYYRROGBBOOOGWWRYYGBYBGY  [score=17]
  U  : WBRGWWOOWORYORWBGYGBBGGWWRYBYOBYROBRRYYOOOGYRBRGGBYGWW  [score=16]
  D2 : OGWOWBWWRBRGORWGYRORYGGWGWWRBORYBOYBGBBOOOBGYRYYGBYWRY  [score=16]
  R  : OGGOWGWWRGWYRRGBOBORWGGBWRRBYYBYWOBYGBBOOOGYRRYYRBYOWW  [score=15]
  R' : OGYOWWWWYBOBGRRYWGOROGGRWRRBYGBYGOBRGBBOOOGYRRYYBBYWWW  [score=15]
  R2 : OGOOWRWWRYGBWROGRBORGGGGWRRBYWBYBOBRGBBOOOGYRYYYWBYYWW  [score=15]
  D  : OGWOWBWWRBRGORWGWWORYGGWBGYORRYYBBBOGBBOOOWRYRYYGBYGYR  [score=15]
  L  : OGWGWBWWRBRGORWBGYBRYBGWORYWYOYYRYBRBORBOYGOGRYWGBOGWO  [score=15]
  L' : WGWYWBYWRBRGORWBGYORYOGWWRYOYOGYRWBRGOGYOBROBRYOGBBGWB  [score=15]
  B  : GWYOWBWWRBRRORBBGOORYGGWWRYBYOBYRGOGWBBGOOOYRGGRWBYWYY  [score=15]
  B' : GOGOWBWWRBROORGBGWORYGGWWRYBYOBYRYWGOBBBOORYRYYWYBWRGG  [score=14]
  U2 : RWWBWOWGOGBBORWBGYRYYGGWWRYBYOBYROBRBRGOOOGYRORYGBYGWW  [score=13]
  F  : OGWOWBROBWRGWRWRGYWGORGRYWYBOBBYROBRGBBOOYGYORYYGBYGWW  [score=12]
  F2 : OGWOWBOYBRRGORWBGYYRWWGGYRORWWBYROBRGBBOOOGYBRYYGBYGWW  [score=12]
  B2 : RBOOWBWWRBRGOROBGGORYGGWWRYBYOBYRWGOYBBWOOGYRWWGYBGYYR  [score=12]
  F' : OGWOWBBOBORGYRWBGYYWYRGROGWBORBYROBRGBROOWGYWRYYGBYGWW  [score=10]

Algorithm: step 23 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 24
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 16
Previous move: D2

Current state:
OGWOWBWWRBRGORWGYRORYGGWGWWRBORYBOYBGBBOOOBGYRYYGBYWRY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U' : WOOWWGRBWRYYORWGYRBRGGGWGWWRBORYBOYBORYOOOBGYGBBGBYWRY  [score=20]
  R  : OGWOWGWWRGWRRRYBOGORWGGBGWRRBYRYWOYWGBBOOOBGYBYYBBYORY  [score=19]
  U  : WBRGWWOOWORYORWGYRGBBGGWGWWRBORYBOYBRYYOOOBGYBRGGBYWRY  [score=18]
  R' : OGYOWWWWWGOBYRRRWGOROGGBGWBRBWRYGOYRGBBOOOBGYRYYBBYWRY  [score=18]
  D  : OGWOWBWWRBRGORWWRYORYGGWGYROBBBYYRROGBBOOOGWWRYYGBYBGY  [score=17]
  R2 : OGOOWBWWBRYGWROGRBORWGGGGWRRBWRYBOYRGBBOOOBGYWYYWBYYRY  [score=16]
  L  : OGWGWBGWRBRGORWGYRRRYRGWOWWYBOYYBYYBBOYBOGGOBRYWGBOWRO  [score=16]
  U2 : RWWBWOWGOGBBORWGYRRYYGGWGWWRBORYBOYBBRGOOOBGYORYGBYWRY  [score=15]
  F  : OGWOWBYOBWRGWRWRYRGGOWGRWWYGOBRYBOYBGBROOBBGORYYGBYWRY  [score=15]
  F' : OGWOWBBOGORGBRWRYRYWWRGWOGGBOYRYBOYBGBROOWBGWRYYGBYWRY  [score=15]
  D' : OGWOWBWWRBRGORWGWWORYGGWBGYORRYYBBBOGBBOOOWRYRYYGBYGYR  [score=15]
  F2 : OGWOWBOBRYRGORWBYRWWGWGGYRORWWRYBOYBGBGOOOBGBRYYGBYWRY  [score=14]
  B  : GWROWBWWRBRBORYGYOORYGGWGWWRBORYBGOBWBBGOOOGYWGRRBYYYY  [score=14]
  L' : YGWYWBYWRBRGORWGYRORYOGWWWWOBOGYBGYBBOGGOBYOBRYOGBRWRR  [score=13]
  L2 : RGWRWBOWRBRGORWGYRYRYYGWYWWOBOOYBWYBYGBOOOBBGRYGGBGWRO  [score=13]
  B' : BOGOWBWWRBROORGGYWORYGGWGWWRBORYBRWGOBBYOOBGYYYYYBRRGW  [score=13]
  B2 : BYOOWBWWRBRBOROGYGORYGGWGWWRBORYBWGORBBWOOGGYYRWYBGYYR  [score=12]

Algorithm: step 24 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 25 (default)

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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 25
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: F

Current state:
OGWOWBYOBWRGWRWRYRGGOWGRWWYGOBRYBOYBGBROOBBGORYYGBYWRY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : GGWWWBWOBWRGWRWRYRGGORGROWYYOBYYBYYBRBOBOGGOBRYYGBOWRO  [score=20]
  R  : OGWOWGYORGWRRRYWWRGGWWGBWWBGOORYROYYGBROOBBGOBYYBBYBRY  [score=19]
  U' : YOOOWGBBWRYYWRWRYRWRGWGRWWYGOBRYBOYBGGOOOBBGOGBRGBYWRY  [score=16]
  R' : OGOOWRYOYRWWYRRRWGGGBWGBWWBGOWRYGOYRGBROOBBGOBYYBBYWRY  [score=16]
  R2 : OGBOWBYOBRYRWRWGRWGGWWGGWWRGOWRYBOYBGBROOBBGOYYYRBYORY  [score=15]
  F2 : OGWOWBBOGORGBRWRYRYWWRGWOGGBOYRYBOYBGBROOWBGWRYYGBYWRY  [score=15]
  L2 : GGWRWBOOBWRGWRWRYRYGOYGRYWYOOBOYBYYBOGBBOORBGRYWGBWWRG  [score=15]
  F  : OGWOWBOBRYRGORWBYRWWGWGGYRORWWRYBOYBGBGOOOBGBRYYGBYWRY  [score=14]
  D  : OGWOWBYOBWRGWRWWRYGGOWGRRYRBBBOYYGROGBROOBWWYRYYGBYBGO  [score=14]
  L' : YGWYWBYOBWRGWRWRYROGOOGRYWYGOBWYBWYBBOGGOBOBRRYOGBRWRG  [score=14]
  U  : WBBGWOOOYGGOWRWRYRGBRWGRWWYGOBRYBOYBRYYOOBBGOWRGGBYWRY  [score=13]
  U2 : BOYBWOWGOGBRWRWRYRRYYWGRWWYGOBRYBOYBWRGOOBBGOGGOGBYWRY  [score=13]
  D' : OGWOWBYOBWRGWRWWWYGGOWGRBGOORGYYOBBBGBROOBWRYRYYGBYRYR  [score=13]
  B  : GWROWBYOBWRBWRYRYOGGOWGRWWYGOBRYBGOBWBRGOBOGOWGRRBYYYY  [score=13]
  D2 : OGWOWBYOBWRGWRWBGOGGOWGRWRYBYOBYRBOGGBROOBRYRRYYGBYWWY  [score=12]
  B' : BOGOWBYOBWROWRGRYWGGOWGRWWYGOBRYBRWGOBRYOBBGOYYYYBRRGW  [score=12]
  B2 : BYOOWBYOBWRBWRORYGGGOWGRWWYGOBRYBWGORBRWOBGGOYRWYBGYYR  [score=11]

Algorithm: step 25 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 26 (default)

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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 26
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 14
Previous move: D

Current state:
OGWOWBYOBWRGWRWWRYGGOWGRRYRBBBOYYGROGBROOBWWYRYYGBYBGO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : OGWOWBWWWBRGBRWBRYORRGGYGWRRBYOYYGROGBBOOOWWYRYYGBYBGO  [score=19]
  L  : GGWWWBROBWRGWRWWRYBGOOGRGYROBBYYYYRORBYBOWGOWRYYGBOBGO  [score=17]
  F2 : OGWOWBBBBYRGBRWRRYRYRRGWOGGBOYOYYGROGBWOOWWWWRYYGBYBGO  [score=16]
  U' : YOOOWGBBWRYYWRWWRYWRGWGRRYRBBBOYYGROGGOOOBWWYGBRGBYBGO  [score=15]
  B  : GWYOWBYOBWROWRRWRGGGOWGRRYRBBBOYYGOWWBRGOBOWYBGRGBYOYY  [score=15]
  B' : WOGOWBYOBWROWRGWRWGGOWGRRYRBBBOYYYWGGBRROBOWYYYOYBGRGB  [score=15]
  F  : OGWOWBYBRYRGORWBRYRWGYGGRROWWWOYYGROGBBOOBWWBRYYGBYBGO  [score=14]
  L' : OGWYWBYOBWRGWRWWRYOGOOGRYYRGBBWYYRROWOGWOBYBRRYGGBOBGB  [score=14]
  L2 : BGWOWBGOBWRGWRWWRYOGOYGRYYROBBOYYYROYWWBOORBGRYRGBWBGG  [score=14]
  R' : OGOOWRYORWWWRRRYWGGGBWGYRYOBBBOYGGRRGBROOBWWYBYYBBYWGO  [score=13]
  D2 : OGWOWBYOBWRGWRWWWYGGOWGRBGOORGYYOBBBGBROOBWRYRYYGBYRYR  [score=13]
  U  : WBBGWOOOYGGOWRWWRYGBRWGRRYRBBBOYYGRORYYOOBWWYWRGGBYBGO  [score=12]
  U2 : BOYBWOWGOGBRWRWWRYRYYWGRRYRBBBOYYGROWRGOOBWWYGGOGBYBGO  [score=12]
  R  : OGBOWGYORGWYRRRWWWGGWWGBRYBBBOOYRGRRGBROOBWWYOYYYBYBGO  [score=12]
  R2 : OGBOWYYOOYRWWRWGRWGGBWGGRYRBBWOYBGRBGBROOBWWYRYYRBYOGO  [score=12]
  D  : OGWOWBYOBWRGWRWBGOGGOWGRWRYBYOBYRBOGGBROOBRYRRYYGBYWWY  [score=12]
  B2 : ORGOWBYOBWRWWROWRGGGOWGRRYRBBBOYYWGOYBRWOBGWYOGBYBGYYR  [score=12]

Algorithm: step 26 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 27
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: L

Current state:
GGWWWBROBWRGWRWWRYBGOOGRGYROBBYYYYRORBYBOWGOWRYYGBOBGO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : GGWWWBWWWBRGBRWORYORRGGYBOGYWWYYYYRORBBBOOGORRYYGBOBGO  [score=22]
  F  : GGWWWBWWYRRGORWBRYGOBYGGRROWWWYYYYRORBOBOBGOBRYYGBOBGO  [score=21]
  U' : RWGOWGBBWRYYWRWWRYWRGOGRGYROBBYYYYROBGOBOWGOWRBYGBOBGO  [score=19]
  U2 : BORBWWWGGRBYWRWWRYRYYOGRGYROBBYYYYROWRGBOWGOWBGOGBOBGO  [score=17]
  F2 : GGWWWBBBOWRGWRWYRYRYGRGOOGBBORYYYYRORBWBOWGOWRYYGBOBGO  [score=17]
  B  : GWYWWBROBWROWRRWRYBGOOGRGYROBBYYYRBGWBYGOWGOWBGRGBYOOY  [score=17]
  B' : GBRWWBROBWRGWRGWRWBGOOGRGYROBBYYYYWGYBYROWOOWYOOYBGRGB  [score=17]
  R' : GGOWWRRORWWWRRRYWGBGBOGYGYOOBBYYGYRRRBYBOWGOWBYYBBOWGO  [score=16]
  D' : GGWWWBROBWRGWRWGYRBGOOGRGOWYYORYBOYBRBYBOWBGORYYGBOWRY  [score=16]
  B2 : ORYWWBROBWRGWRBWRRBGOOGRGYROBBYYYWGGYBYWOWGOWOGBOBGYYR  [score=16]
  U  : WBBGWOGWRBGOWRWWRYRBYOGRGYROBBYYYYRORYYBOWGOWWRGGBOBGO  [score=15]
  R  : GGBWWGRORGWYRRRWWWBGWOGBGYBOBOYYRYRRRBYBOWGOWOYYYBOBGO  [score=15]
  R2 : GGBWWYROOYRWWRWGRWBGBOGGGYROBWYYBYRBRBYBOWGOWRYYRBOOGO  [score=15]
  D2 : GGWWWBROBWRGWRWGOWBGOOGRBGOORYYYYBBORBYBOWWRYRYYGBOGYR  [score=14]
  L  : BGWOWBGOBWRGWRWWRYOGOYGRYYROBBOYYYROYWWBOORBGRYRGBWBGG  [score=14]
  L2 : OGWYWBYOBWRGWRWWRYOGOOGRYYRGBBWYYRROWOGWOBYBRRYGGBOBGB  [score=14]
  D  : GGWWWBROBWRGWRWBGOBGOOGRWRYBYOBYROYYRBYBOWGYRRYYGBOGOW  [score=13]

Algorithm: step 27 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 28
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 16
Previous move: B2

Current state:
ORYWWBROBWRGWRBWRRBGOOGRGYROBBYYYWGGYBYWOWGOWOGBOBGYYR

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : ORYWWBWWWBRGBRBORRORRGGYBOGYWWYYYWGGYBBWOOGOROGBOBGYYR  [score=21]
  F  : ORYWWBWWYRRGORBBRRGOBYGGRROWWWYYYWGGYBOWOBGOBOGBOBGYYR  [score=20]
  R' : OROWWRRORWWWRRRRBGBGBOGYGYGOBYYYOWGOYBYWOWGOWBGBBBGYYR  [score=19]
  B  : GBRWWBROBWRGWRGWRWBGOOGRGYROBBYYYYWGYBYROWOOWYOOYBGRGB  [score=17]
  B' : GWYWWBROBWROWRRWRYBGOOGRGYROBBYYYRBGWBYGOWGOWBGRGBYOOY  [score=17]
  U' : RWOOWRBBYOGBWRBWRRWRGOGRGYROBBYYYWGGBGOWOWGOWYBYOBGYYR  [score=16]
  R  : ORYWWOROOGBRRRRWWWBGYOGBGYBOBOYYRWGRYBYWOWGOWGGBYBGBYR  [score=16]
  R2 : ORBWWYROGRRWBRWGRWBGYOGOGYOOBYYYBWGBYBYWOWGOWRGBRBGOYR  [score=16]
  F2 : ORYWWBBBOWRGWRBYRRRYGRGOOGBBORYYYWGGYBWWOWGOWOGBOBGYYR  [score=16]
  U2 : BORBWWYROYBYWRBWRROGBOGRGYROBBYYYWGGWRGWOWGOWBGOOBGYYR  [score=15]
  L2 : ORYYWBWOBWRGWRBWRRRGOGGRBYROBBWYYRGGWOGWOWYBYOGGOBOYYB  [score=15]
  U  : YBBRWOOWRBGOWRBWRRYBYOGRGYROBBYYYWGGOGBWOWGOWWRGOBGYYR  [score=14]
  D' : ORYWWBROBWRGWRBGYRBGOOGRGOWWYOGYBGYBYBYWOWYYROGBOBGWRR  [score=14]
  D  : ORYWWBROBWRGWRBYYRBGOOGRWRRBYGBYGOYWYBYWOWGYROGBOBGGOW  [score=13]
  D2 : ORYWWBROBWRGWRBGOWBGOOGRYYRGGWYYYBBOYBYWOWWRROGBOBGGYR  [score=12]
  L  : BRYOWBGOBWRGWRBWRROGOYGRWYRRBBGYYBGGYWWBOOYWGOGROBWYYO  [score=12]
  L' : RRYGWBBOBWRGWRBWRROGOWGRRYRBBBOYYGGGGWYOOBWWYOGWOBYYYO  [score=12]

Algorithm: step 28 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 29
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: B

Current state:
GBRWWBROBWRGWRGWRWBGOOGRGYROBBYYYYWGYBYROWOOWYOOYBGRGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F' : GBRWWBWWWBRGBRGORWORRGGYBOGYWWYYYYWGYBBROOOORYOOYBGRGB  [score=22]
  R' : GBOWWRRORWWWRRRWGGBGBOGYGYGOBRYYYYWYYBYROWOOWBOOBBGRGB  [score=21]
  F  : GBRWWBWWYRRGORGBRWGOBYGGRROWWWYYYYWGYBOROBOOBYOOYBGRGB  [score=21]
  U' : RWGOWBBBRYOOWRGWRWWRGOGRGYROBBYYYYWGBGOROWOOWYBYYBGRGB  [score=18]
  U  : RBBBWOGWRBGOWRGWRWYBYOGRGYROBBYYYYWGYOOROWOOWWRGYBGRGB  [score=17]
  R  : GBRWWYROYGGWRRRWWWBGROGBGYBOBOYYRYWRYBYROWOOWGOOYBGBGB  [score=17]
  F2 : GBRWWBBBOWRGWRGYRWRYGRGOOGBBORYYYYWGYBWROWOOWYOOYBGRGB  [score=17]
  B  : GGWWWBROBWRGWRWWRYBGOOGRGYROBBYYYYRORBYBOWGOWRYYGBOBGO  [score=17]
  B2 : GWYWWBROBWROWRRWRYBGOOGRGYROBBYYYRBGWBYGOWGOWBGRGBYOOY  [score=17]
  U2 : BORBWWRBGYBYWRGWRWYOOOGRGYROBBYYYYWGWRGROWOOWBGOYBGRGB  [score=16]
  R2 : GBBWWYROGWRWGRWGRWBGROGYGYYOBRYYBYWBYBYROWOOWROORBGOGB  [score=16]
  L2 : OBRYWBYOBWRGWRGWRWBGOGGROYRGBBWYYRWGWOOWORYBYYOGYBORGB  [score=14]
  D  : GBRWWBROBWRGWRGRGBBGOOGRWRWBYGBYWOYYYBYROWGYRYOOYBGOOW  [score=13]
  D' : GBRWWBROBWRGWRGGYRBGOOGROOWYYOWYBGYBYBYROWRGBYOOYBGWRW  [score=13]
  D2 : GBRWWBROBWRGWRGOOWBGOOGRRGBGWYYYYBBOYBYROWWRWYOOYBGGYR  [score=13]
  L' : BBRGWBOOBWRGWRGWRWGGOWGRRYRBBBOYYGWGORYOOBWWYYOYYBYRGO  [score=13]
  L  : BBROWBGOBWRGWRGWRWOGOYGRYYRBBBGYYOWGYWWBOOYROYORYBWRGG  [score=12]

Algorithm: step 29 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 30
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 21
Previous move: F

Current state:
GBRWWBWWYRRGORGBRWGOBYGGRROWWWYYYYWGYBOROBOOBYOOYBGRGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R' : GBBWWGWWOBORRRRWGGGOWYGYRRGWWRYYYYWYYBOROBOOBYOOBBGRGB  [score=23]
  R2 : GBWWWYWWGWRBGROGRRGORYGYRRYWWRYYBYWYYBOROBOOBOOOGBGBGB  [score=22]
  F2 : GBRWWBWWWBRGBRGORWORRGGYBOGYWWYYYYWGYBBROOOORYOOYBGRGB  [score=22]
  B  : GGWWWBWWYRRGORWBRYGOBYGGRROWWWYYYYRORBOBOBGOBRYYGBOBGO  [score=21]
  B2 : GWYWWBWWYRROORRBRYGOBYGGRROWWWYYYRBGWBOGOBGOBBGRGBYOOY  [score=21]
  U' : WWGWWBYBRYOOORGBRWRRGYGGRROWWWYYYYWGGOBROBOOBYBOYBGRGB  [score=20]
  D  : GBRWWBWWYRRGORGRGBGOBYGGBRWWYGWYWWYYYBOROBRROYOOYBGOOB  [score=20]
  D' : GBRWWBWWYRRGORGRROGOBYGGOOBYYWWYWGYWYBOROBRGBYOOYBGBRW  [score=20]
  B' : ORYWWBWWYRRGORBBRRGOBYGGRROWWWYYYWGGYBOWOBGOBOGBOBGYYR  [score=20]
  U  : RBYBWWGWWGOBORGBRWYBOYGGRROWWWYYYYWGYOOROBOOBRRGYBGRGB  [score=19]
  R  : GBRWWYWWYGGWRRRROBGORYGBRRYWWBYYGYWOYBOROBOOBGOOYBGWGB  [score=19]
  U2 : YWWBWWRBGYBOORGBRWYOOYGGRROWWWYYYYWGRRGROBOOBGOBYBGRGB  [score=18]
  D2 : GBRWWBWWYRRGORGOOBGOBYGGRGBGWYYYYWWWYBOROBBRWYOOYBGRRO  [score=18]
  F  : GBRWWBBBOWRGWRGYRWRYGRGOOGBBORYYYYWGYBWROWOOWYOOYBGRGB  [score=17]
  L' : BBRGWBOWYRRGORGBRWGOBWGGWROGWWYYYRWGORYOOBBBOYOYYBYRGW  [score=17]
  L2 : WBRYWBYWYRRGORGBRWBOBGGGOROGWWWYYWWGBOOBOROBYYORYBYRGG  [score=17]
  L  : GBRYWBRWYRRGORGBRWWOBYGGYROBWWGYYOWGOBBBOOYROYOWYBWRGG  [score=15]

Algorithm: step 30 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 31
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 19
Previous move: R

Current state:
GBRWWYWWYGGWRRRROBGORYGBRRYWWBYYGYWOYBOROBOOBGOOYBGWGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R2 : GBBWWGWWOBORRRRWGGGOWYGYRRGWWRYYYYWYYBOROBOOBYOOBBGRGB  [score=23]
  R  : GBWWWYWWGWRBGROGRRGORYGYRRYWWRYYBYWYYBOROBOOBOOOGBGBGB  [score=22]
  U' : WWGWWBYYRGOORRRROBGGWYGBRRYWWBYYGYWOGORROBOOBYBOYBGWGB  [score=21]
  U  : RYYBWWGWWGORRRRROBYBOYGBRRYWWBYYGYWOGOOROBOOBGGWYBGWGB  [score=20]
  U2 : YWWYWWRBGYBORRRROBGOOYGBRRYWWBYYGYWOGGWROBOOBGORYBGWGB  [score=18]
  D' : GBRWWYWWYGGWRRRRRYGORYGBOOBYYWWYWOGBYBOROBWGBGOOYBGROB  [score=18]
  B  : WRBWWYWWYGGORRWROYGORYGBRRYWWBYYGYRORBOBOBGOBWYGGBOBGO  [score=18]
  B' : ORYWWYWWYGGGRRBRORGORYGBRRYWWBYYGBRWYBOWOBOOBOGBOBGGYW  [score=18]
  B2 : OWYWWYWWYGGORRRROYGORYGBRRYWWBYYGRBGBBOROBWOBBGWGBYOOG  [score=18]
  F2 : GBRWWYBWWBGWBRROOBYRRBGYROGYWWYYGYWOYBRROROOGGOOYBGWGB  [score=17]
  D2 : GBRWWYWWYGGWRRROOBGORYGBWGBOWYGYYBWWYBOROBROBGOOYBGRRY  [score=17]
  D  : GBRWWYWWYGGWRRRWGBGORYGBROBBGOWYWWYYYBOROBRRYGOOYBGOOB  [score=16]
  L' : BBRGWYOWYGGWRRRROBGORWGBWRYGWBYYGRWOORYOOBBBOGOYYBYWGW  [score=15]
  L2 : WBRYWYYWYGGWRRRROBBORGGBORYGWBWYGWWOBOOBOROBYGORYBYWGG  [score=15]
  F  : GBRWWYBBOWGWWRRYOBRYGRGOYBRRRGYYGYWOYBWROWOOBGOOYBGWGB  [score=14]
  F' : GBRWWYGRRBGWWRRWOBRBYOGRGYROBBYYGYWOYBYROWOOWGOOYBGWGB  [score=14]
  L  : GBRYWYRWYGGWRRRROBWORYGBYRYBWBGYGOWOOBBBOOYROGOWYBWWGG  [score=13]

Algorithm: step 31 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 32
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 20
Previous move: U

Current state:
RYYBWWGWWGORRRRROBYBOYGBRRYWWBYYGYWOGOOROBOOBGGWYBGWGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U2 : WWGWWBYYRGOORRRROBGGWYGBRRYWWBYYGYWOGORROBOOBYBOYBGWGB  [score=21]
  R  : RYWBWYGWGRRBOROGRRYBYYGWRRWWWOYYBYWYGOOROBOOBOGWGBGBGB  [score=21]
  R2 : RYBBWGGWOBORRRRROGYBWYGYRRGWWYYYWYWWGOOROBOOBYGWBBGOGB  [score=21]
  L' : BYYGWWWWWGORRRRROBRBOBGBGRYYWBYYGRWOORGOOOBBOGGYYBYWGW  [score=21]
  R' : RYOBWBGWYRRGOROBRRYBBYGGRROWWWYYYYWGGOOROBOOBWGWWBGYGB  [score=20]
  B2 : OWYBWWGWWGOORRRROGYBOYGBRRYWWBYYGYYRBOOROBROBBGWGBYWGG  [score=20]
  D' : RYYBWWGWWGORRRRRRYYBOYGBOOBYYWWYWOGBGOOROBWGBGGWYBGROB  [score=19]
  L2 : WYYYWWYWWGORRRRROBBBOGGBWRYRWBBYGGWOBOOBOROOGGGRYBYWGY  [score=19]
  U  : YWWYWWRBGYBORRRROBGOOYGBRRYWWBYYGYWOGGWROBOOBGORYBGWGB  [score=18]
  D2 : RYYBWWGWWGORRRROOBYBOYGBWGBOWYGYYBWWGOOROBROBGGWYBGRRY  [score=18]
  L  : YYYYWWRWWGORRRRROBWBOYGBYRYBWBGYGWWOOBBOOOGROGGGYBBWGR  [score=18]
  B' : ORGBWWGWWGORRRYROYYBOYGBRRYWWBYYGBRRYOOWOBOOBWGBGBGGYW  [score=18]
  F2 : RYYBWWBWWBORBRROOBYRRBGYOBYWWGYYGYWOGORROROOGGGWYBGWGB  [score=17]
  D  : RYYBWWGWWGORRRRWGBYBOYGBROBBGOWYWWYYGOOROBRRYGGWYBGOOB  [score=17]
  B  : RRBBWWGWWGOORRWROYYBOYGBRRYWWBYYGGROYOOYOBROBWYGGBGBGW  [score=16]
  F  : RYYBWWBBOGORWRRWOBRYYRGBYBORRGYYGYWOGOWROWOOBGGWYBGWGB  [score=15]
  F' : RYYBWWGRRBORWRRWOBOBYBGRYYROBBYYGYWOGOWROWOOGGGWYBGWGB  [score=15]

Algorithm: step 32 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 33
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: F2

Current state:
RYYBWWBWWBORBRROOBYRRBGYOBYWWGYYGYWOGORROROOGGGWYBGWGB

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U  : YWWYWWRBBYRRBRROOBGORBGYOBYWWGYYGYWOGGWROROOGBORYBGWGB  [score=19]
  U2 : WWBWWBYYRGORBRROOBGGWBGYOBYWWGYYGYWOBORROROOGYRRYBGWGB  [score=19]
  R  : RYWBWYBWGRRBOROBBOYRYBGWOBWWWRYYYYWYGORROROOGOGWGBGGGB  [score=18]
  R' : RYRBWYBWYOBBOROBRRYRGBGGOBOWWWYYYYWGGORROROOGWGWWBGYGB  [score=18]
  D2 : RYYBWWBWWBORBRROOGYRRBGYWGBOWYGYYGWWGORROROOBGGWYBGOBY  [score=18]
  R2 : RYGBWGBWOBOORRBROBYRWBGYOBGWWYYYWYWWGORROROOGYGWYBGRGB  [score=17]
  L2 : WYYYWWYWWBORBRROOBBRRGGYWBYRWGBYGBWOGOORORROGGGOYBBWGY  [score=17]
  B2 : OWYBWWBWWBOOBRROOGYRRBGYOBYWWGYYGYYRBORRORROGBGWGBYWGG  [score=17]
  D' : RYYBWWBWWBORBRROBYYRRBGYOOGYYWWYWOGGGORRORWGBGGWYBGOOB  [score=16]
  L  : YYYBWWOWWBORBRROOBWRRYGYYBYBWGGYGWWORRGOOOGROGGBYBBWGR  [score=16]
  L' : BYYGWWWWWBORBRROOBRRRBGYBBYYWGBYGOWOORGOOOGRRGGYYBYWGW  [score=16]
  U' : BBRWWYWWYGGWBRROOBBORBGYOBYWWGYYGYWOYRRROROOGGORYBGWGB  [score=15]
  F  : RYYBWWGRRBORWRRWOBOBYBGRYYROBBYYGYWOGOWROWOOGGGWYBGWGB  [score=15]
  F' : RYYBWWBBOGORWRRWOBRYYRGBYBORRGYYGYWOGOWROWOOBGGWYBGWGB  [score=15]
  D  : RYYBWWBWWBORBRRWGBYRRBGYOOBGGOWYWWYYGORROROBYGGWYBGOOG  [score=15]
  B' : ORGBWWBWWBORBRYOOYYRRBGYOBYWWGYYGBRRYORWOROOGWGBGBGGYW  [score=15]
  B  : RRBBWWBWWBOOBRWOOYYRRBGYOBYWWGYYGGROYORYORROGWYGGBGBGW  [score=13]

Algorithm: step 33 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 34
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 18
Previous move: D2

Current state:
RYYBWWBWWBORBRROOGYRRBGYWGBOWYGYYGWWGORROROOBGGWYBGOBY

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : YYYBWWWWWBORBRROOGORRGGYGGBYWYGYYWWWRRBOOOGROGGBYBBOBR  [score=24]
  U  : YWWYWWRBBYRRBRROOGGORBGYWGBOWYGYYGWWGGWROROOBBORYBGOBY  [score=20]
  U2 : WWBWWBYYRGORBRROOGGGWBGYWGBOWYGYYGWWBORROROOBYRRYBGOBY  [score=20]
  L' : YYYGWWWWWBORBRROOGRRRBGYBGBYWYBYYWWWORGOOOBRRGGGYBGOBO  [score=20]
  L2 : OYYGWWGWWBORBRROOGYRRGGYWGBRWYBYYBWWBOORORROGGGWYBBOBY  [score=20]
  B2 : WWGBWWBWWBOOBRROOGYRRBGYWGBOWYGYYYYRGORRORROBYBOGBYWGG  [score=20]
  F2 : RYYBWWYWOBORRRRROGBGWYGBRRYWWBGYYGWWGOOROBOOBGGWYBGOBY  [score=19]
  R2 : RYYBWYBWWGOORRBROBYROBGYWGGOWYGYWGWWGORROROOBBGWYBGRBY  [score=18]
  U' : BBRWWYWWYGGWBRROOGBORBGYWGBOWYGYYGWWYRRROROOBGORYBGOBY  [score=16]
  F  : RYYBWWBRRBORWRRWOGWBYGGRBYROBBGYYGWWGOOROWOOYGGWYBGOBY  [score=16]
  D  : RYYBWWBWWBORBRROBYYRRBGYOOGYYWWYWOGGGORRORWGBGGWYBGOOB  [score=16]
  B' : ORGBWWBWWBORBRYOOYYRRBGYWGBOWYGYYGRRGORWORWOBWGYGBBGYO  [score=16]
  R  : RYOBWYBWGRRGOROBBOYRYBGWWGWOWRGYYGWBGORROROOBWGWYBGYBY  [score=15]
  R' : RYRBWYBWBOBBOROGRRYRYBGYWGWOWOGYYGWGGORROROOBWGWWBGYBY  [score=15]
  F' : RYYBWWBBOYORWRROOGRYBRGGYBWRRBGYYGWWGOWROWOOBGGWYBGOBY  [score=15]
  D' : RYYBWWBWWBORBRRWGBYRRBGYOOBGGOWYWWYYGORROROBYGGWYBGOOG  [score=15]
  B  : RRGBWWBWWBOWBRWOOGYRRBGYWGBOWYGYYGROYORYORROBOYGBBGYGW  [score=15]

Algorithm: step 34 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 35
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 20
Previous move: L'

Current state:
YYYGWWWWWBORBRROOGRRRBGYBGBYWYBYYWWWORGOOOBRRGGGYBGOBO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  D2 : YYYGWWWWWBORBRRBRRRRRBGYOBOWWWYYBYWYORGOOOOOGGGGYBGBGB  [score=24]
  L2 : YYYBWWWWWBORBRROOGORRGGYGGBYWYGYYWWWRRBOOOGROGGBYBBOBR  [score=24]
  U  : YWWYWWYGWRRRBRROOGORGBGYBGBYWYBYYWWWGGGOOOBRRBORYBGOBO  [score=23]
  U2 : WWWWWGYYYORGBRROOGGGGBGYBGBYWYBYYWWWBOROOOBRRRRRYBGOBO  [score=23]
  B2 : WWWGWWWWWBOBBROOOORRRBGYBGBYWYBYYYYYGRGROORRROBOGBYGGG  [score=22]
  R2 : YYYGWYWWWGOORRBROBRROBGYBGGYWYBYWWWWORGOOOBRRBGGYBGRBO  [score=20]
  D  : YYYGWWWWWBORBRROBORRRBGYOOGYYWWYWYBWORGOOOBGBGGGYBGBRR  [score=20]
  D' : YYYGWWWWWBORBRRBGBRRRBGYBRRWBYWYWWYYORGOOOOBOGGGYBGOOG  [score=20]
  L' : OYYGWWGWWBORBRROOGYRRGGYWGBRWYBYYBWWBOORORROGGGWYBBOBY  [score=20]
  U' : WGYWWYWWYGGGBRROOGBORBGYBGBYWYBYYWWWRRROOOBRRORGYBGOBO  [score=18]
  R  : YYOGWYWWGRRGOROBBORRYBGWBGWYWRBYYWWBORGOOOBRRWGGYBGYBO  [score=17]
  R' : YYRGWYWWBOBBOROGRRRRYBGYBGWYWOBYYWWGORGOOOBRRWGGWBGYBO  [score=17]
  F2 : YYYGWWYWYRORORRGOGBGBYGBRRRWWWBYYWWWOROOOBBRBGGGYBGOBO  [score=17]
  B  : RRGGWWWWWBOWBRWOOWRRRBGYBGBYWYBYYOOBYRGYOOYRROYGBBGOGG  [score=16]
  B' : BOOGWWWWWBOYBRYOOYRRRBGYBGBYWYBYYGRRWRGWOOWRRGGOGBBGYO  [score=16]
  F  : YYYGWWROGWORWRRWOGBBRGGRBYROBBBYYWWWORYOOWBRYGGGYBGOBO  [score=14]
  F' : YYYGWWBBOYORWRRYOGRYBRGGRBBGORBYYWWWORWOOWBRWGGGYBGOBO  [score=14]

Algorithm: step 35 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 36
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: R

Current state:
YYOGWYWWGRRGOROBBORRYBGWBGWYWRBYYWWBORGOOOBRRWGGYBGYBO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L2 : YYOBWYWWGRRGOROBBOORYGGWGGWYWRGYYWWBRRBOOOGROWGBYBBYBR  [score=21]
  B2 : BWWGWYWWGRRBOROBBORRYBGWBGWYWRBYYOYYORGOOOGRROBYGBYGGW  [score=21]
  R  : YYYGWYWWWGOORRBROBRROBGYBGGYWYBYWWWWORGOOOBRRBGGYBGRBO  [score=20]
  D2 : YYOGWYWWGRRGOROBRRRRYBGWYBOBWWYYBRWYORGOOOBBOWGGYBGBGW  [score=19]
  D' : YYOGWYWWGRRGOROBGWRRYBGWBRRWBYWYWBYRORGOOOYBOWGGYBGBBO  [score=18]
  U  : OYGYWWYGWRRYOROBBOORGBGWBGWYWRBYYWWBWGGOOOBRRRRGYBGYBO  [score=17]
  U2 : GWWYWGOYYORGOROBBOWGGBGWBGWYWRBYYWWBRRGOOOBRRRRYYBGYBO  [score=17]
  R2 : YYRGWYWWBOBBOROGRRRRYBGYBGWYWOBYYWWGORGOOOBRRWGGWBGYBO  [score=17]
  L' : OYOGWYGWGRRGOROBBOYRYGGWWGWRWRBYYBWBBOORORROGWGWYBBYBY  [score=17]
  D  : YYOGWYWWGRRGOROYBORRYBGWBBORYBWYWYBWORGOOOBGWWGGYBGBRR  [score=16]
  B  : GOOGWYWWGRRBORWBBWRRYBGWBGWYWRBYYOOBORGYOOYRRYYWBBGOGG  [score=16]
  U' : WGYWWYGYOWGGOROBBORRGBGWBGWYWRBYYWWBRRYOOOBRRORGYBGYBO  [score=15]
  F2 : YYOGWYRWYRRGOROGBOWGBWGBYRRGWWBYYWWBORBOOOBRRWGGYBGYBO  [score=15]
  L  : RYOBWYBWGRRGOROBBOYRYBGWWGWOWRGYYGWBGORROROOBWGWYBGYBY  [score=15]
  B' : BOOGWYWWGRRYORYBBORRYBGWBGWYWRBYYOOGWRGWOOBRRGGOGBBWYY  [score=15]
  F' : YYOGWYROBRRGWROYBOYWWRGGRBBGORBYYWWBORGOOWBRWWGGYBGYBO  [score=13]
  F  : YYOGWYROGWRGWROGBOBBRGGRWWYBORBYYWWBORYOOWBRRWGGYBGYBO  [score=12]

Algorithm: step 36 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 37
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 15
Previous move: F2

Current state:
YYOGWYRWYRRGOROGBOWGBWGBYRRGWWBYYWWBORBOOOBRRWGGYBGYBO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R2 : YYWGWYRWBOBGOROGRRWGYWGYYRWGWOBYYWWYORBOOOBRRRGGBBGBBO  [score=19]
  L2 : GYOBWYWWYRRGOROGBOOGBGGBGRRYWWGYYRWBRRBOOOBROWGYYBWYBW  [score=19]
  B2 : BWWGWYRWYRRBOROGBOWGBWGBYRRGWWBYYOYYORBOOOGRROBYGBYGGW  [score=19]
  D' : YYOGWYRWYRRGOROYRRWGBWGBBRRWBGWYWBYWORBOOOYBOWGGYBGGBO  [score=18]
  L  : WYOWWYYWYRRGOROGBOGGBBGBWRROWWGYYGWBBORROROOBWGRYBGYBY  [score=18]
  L' : OYOGWYGWYRRGOROGBOYGBGGBRRRWWWWYYYWBBOORORROBWGWYBBYBG  [score=18]
  D2 : YYOGWYRWYRRGOROBRRWGBWGBYBOBWWYYBWWGORBOOOGBOWGGYBGYRR  [score=17]
  R  : YYYGWYRWWGOORRBROGWGOWGYYRYGWBBYBWWRORBOOOBRRBGGYBGWBO  [score=16]
  R' : YYBGWBRWRGORBRROOGWGWWGYYRBGWYBYYWWWORBOOOBRRYGGYBGOBO  [score=16]
  D  : YYOGWYRWYRRGOROYBOWGBWGBGBOWYBWYWGBWORBOOOYRRWGGYBGBRR  [score=16]
  U2 : YWRYWGOYYORBOROGBOWGGWGBYRRGWWBYYWWBRRGOOOBRRWGBYBGYBO  [score=15]
  B  : GOOGWYRWYRRBORWGBWWGBWGBYRRGWWBYYOOBORBYOOYRRYYWBBGOGG  [score=14]
  U' : RGYWWYYYOWGGOROGBORRGWGBYRRGWWBYYWWBWGBOOOBRRORBYBGYBO  [score=13]
  F  : YYOGWYROBRRGWROYBOYWWRGGRBBGORBYYWWBORGOOWBRWWGGYBGYBO  [score=13]
  B' : BOOGWYRWYRRYORYGBOWGBWGBYRRGWWBYYOOGWRBWOOBRRGGOGBBWYY  [score=13]
  F' : YYOGWYROGWRGWROGBOBBRGGRWWYBORBYYWWBORYOOWBRRWGGYBGYBO  [score=12]
  U  : OYYYWWYGRWGBOROGBOORBWGBYRRGWWBYYWWBWGGOOOBRRRRGYBGYBO  [score=11]

Algorithm: step 37 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
next_state = <54-char string copied from table before [score=>

---

## Actual LLM Prompt at Step 38 (default)

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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 38
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 19
Previous move: B2

Current state:
BWWGWYRWYRRBOROGBOWGBWGBYRRGWWBYYOYYORBOOOGRROBYGBYGGW

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L  : WWWWWYYWYRRBOROGBOGGBBGBORRWWWYYYYYYBORROROOGOBRGBGGGB  [score=25]
  D2 : BWWGWYRWYRRBOROGRRWGBWGBGGWYYOYYBWWGORBOOOGBOOBYGBYYRR  [score=24]
  R2 : BWWGWYRWYOBGOROBRRWGGWGGYROGWWBYYOYYORBOOOGRRRBYBBYBGW  [score=23]
  D' : BWWGWYRWYRRBOROYRRWGBWGBGRROBGYYWYYWORBOOOGGWOBYGBYGBO  [score=23]
  L' : WWWYWYYWYRRBOROGBOBGBGGBRRRWWWWYYYYYGOORORROBOBOGBBGGG  [score=23]
  F2 : BWWGWYWWGRRBOROBBORRYBGWBGWYWRBYYOYYORGOOOGRROBYGBYGGW  [score=21]
  D  : BWWGWYRWYRRBOROGGWWGBWGBGBOWYYWYYGBOORBOOOYRROBYGBYGRR  [score=20]
  L2 : GWWBWYOWYRRBOROGBOWGBYGBYRRBWWGYYRYYRRGOOOBROOBYGBWGGW  [score=19]
  F  : BWWGWYROBRRBWROYBOYWWRGGRBBGORBYYOYYORGOOWGRWOBYGBYGGW  [score=17]
  U  : WYYWWWBGRWGBOROGBOORBWGBYRRGWWBYYOYYOBYOOOGRRRRBGBYGGW  [score=16]
  U2 : YWRYWGWWBORBOROGBOOBYWGBYRRGWWBYYOYYRRBOOOGRRWGBGBYGGW  [score=16]
  R  : BWGGWGRWOBOORRBROGWGWWGYYRYGWBBYBOYRORBOOOGRRYBYYBYWGW  [score=16]
  R' : BWBGWBRWRGORBRROOBWGWWGYYRYGWGBYGOYOORBOOOGRRYBYYBYWGW  [score=16]
  F' : BWWGWYROGWRBWROGBOBBRGGRWWYBORBYYOYYORYOOWGRROBYGBYGGW  [score=16]
  U' : RGBWWWYYWOBYOROGBORRBWGBYRRGWWBYYOYYWGBOOOGRRORBGBYGGW  [score=15]
  B' : GOOGWYRWYRRBORWGBWWGBWGBYRRGWWBYYOOBORBYOOYRRYYWBBGOGG  [score=14]
  B  : BOOGWYRWYRRYORYGBOWGBWGBYRRGWWBYYOOGWRBWOOBRRGGOGBBWYY  [score=13]

Algorithm: step 38 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 39
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 23
Previous move: L'

Current state:
WWWYWYYWYRRBOROGBOBGBGGBRRRWWWWYYYYYGOORORROBOBOGBBGGG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  R2 : WWWYWYYWYOBGOROBRRBGGGGGRROWWWWYYYYYGOORORROBRBOBBBBGG  [score=27]
  F2 : WWWYWYWWWBRBRROOBORRRBGGBGBYWYWYYYYYGOGROOROROBOGBBGGG  [score=27]
  D2 : WWWYWYYWYRRBOROROBBGBGGBGGGYYYYYWWWWGOORORGBOOBOGBBRRR  [score=27]
  D' : WWWYWYYWYRRBORORRRBGBGGBROBYWWYYWYYWGOORORGGGOBOGBBGBO  [score=26]
  L2 : WWWWWYYWYRRBOROGBOGGBBGBORRWWWYYYYYYBORROROOGOBRGBGGGB  [score=25]
  D  : WWWYWYYWYRRBOROGGGBGBGGBGBOWYYWYYWWYGOORORRRROBOGBBROB  [score=24]
  U  : WYYWWWWYYBGBOROGBOGOOGGBRRRWWWWYYYYYOBORORROBRRBGBBGGG  [score=21]
  B2 : YYYYWYYWYRRRORRGBGBGBGGBRRRWWWWYYWWWOOOOORBOBGGGBBGOBO  [score=21]
  R  : WWGYWGYWOBOORRBROGBGWGGYRRYWWBWYBYYRGOORORROBYBOYBBWGG  [score=20]
  R' : WWBYWBYWRGORBRROOBBGWGGYRRYWWGWYGYYOGOORORROBYBOYBBWGG  [score=20]
  F  : WWWYWYBROYRBWROYBORGBRGGRBBGORWYYYYYGOWROWROWOBOGBBGGG  [score=20]
  F' : WWWYWYROGWRBWROWBOBBRGGRBGRORBWYYYYYGOYROWROYOBOGBBGGG  [score=20]
  U2 : YWYYWYWWWGOOOROGBOOBOGGBRRRWWWWYYYYYRRBRORROBBGBGBBGGG  [score=19]
  L' : GWWBWYOWYRRBOROGBOWGBYGBYRRBWWGYYRYYRRGOOOBROOBYGBWGGW  [score=19]
  U' : YYWWWWYYWOBOOROGBORRBGGBRRRWWWWYYYYYBGBRORROBGOOGBBGGG  [score=17]
  B  : BOOYWYYWYRRYORYGBYBGBGGBRRRWWWWYYGRRWOOWORWOBGGOGBBGBO  [score=17]
  B' : RRGYWYYWYRRWORWGBWBGBGGBRRRWWWWYYOOBYOOYORYOBOBGBBGOGG  [score=17]

Algorithm: step 39 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 40
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 17
Previous move: U'

Current state:
YYWWWWYYWOBOOROGBORRBGGBRRRWWWWYYYYYBGBRORROBGOOGBBGGG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  F2 : YYWWWWWWWBBORROBBORRRBGGBRRWYYWYYYYYBGGROOROOGOOGBBGGG  [score=24]
  U2 : WYYWWWWYYBGBOROGBOGOOGGBRRRWWWWYYYYYOBORORROBRRBGBBGGG  [score=21]
  D2 : YYWWWWYYWOBOOROROBRRBGGBGGGYYYYYWWWWBGBRORGBOGOOGBBRRR  [score=21]
  D' : YYWWWWYYWOBOORORRRRRBGGBROBYWWYYWYYWBGBRORGGGGOOGBBGBO  [score=20]
  B2 : YYYWWWYYWOBRORRGBBRRBGGBRRRWWWWYYWYYOGBOOROOBGGGBBGOOG  [score=20]
  U' : YWYYWYWWWGOOOROGBOOBOGGBRRRWWWWYYYYYRRBRORROBBGBGBBGGG  [score=19]
  R2 : YYWWWYYYYOBGOROOBORRGGGGRRGWWWWYWYYWBGBRORROBROOBBBBGG  [score=18]
  D  : YYWWWWYYWOBOOROGGGRRBGGBGBOWYYWYYWWYBGBRORRRRGOOGBBROB  [score=18]
  L2 : WYWWWWYYWOBOOROGBOGRBBGBORRYWWWYYYYYBORRORBGBGORGBGGGR  [score=18]
  F  : YYWWWWBRBYBOYROWBORGRRGRRBBGOOWYYYYYBGWROWROWGOOGBBGGG  [score=16]
  F' : YYWWWWOOGWBOWROWBOBBRRGRRGRBRBWYYYYYBGWROYROYGOOGBBGGG  [score=16]
  L  : RYWGWWRYWOBOOROGBOWRBWGBYRRGWWBYYOYYBRBGOOBRRGOYGBWGGY  [score=13]
  L' : GYWBWWOYWOBOOROGBOYRBWGBYRRRWWGYYRYYRRBOOGBRBGOYGBWGGW  [score=13]
  B  : OOOWWWYYWOBYORYGBYRRBGGBRRRWWWWYYBRRWGBYORYOBGGGGBOGBO  [score=13]
  B' : RRBWWWYYWOBYORYGBWRRBGGBRRRWWWWYYOOOYGBYORYOBOBGOBGGGG  [score=13]
  R  : YYGWWGYYGOOOBRBOOGRRWGGWRRWWWBWYBYYRBGBRORROBYOOYBBWGG  [score=12]
  R' : YYBWWBYYRGOOBRBOOORRWGGYRRYWWGWYGYYGBGBRORROBWOOWBBWGG  [score=12]

Algorithm: step 40 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 41
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 24
Previous move: F2

Current state:
YYWWWWWWWBBORROBBORRRBGGBRRWYYWYYYYYBGGROOROOGOOGBBGGG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  U  : WWWYWWYWWRRRRROBBOBGGBGGBRRWYYWYYYYYGOOROOROOBBOGBBGGG  [score=33]
  D2 : YYWWWWWWWBBORROROORRRBGGGGGYYYYYWYYWBGGROOBBOGOOGBBBRR  [score=28]
  B2 : YYYWWWWWWBBRRRRBBBRRRBGGBRRWYYWYYWYYOGGOOOOOOGGGBBGOOG  [score=27]
  U2 : WWWWWWWYYBGGRROBBOGOOBGGBRRWYYWYYYYYBBOROOROORRRGBBGGG  [score=26]
  D' : YYWWWWWWWBBORROBRRRRRBGGROOYWWYYYYYYBGGROOGGGGOOGBBBBO  [score=26]
  L2 : WYWWWWYWWBBORROBBOGRRBGGORRYYYWYYWYYOOROORGGBGOBGBBGGR  [score=26]
  U' : WWYWWYWWWGOORROBBOBBOBGGBRRWYYWYYYYYRRRROOROOBGGGBBGGG  [score=25]
  D  : YYWWWWWWWBBORROGGGRRRBGGBBOYYYYYYWWYBGGROOBRRGOOGBBROO  [score=22]
  R2 : YYYWWYWWYOBBORROBBRRGBGGBRGWYWWYWYYWBGGROOROOROOGBBRGG  [score=20]
  L  : RYWBWWBWWBBORROBBOWRRWGGYRRGYYBYYOYYGOOGOOBRRGOWGBWGGY  [score=20]
  L' : GYWBWWOWWBBORROBBOYRRWGGWRRRYYBYYBYYRRBOOGOOGGOYGBWGGW  [score=20]
  B  : OOOWWWWWWBBYRRYBBYRRRBGGBRRWYYWYYBRRWGGYOOYOOGGGGBOGBO  [score=20]
  B' : RRBWWWWWWBBYRRYBBWRRRBGGBRRWYYWYYOOOYGGYOOYOOOBGOBGGGG  [score=20]
  R  : YYGWWGWWGOOOBRBBRBRRWBGWBRWWYRWYGYYRBGGROOROOYOOYBBYGG  [score=17]
  R' : YYRWWGWWRBRBBRBOOORRYBGYBRYWYGWYGYYGBGGROOROOWOOWBBWGG  [score=17]
  F  : YYWWWWOOGWBOWROWBOBBRRGRRGRBRBWYYYYYBGWROYROYGOOGBBGGG  [score=16]
  F' : YYWWWWBRBYBOYROWBORGRRGRRBBGOOWYYYYYBGWROWROWGOOGBBGGG  [score=16]

Algorithm: step 41 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 42
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 27
Previous move: B2

Current state:
YYYWWWWWWBBRRRRBBBRRRBGGBRRWYYWYYWYYOGGOOOOOOGGGBBGOOG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L2 : WYYWWWWWWBBRRRRBBBGRRGGGGRRYYYWYYWYYOOOOOOGGOGGBBBBOOR  [score=34]
  U  : YWWYWWYWWRRRRRRBBBOGGBGGBRRWYYWYYWYYGGGOOOOOOBBRBBGOOG  [score=32]
  D' : YYYWWWWWWBBRRRRBRRRRRBGGOOOWWWYYYYYYOGGOOOOOGGGGBBGBBB  [score=31]
  U2 : WWWWWWYYYOGGRRRBBBGGGBGGBRRWYYWYYWYYBBROOOOOORRRBBGOOG  [score=28]
  D2 : YYYWWWWWWBBRRRROOORRRBGGOOGYYWYYWYYWOGGOOOBBBGGGBBGBRR  [score=26]
  U' : WWYWWYWWYGGGRRRBBBBBRBGGBRRWYYWYYWYYRRROOOOOOOGGBBGOOG  [score=25]
  L  : RYYBWWBWWBBRRRRBBBWRRWGGWRRGYYGYYGYYGOOGOOOOOGGWBBWOOY  [score=25]
  L' : GYYGWWGWWBBRRRRBBBYRRWGGWRRRYYBYYBYYOOOOOGOOGGGWBBWOOW  [score=25]
  D  : YYYWWWWWWBBRRRROOGRRRBGGBBBYYYYYYWWWOGGOOOBRRGGGBBGOOO  [score=24]
  R2 : YYYWWYWWYBBBRRRRBBRROBGBBRGWYYWYWWYWOGGOOOOOORGGGBGROG  [score=22]
  R  : YYOWWBWWGRRBBRBBRBRRYBGWBRWWYRWYGWYROGGOOOOOOYGGYBGYOG  [score=20]
  R' : YYRWWGWWRBRBBRBBRRRRYBGYBRYWYOWYBWYGOGGOOOOOOWGGWBGYOG  [score=20]
  F2 : YYYWWWYYWOBRORRGBBRRBGGBRRRWWWWYYWYYOGBOOROOBGGGBBGOOG  [score=20]
  B  : RRBWWWWWWBBYRRYBBWRRRBGGBRRWYYWYYOOOYGGYOOYOOOBGOBGGGG  [score=20]
  B' : OOOWWWWWWBBYRRYBBYRRRBGGBRRWYYWYYBRRWGGYOOYOOGGGGBOGBO  [score=20]
  F  : YYYWWWOOGWBRWRRWBBBBRRGRRGRBRBWYYWYYOGWOOYOOYGGGBBGOOG  [score=19]
  F' : YYYWWWBRBYBRYRRWBBRGRRGRRBBGOOWYYWYYOGWOOWOOWGGGBBGOOG  [score=19]

Algorithm: step 42 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 43
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 32
Previous move: U

Current state:
YWWYWWYWWRRRRRRBBBOGGBGGBRRWYYWYYWYYGGGOOOOOOBBRBBGOOG

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  L2 : WWWWWWWWWRRRRRRBBBGGGGGGRRRYYYYYYYYYOOOOOOGGGBBBBBBOOO  [score=42]
  D' : YWWYWWYWWRRRRRRBRROGGBGGOOOWWWYYYYYYGGGOOOOOGBBRBBGBBB  [score=36]
  L  : OWWBWWBWWRRRRRRBBBWGGWGGWRRGYYGYYRYYGOOGOOGOOBBYBBYOOY  [score=32]
  L' : GWWGWWRWWRRRRRRBBBYGGYGGYRROYYBYYBYYOOGOOGOOGBBWBBWOOW  [score=32]
  D2 : YWWYWWYWWRRRRRROOOOGGBGGOOGYYWYYWYYWGGGOOOBBBBBRBBGBRR  [score=31]
  D  : YWWYWWYWWRRRRRROOGOGGBGGBBBYYYYYYWWWGGGOOOBRRBBRBBGOOO  [score=29]
  U  : WWWWWWYYYOGGRRRBBBGGGBGGBRRWYYWYYWYYBBROOOOOORRRBBGOOG  [score=28]
  F2 : YWWYWWYYWORRORRGBBRRBGGBGGOWWYWYYWYYGGBOOROORBBRBBGOOG  [score=26]
  B2 : YYWYWWYWWRRORROBBGOGGBGGBRRWYYWYYWWYBGGROOROOGOOGBBRBB  [score=26]
  U2 : WWYWWYWWYGGGRRRBBBBBRBGGBRRWYYWYYWYYRRROOOOOOOGGBBGOOG  [score=25]
  F  : YWWYWWOOGYRRWRRWBBBBORGGRGGBRRWYYWYYGGWOOYOOYBBRBBGOOG  [score=24]
  F' : YWWYWWRRBYRRYRRWBBGGRGGROBBGOOWYYWYYGGWOOWOOYBBRBBGOOG  [score=24]
  B  : RRBYWWYWWRRYRRYBBWOGGBGGBRRWYYWYYGOOWGGWOOYOOOBBOBBGGR  [score=24]
  B' : OOGYWWYWWRRYRRWBBWOGGBGGBRRWYYWYYBRRWGGYOOYOORGGBBOBBO  [score=24]
  R  : YWOYWBYWBRRBRRBRRBOGWBGWBRWWYGWYGWYRGGGOOOOOOYBRYBGYOG  [score=22]
  R' : YWGYWGYWRBRRBRRBRROGYBGYBRYWYOWYBWYBGGGOOOOOOWBRWBGWOG  [score=22]
  R2 : YWYYWYYWYBBBRRRRRROGOBGBBRBWYWWYWWYWGGGOOOOOORBRGBGGOG  [score=22]

Algorithm: step 43 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
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

KNOWN SOLUTION ALGORITHM (44-move scramble inverse):
The scramble [D, L2, U', B2, F2, U, L, B2, F2, R', L, D2, F2, U', R', F', B', B2, L', D', F', D2, L2, R2, F, U2, R, U, R', U', F2, D, L, B', U2, R, D, B', U', L2, B, D, U2, R'] has exact inverse applied in this order:
  R → U2 → D' → B' → L2 → U → B → D' → R' → U2 → B → L' → D' → F2 → U → R → U' → R' → U2 → F' → R2 → L2 → D2 → F → D → L → B2 → B → F → R → U → F2 → D2 → L' → R → F2 → B2 → L' → U' → F2 → B2 → U → L2 → D'
Determine this step's move from the CURRENT STEP NUMBER using this table:
  step 1  → R
  step 2  → U2
  step 3  → D'
  step 4  → B'
  step 5  → L2
  step 6  → U
  step 7  → B
  step 8  → D'
  step 9  → R'
  step 10 → U2
  step 11 → B
  step 12 → L'
  step 13 → D'
  step 14 → F2
  step 15 → U
  step 16 → R
  step 17 → U'
  step 18 → R'
  step 19 → U2
  step 20 → F'
  step 21 → R2
  step 22 → L2
  step 23 → D2
  step 24 → F
  step 25 → D
  step 26 → L
  step 27 → B2
  step 28 → B
  step 29 → F
  step 30 → R
  step 31 → U
  step 32 → F2
  step 33 → D2
  step 34 → L'
  step 35 → R
  step 36 → F2
  step 37 → B2
  step 38 → L'
  step 39 → U'
  step 40 → F2
  step 41 → B2
  step 42 → U
  step 43 → L2
  step 44 → D'

TABLE FORMAT:
Each line in the lookup table has this format:
  move: NEXT_STATE  [score=N]
where NEXT_STATE is a 54-character color string and [score=N] is metadata.

INSTRUCTIONS:
1. Look up the CURRENT STEP NUMBER in the table above to determine this step's move.
2. Find the line in the lookup table whose move matches the determined move.
3. Copy next_state EXACTLY: it is the 54-character string BETWEEN ": " and "  [score=" on that line.
4. Do NOT compute or modify next_state — copy it character-by-character from the table.
5. If the determined move is not present in the lookup table, pick the FIRST entry instead.

REQUIREMENTS (STRICT):
- Output MUST contain a single next move in this EXACT FORMAT:
move = <one move token>
- Output MUST contain the next state after applying that move in this EXACT FORMAT:
next_state = <54-character string>
- Output MUST be EXACTLY TWO LINES (no extra text, no explanations, no markdown).
- next_state MUST be copied EXACTLY from the lookup table — the 54 characters before "[score=".


### User Prompt
Step: 44
Phase: full_solve
Goal: Continue toward the full solve.
Current score: 42
Previous move: L2

Current state:
WWWWWWWWWRRRRRRBBBGGGGGGRRRYYYYYYYYYOOOOOOGGGBBBBBBOOO

MOVE LOOKUP TABLE (find your determined move here, copy its next_state):
  D' : WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB  [score=54]
  D  : WWWWWWWWWRRRRRROOOGGGGGGBBBYYYYYYYYYOOOOOORRRBBBBBBGGG  [score=42]
  D2 : WWWWWWWWWRRRRRRGGGGGGGGGOOOYYYYYYYYYOOOOOOBBBBBBBBBRRR  [score=42]
  R  : WWOWWBWWBRRBRRBRRBGGWGGWRRWYYGYYGYYROOOOOOGGGYBBYBBYOO  [score=32]
  R' : WWGWWGWWRBRRBRRBRRGGYGGYRRYYYOYYBYYBOOOOOOGGGWBBWBBWOO  [score=32]
  R2 : WWYWWYWWYBBBRRRRRRGGOGGBRRBYYWYYWYYWOOOOOOGGGRBBGBBGOO  [score=32]
  F  : WWWWWWGOOWRRWRRWBBRGGRGGRGGBRRYYYYYYOOYOOYGGYBBBBBBOOO  [score=32]
  F' : WWWWWWRRBYRRYRRYBBGGRGGRGGROOGYYYYYYOOWOOWGGWBBBBBBOOO  [score=32]
  F2 : WWWWWWYYYGRRORROBBRRRGGGGGGWWWYYYYYYOOBOORGGRBBBBBBOOO  [score=32]
  L  : GWWGWWRWWRRRRRRBBBYGGYGGYRROYYBYYBYYOOGOOGOOGBBWBBWOOW  [score=32]
  L' : OWWBWWBWWRRRRRRBBBWGGWGGWRRGYYGYYRYYGOOGOOGOOBBYBBYOOY  [score=32]
  B  : RRBWWWWWWRRYRRYBBYGGGGGGRRRYYYYYYOOGWOOWOOWGGOBBOBBOBB  [score=32]
  B' : GOOWWWWWWRRWRRWBBWGGGGGGRRRYYYYYYBRRYOOYOOYGGBBOBBOBBO  [score=32]
  B2 : YYYWWWWWWRRGRROBBOGGGGGGRRRYYYYYYWWWBOOROORGGOOOBBBBBB  [score=32]
  U  : WWWWWWWWWGGGRRRBBBOOOGGGRRRYYYYYYYYYBBBOOOGGGRRRBBBOOO  [score=30]
  U' : WWWWWWWWWBBBRRRBBBRRRGGGRRRYYYYYYYYYGGGOOOGGGOOOBBBOOO  [score=30]
  U2 : WWWWWWWWWOOORRRBBBBBBGGGRRRYYYYYYYYYRRROOOGGGGGGBBBOOO  [score=30]

Algorithm: step 44 → this step's move = see table: 1→R, 2→U2, 3→D', 4→B', 5→L2, 6→U, 7→B, 8→D', 9→R', 10→U2, 11→B, 12→L', 13→D', 14→F2, 15→U, 16→R, 17→U', 18→R', 19→U2, 20→F', 21→R2, 22→L2, 23→D2, 24→F, 25→D, 26→L, 27→B2, 28→B, 29→F, 30→R, 31→U, 32→F2, 33→D2, 34→L', 35→R, 36→F2, 37→B2, 38→L', 39→U', 40→F2, 41→B2, 42→U, 43→L2, 44→D'
Find that move in the lookup table above. Copy its 54-character next_state (before "[score=") EXACTLY.
Output EXACTLY TWO LINES:
move = <determined move>
next_state = <54-char string copied from table before [score=>

---
