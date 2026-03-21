from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

Vec = Tuple[int, int, int]
StickerKey = Tuple[int, int, int, int, int, int]  # (x,y,z,nx,ny,nz)

CONFIGS = {
    "2-move": ["R", "U"],
    "4-move": ["R", "U", "R'", "U'"],
    "6-move": ["R", "U", "R'", "U'", "F2", "D"],
    "8-move": ["R", "U", "R'", "U'", "F2", "D", "L", "B'"],
    "10-move": ["R", "U", "R'", "U'", "F2", "D", "L", "B'", "U2", "R"],
    "12-move": ["R", "U", "R'", "U'", "F2", "D", "L", "B'", "U2", "R", "D'", "F"],
}


def _rot_x_p90(v: Vec) -> Vec:
    x, y, z = v
    return (x, -z, y)


def _rot_x_m90(v: Vec) -> Vec:
    x, y, z = v
    return (x, z, -y)


def _rot_y_p90(v: Vec) -> Vec:
    x, y, z = v
    return (z, y, -x)


def _rot_y_m90(v: Vec) -> Vec:
    x, y, z = v
    return (-z, y, x)


def _rot_z_p90(v: Vec) -> Vec:
    x, y, z = v
    return (-y, x, z)


def _rot_z_m90(v: Vec) -> Vec:
    x, y, z = v
    return (y, -x, z)


def _vec_to_key(pos: Vec, n: Vec) -> StickerKey:
    return (pos[0], pos[1], pos[2], n[0], n[1], n[2])


@dataclass
class RubiksCube:
    """
    Sticker-level cube model (54 stickers), deterministic transitions.
    Faces order (for state string): U, R, F, D, L, B (each 9 stickers).
    Colors default: U=W, D=Y, F=G, B=B, L=O, R=R.
    """
    state: str
    phase: str = "white_cross"
    last_phase_announcement: str = ""
    last_move: str = "None"

    # Configurable red-flag thresholds
    forbid_undo: bool = True
    max_score_drop: int = 3  # if a move drops score by more than this -> invalid

    # Internal mappings
    _idx_to_key: List[StickerKey] = None  # type: ignore
    _key_to_idx: Dict[StickerKey, int] = None  # type: ignore

    MOVES_18 = [
        "U", "U'", "U2",
        "R", "R'", "R2",
        "F", "F'", "F2",
        "D", "D'", "D2",
        "L", "L'", "L2",
        "B", "B'", "B2",
    ]

    @staticmethod
    def solved_state() -> str:
        return "W" * 9 + "R" * 9 + "G" * 9 + "Y" * 9 + "O" * 9 + "B" * 9

    @classmethod
    def from_config(
        cls,
        scramble: Optional[List[str]] = None,
        forbid_undo: bool = True,
        max_score_drop: int = 3,
    ):
        cube = cls(
            state=cls.solved_state(),
            forbid_undo=forbid_undo,
            max_score_drop=max_score_drop,
        )
        cube._init_mappings()
        if scramble:
            for mv in scramble:
                cube.apply_move(mv, validate=False)
            cube.last_move = "None"
            cube._update_phase()
        return cube

    def _init_mappings(self) -> None:
        """
        Build a bijection between (pos, normal) and sticker index.

        Coordinate system:
          x: -1 (L) .. +1 (R)
          y: -1 (D) .. +1 (U)
          z: -1 (B) .. +1 (F)

        For each face (normal), we define 3x3 grid mapping to positions.
        This mapping is consistent with a typical cube net visualization.
        """
        idx_to_key: List[StickerKey] = []

        def add_face(normal: Vec, grid_to_pos) -> None:
            for r in range(3):
                for c in range(3):
                    pos = grid_to_pos(r, c)
                    idx_to_key.append(_vec_to_key(pos, normal))

        # U (y=+1), viewed from +y: row0 is z=-1 (back), row2 is z=+1 (front)
        add_face((0, 1, 0), lambda r, c: (-1 + c, 1, -1 + r))
        # R (x=+1), viewed from +x: row0 is y=+1, row2 is y=-1; col0 is z=+1 (front) to col2 z=-1 (back)
        add_face((1, 0, 0), lambda r, c: (1, 1 - r, 1 - c))
        # F (z=+1), viewed from +z: row0 y=+1 to row2 y=-1; col0 x=-1 to col2 x=+1
        add_face((0, 0, 1), lambda r, c: (-1 + c, 1 - r, 1))
        # D (y=-1), viewed from -y: row0 is z=+1 (front), row2 z=-1 (back)
        add_face((0, -1, 0), lambda r, c: (-1 + c, -1, 1 - r))
        # L (x=-1), viewed from -x: row0 y=+1..; col0 z=-1 (back) to col2 z=+1 (front)
        add_face((-1, 0, 0), lambda r, c: (-1, 1 - r, -1 + c))
        # B (z=-1), viewed from -z: row0 y=+1..; col0 x=+1 to col2 x=-1 (because looking from back)
        add_face((0, 0, -1), lambda r, c: (1 - c, 1 - r, -1))

        key_to_idx: Dict[StickerKey, int] = {k: i for i, k in enumerate(idx_to_key)}
        if len(key_to_idx) != 54:
            raise RuntimeError("Sticker mapping is not bijective; check face definitions.")

        self._idx_to_key = idx_to_key
        self._key_to_idx = key_to_idx

    def get_state(self) -> str:
        return self.state

    def visualize(self) -> str:
        """
        Simple net visualization (U on top, L F R B in middle, D bottom).
        This is for debugging in terminal.
        """
        s = self.state
        U = [s[i:i+3] for i in range(0, 9, 3)]
        R = [s[i:i+3] for i in range(9, 18, 3)]
        F = [s[i:i+3] for i in range(18, 27, 3)]
        D = [s[i:i+3] for i in range(27, 36, 3)]
        L = [s[i:i+3] for i in range(36, 45, 3)]
        B = [s[i:i+3] for i in range(45, 54, 3)]

        lines = []
        lines.append("      " + U[0])
        lines.append("      " + U[1])
        lines.append("      " + U[2])
        for r in range(3):
            lines.append(L[r] + " " + F[r] + " " + R[r] + " " + B[r])
        lines.append("      " + D[0])
        lines.append("      " + D[1])
        lines.append("      " + D[2])
        return "\n".join(lines)

    def is_solved(self) -> bool:
        return self.state == self.solved_state()

    def compute_progress(self) -> float:
        sol = self.solved_state()
        correct = sum(1 for i in range(54) if self.state[i] == sol[i])
        return correct / 54

    def is_valid_state(self, state: str) -> str:
        """
        Required by your shared Parser interface.
        Must RETURN the state (not bool) and RAISE ValueError if invalid.
        """
        if not isinstance(state, str):
            raise ValueError("Invalid state: not a string.")
        if len(state) != 54:
            raise ValueError("Invalid state: must have length 54.")

        allowed = set("WRGYOB")
        if any(ch not in allowed for ch in state):
            raise ValueError("Invalid state: contains invalid color letters.")

        for c in "WRGYOB":
            if state.count(c) != 9:
                raise ValueError("Invalid state: each color must appear exactly 9 times.")

        return state

    def score(self, state: Optional[str] = None) -> int:
        """
        Phase-aware heuristic score.

        white_cross phase:
        - reward U center white + U cross whites
        - reward correct side alignment for those 4 cross edges
        full_solve phase:
        - fallback to solved-position stickers (simple baseline)
        """
        st = state if state is not None else self.state

        if self.phase == "white_cross":
            score = 0

            # U center
            if st[4] == "W":
                score += 3

            # U edges on U face: 1,3,5,7
            u_edges = [1, 3, 5, 7]
            score += sum(2 for i in u_edges if st[i] == "W")  # up to 8

            # Side alignment for those edges: F(19), R(10), B(46), L(37) should match face centers
            if st[19] == st[22]:
                score += 2
            if st[10] == st[13]:
                score += 2
            if st[46] == st[49]:
                score += 2
            if st[37] == st[40]:
                score += 2

            # total max in this phase: 3 + 8 + 8 = 19
            return score

        # full_solve (baseline)
        sol = self.solved_state()
        return sum(1 for i in range(54) if st[i] == sol[i])

    def _inverse_move(self, mv: str) -> str:
        if mv.endswith("2"):
            return mv
        if mv.endswith("'"):
            return mv[:-1]
        return mv + "'"

    def _apply_quarter_turn(self, mv: str, st: str) -> str:
        """
        Apply a single quarter turn (U,R,F,D,L,B) or its inverse by rotating a layer in 3D.
        """
        if mv not in ["U", "U'", "R", "R'", "F", "F'", "D", "D'", "L", "L'", "B", "B'"]:
            raise ValueError(f"Unsupported quarter move: {mv}")

        face = mv[0]
        prime = mv.endswith("'")

        if face == "U":
            axis = "y"; layer_val = 1; rot = _rot_y_p90 if not prime else _rot_y_m90
        elif face == "D":
            axis = "y"; layer_val = -1; rot = _rot_y_m90 if not prime else _rot_y_p90
        elif face == "R":
            axis = "x"; layer_val = 1; rot = _rot_x_p90 if not prime else _rot_x_m90
        elif face == "L":
            axis = "x"; layer_val = -1; rot = _rot_x_m90 if not prime else _rot_x_p90
        elif face == "F":
            axis = "z"; layer_val = 1; rot = _rot_z_m90 if not prime else _rot_z_p90
        elif face == "B":
            axis = "z"; layer_val = -1; rot = _rot_z_p90 if not prime else _rot_z_m90
        else:
            raise ValueError(f"Unknown face: {face}")

        chars = list(st)
        out = chars.copy()

        for idx, key in enumerate(self._idx_to_key):
            x, y, z, nx, ny, nz = key
            pos = (x, y, z)
            n = (nx, ny, nz)

            if (axis == "x" and x == layer_val) or (axis == "y" and y == layer_val) or (axis == "z" and z == layer_val):
                pos2 = rot(pos)
                n2 = rot(n)
                idx2 = self._key_to_idx[_vec_to_key(pos2, n2)]
                out[idx2] = chars[idx]

        return "".join(out)

    def peek_next_state(self, move: str) -> str:
        st = self.state
        if move.endswith("2"):
            base = move[0]
            st = self._apply_quarter_turn(base, st)
            st = self._apply_quarter_turn(base, st)
            return st
        return self._apply_quarter_turn(move, st)

    def validate_move(self, move: str) -> str:
        """
        Required by your shared Parser interface.
        Must RETURN the validated move (not None) and RAISE ValueError if invalid.
        Also applies heuristic red-flagging.
        """
        mv = move.strip()
        if mv not in self.MOVES_18:
            raise ValueError("Invalid move: not in allowed move set.")

        if self.forbid_undo and self.last_move not in ["None", ""]:
            if mv == self._inverse_move(self.last_move):
                raise ValueError("Invalid move: immediate undo move (loop prevention).")

        before = self.score(self.state)
        after_state = self.peek_next_state(mv)
        after = self.score(after_state)

        # In white_cross phase, be less strict: allow small drops (search needs wiggle room)
        # In full_solve phase, keep existing threshold.
        drop_limit = self.max_score_drop
        if self.phase == "white_cross":
            drop_limit = max(drop_limit, 2)  # ensure at least 2

        if after < before - drop_limit:
            raise ValueError("Invalid move: heuristic score drop too large.")

        return mv

    def apply_move(self, move: str, validate: bool = True) -> None:
        if validate:
            move = self.validate_move(move)

        st = self.state
        if move.endswith("2"):
            base = move[0]
            st = self._apply_quarter_turn(base, st)
            st = self._apply_quarter_turn(base, st)
        else:
            st = self._apply_quarter_turn(move, st)

        self.state = st
        self.last_move = move
        self._update_phase()

    def _update_phase(self) -> None:
        """
        Phase logic:
          - Start with white_cross
          - Once white_cross is solved -> phase=full_solve (for now)
        """
        if self.phase == "white_cross" and self.is_white_cross_solved():
            self.phase = "full_solve"

    def announce_phase_if_needed(self) -> Optional[str]:
        """
        Used by main loop (optional): produce a one-time message when a phase completes.
        """
        if self.phase == "full_solve" and self.last_phase_announcement != "white_cross_done":
            self.last_phase_announcement = "white_cross_done"
            return "✅ Phase complete: WHITE CROSS solved. Switching to FULL SOLVE."
        return None

    def is_white_cross_solved(self) -> bool:
        """
        Check a standard "white cross" on U face:
          - U center is W
          - U edges are W
          - Adjacent side stickers match their face centers at those edges
        """
        s = self.state
        if s[4] != "W":
            return False

        u_edges = [1, 3, 5, 7]
        if any(s[i] != "W" for i in u_edges):
            return False

        if s[19] != s[22]:
            return False
        if s[10] != s[13]:
            return False
        if s[46] != s[49]:
            return False
        if s[37] != s[40]:
            return False

        return True

    def check_next_state(self, current_state: str, move: str, next_state: str) -> None:
        """
        Optional MAKER guardrail: if LLM outputs next_state, ensure it matches applying move.
        """
        expected = self.peek_next_state(move.strip())
        if next_state.strip() != expected:
            raise ValueError("Invalid next_state: does not match applying move to current_state.")