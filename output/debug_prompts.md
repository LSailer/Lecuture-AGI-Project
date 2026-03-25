
## Actual LLM Prompt at Step 1 (default)

### System Prompt
Rubik's Cube solver. 54-char state: W/R/G/Y/O/B.
Faces: U=s[0:9] R=s[9:18] F=s[18:27] D=s[27:36] L=s[36:45] B=s[45:54].
Solved: WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB

FACE ROTATION (use col values c0/c1/c2 from expand table — no F[N] indexing):
  CW  (U/R/D/L face CW, or F/B face CCW): new_r0=c2  new_r1=c1  new_r2=c0
  CCW (U/R/D/L face CCW, or F/B face CW): new_r0=rev(c0)  new_r1=rev(c1)  new_r2=rev(c2)
  X2: new_r0=rev(r2)  new_r1=rev(r1)  new_r2=rev(r0)
  [rev(XYZ)=ZYX; e.g. rev(BWY)=YWB]

EDGE CYCLES (A→B: new B = old A; rev=reverse 3 chars):
R CW:  R-face CW;  U-c2→F-c2→D-c2→B-c0(rev)
R' CCW: R-face CCW; F-c2→U-c2→B-c0(rev)→D-c2
U CW:  U-face CW;  F-r0→R-r0→B-r0→L-r0
U' CCW: U-face CCW; R-r0→F-r0→L-r0→B-r0
F CW:  F-face CW;  U-r2→R-c0→D-r0(rev)→L-c2(rev)
F' CCW: F-face CCW; R-c0→U-r2→L-c2(rev)→D-r0(rev)
D CW:  D-face CW;  R-r2→F-r2→L-r2→B-r2
D' CCW: D-face CCW; F-r2→R-r2→B-r2→L-r2
L CW:  L-face CW;  F-c0→U-c0→B-c2(rev)→D-c0
L' CCW: L-face CCW; U-c0→F-c0→D-c0→B-c2(rev)
B CW:  B-face CW;  R-c2(rev)→U-r0→L-c0(rev)→D-r2
B' CCW: B-face CCW; U-r0→R-c2(rev)→D-r2→L-c0(rev)

ASSEMBLY (read r0/r1/r2/c0/c1/c2 from expand table):
  r0-updated (edge e=3c): r0_new=e  r1_new=r1  r2_new=r2
  r2-updated (edge e=3c): r0_new=r0  r1_new=r1  r2_new=e
  c0-updated (e=e0e1e2):  r0_new=e0+r0[1:3]  r1_new=e1+r1[1:3]  r2_new=e2+r2[1:3]
  c2-updated (e=e0e1e2):  r0_new=r0[0:2]+e0  r1_new=r1[0:2]+e1  r2_new=r2[0:2]+e2
  [r0[0:2]=first 2 chars; r0[1:3]=last 2 chars; e.g. r0=ABC → r0[0:2]=AB, r0[1:3]=BC]
  unchanged: r0_new=r0  r1_new=r1  r2_new=r2
  rotating face: apply rotation formula above
Write each face as: new_X=r0_new|r1_new|r2_new  (| separators only; each piece is exactly 3 chars)

NEXT_STATE: after writing all new_X lines, write ns[N..M]=<9c> for each face.
ns rule: copy new_X chars left→right skipping |. Each piece is 3c; total = 3+3+3 = 9c always.
BOUNDARY NOTE: if piece1 ends with char C and piece2 starts with C, they are still separate: e.g.
  GGG|GRR → skip | → G G G G R R = GGGGR R (6c for these 2 pieces). ORR|GGG|GRR = 3+3+3 = 9c → ORRGGGGRR (4 Gs, not 5).
next_state = ns[0..8]+ns[9..17]+ns[18..26]+ns[27..35]+ns[36..44]+ns[45..53] (54c, no spaces).

EXAMPLE — move U' on BBBWWWWWWGGWRRRRRROOOGGWGGWYYGYYGYYGYBBOOOOOORRRYBBYBB:
(Expand tables in user prompt)
edge U' (R-r0→F-r0→L-r0→B-r0): R_r0=GGW F_r0=OOO L_r0=YBB B_r0=RRR
  → new_R_r0=RRR new_F_r0=GGW new_L_r0=OOO new_B_r0=YBB
rotate U CCW: new_r0=rev(c0)=rev(BWW)=WWB  new_r1=rev(c1)=rev(BWW)=WWB  new_r2=rev(c2)=rev(BWW)=WWB
new_U=WWB|WWB|WWB
new_R=RRR|RRR|RRR
new_F=GGW|GGW|GGW
new_D=YYG|YYG|YYG
new_L=OOO|OOO|OOO
new_B=YBB|YBB|YBB
ns[0..8]=WWBWWBWWB
ns[9..17]=RRRRRRRRR
ns[18..26]=GGWGGWGGW
ns[27..35]=YYGYYGYYG
ns[36..44]=OOOOOOOOO
ns[45..53]=YBBYBBYBB
move = U'
next_state = WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB


### User Prompt
Step:1 Score:17 Prev:None
Allowed:U, U', U2, R, R', R2, F, F', F2, D, D', D2, L, L', L2, B, B', B2
State:WWBWWBWWBRRRRRRRRRGGWGGWGGWYYGYYGYYGOOOOOOOOOYBBYBBYBB
Expand (read r0/r1/r2/c0/c1/c2 from here — do NOT re-read State string):
U: r0=WWB r1=WWB r2=WWB  c0=WWW c1=WWW c2=BBB
R: r0=RRR r1=RRR r2=RRR  c0=RRR c1=RRR c2=RRR
F: r0=GGW r1=GGW r2=GGW  c0=GGG c1=GGG c2=WWW
D: r0=YYG r1=YYG r2=YYG  c0=YYY c1=YYY c2=GGG
L: r0=OOO r1=OOO r2=OOO  c0=OOO c1=OOO c2=OOO
B: r0=YBB r1=YBB r2=YBB  c0=YYY c1=BBB c2=BBB
Solved-U=WWWWWWWWW Solved-R=RRRRRRRRR Solved-F=GGGGGGGGG Solved-D=YYYYYYYYY Solved-L=OOOOOOOOO Solved-B=BBBBBBBBB
Mismatched edges (compare expand c2/c0 to solved): U-c2=BBB(solved=WWW) F-c2=WWW(solved=GGG) D-c2=GGG(solved=YYY) B-c0=YYY(solved=BBB)
Hint: if U-c2≠WWW or F-c2≠GGG or D-c2≠YYY or B-c0≠BBB, the R-column cycle is displaced — apply R or R' to fix.

RESPOND WITH ONLY THIS FORMAT (no preamble):
edge [move] ([cycle_desc]): [src_values] → new_[X]_r0=[3c] ...
rotate [face] ([dir]): new_r0=[3c]  new_r1=[3c]  new_r2=[3c]
new_U=[3c]|[3c]|[3c]
new_R=[3c]|[3c]|[3c]
new_F=[3c]|[3c]|[3c]
new_D=[3c]|[3c]|[3c]
new_L=[3c]|[3c]|[3c]
new_B=[3c]|[3c]|[3c]
ns[0..8]=<9c: new_U without |>
ns[9..17]=<9c: new_R without |>
ns[18..26]=<9c: new_F without |>
ns[27..35]=<9c: new_D without |>
ns[36..44]=<9c: new_L without |>
ns[45..53]=<9c: new_B without |>
move = <token>
next_state = <54c: copy ns[0..8]ns[9..17]ns[18..26]ns[27..35]ns[36..44]ns[45..53] joined — NO spaces>


---
