from __future__ import annotations

import random
from typing import ClassVar

MOVES = Literal["R", "L", "U", "D", "F", "B"]
MODIFIERS = Literal["", "'", "2"]

# 0 -> R/L, 1 -> U/D, 2 -> F/B
_AXIS_OF: dict[MOVES, int] = {"R": 0, "L": 0, "U": 1, "D": 1, "F": 2, "B": 2}

class Scrambler:

    @classmethod
    def generate_scramble(cls, length: int = 20) -> str:
        """Generate a WCA 3x3x3 scramble of given length."""
        scramble = []
        last_face = None
        second_last_face = None

        for _ in range(length):
            available_moves = [
                m
                for m in cls.MOVES
                if m != last_face
                and (last_face is None or m != cls._opposite_face(last_face))
                and not (m == second_last_face and cls._opposite_face(m) == last_face)
            ]

            if not available_moves:
                available_moves = [m for m in cls.MOVES if m != last_face]

            face = random.choice(available_moves)
            modifier = random.choice(cls.MODIFIERS)

            scramble.append(f"{face}{modifier}")

            second_last_face = last_face
            last_face = face

        return " ".join(scramble)

    @staticmethod
    def _opposite_face(face: str) -> str:
        opposites = {"R": "L", "L": "R", "U": "D", "D": "U", "F": "B", "B": "F"}
        return opposites.get(face, "")
