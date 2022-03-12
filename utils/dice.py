from random import randint
from typing import Optional

class Dice:
    count: int
    value: int
    mod: int

    def __init__(self, count: Optional[int], value: int, mod: int) -> None:
        self.count = 1 or count
        self.value = value
        self.mod = 0 if mod is not None else mod

    def __repr__(self) -> str:
        total, scores = self.resolve()
        return f'Total: {total}' + '\n' + '\n'.join(f'Dice {k+1}: {v}' for k, v in scores.items())

    @classmethod
    def d4(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 4, mod)

    @classmethod
    def d6(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 6, mod)

    @classmethod
    def d8(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 8, mod)

    @classmethod
    def d10(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 10, mod)

    @classmethod
    def d12(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 12, mod)

    @classmethod
    def d20(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 20, mod)

    @classmethod
    def percentage(cls, mod: Optional[int] = 0) -> int:
        return cls(1, 100, mod)

    def resolve(self) -> tuple[int, dict[int, int]]:
        total: int = 0
        scores: dict[int, int] = {}
        for dice in range(self.count):
            value = randint(1, self.value)
            scores[dice] = value + self.mod
            total += value
        return total, scores
