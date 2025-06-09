from cardparser import Card
from math_mode.math_report import MathReport


class ScoreReport(MathReport):
    def __init__(self, target: Card):
        self.card: Card = target
        self._score = 0

    def pow2cmc(self) -> None:
        super().pow2cmc()
        if self.card.keywords:
            self._score += len(self.card.keywords)
        return
