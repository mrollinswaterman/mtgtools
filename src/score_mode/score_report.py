from cardparser import Card
from constants import KEYWORDS
from math_mode.math_report import MathReport


class ScoreReport(MathReport):
    def __init__(self, target: Card):
        super().__init__(target)

    def keyword_score(self) -> float:
        keyword_score = 0.0
        if self.card.keywords:
            keyword_score += len(self.card.keywords)
            for word in self.card.keywords:
                if word in KEYWORDS:
                    keyword_score += KEYWORDS[word]
        return keyword_score

    def pow2cmc(self) -> None:
        super().pow2cmc()

        if self.score is None:
            return

        self._score = 0
        if self.card.power.isdigit():
            numerator = int(self.card.power)
        else:
            numerator = 0

        numerator += self.keyword_score()

        self._score = numerator / self.card.cmc

        return

    def tou2cmc(self):
        super().tou2cmc()
        if self.score is None:
            return

        self._score = 0
        if self.card.toughness.isdigit():
            numerator = int(self.card.toughness)
        else:
            numerator = 0

        numerator += self.keyword_score()

        return numerator / self.card.cmc
