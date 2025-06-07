import re

from cardparser import Card, parse_num


class MathReport:
    def __init__(self, target: Card):
        self.card: Card = target
        self._score = 0

    @property
    def score(self):
        return self._score

    def pow2cmc(self) -> None:
        if not self.card.power:
            self._score = None
            return
        if self.card.power.isdigit():
            self._score = int(self.card.power) / self.card.cmc
        else:
            self._score = None

    def tou2cmc(self) -> None:
        if not self.card.toughness:
            self._score = None
            return
        if self.card.toughness.isdigit():
            self._score = int(self.card.toughness) / self.card.cmc
        else:
            self._score = None

    def match_exp(self, exp):
        return re.search(exp, self.card.oracle_text)

    def draw2cmc(self) -> None:
        # regex to find out if a card draws cards
        exp = r"[Dd]raw[s]* .* card"
        match = self.match_exp(exp)

        # if we find a match in our oracle text:
        if match:
            # pull out the stringified number (ie. "a", "two", "four", etc)
            cards = self.card.oracle_text[match.start() : match.end()]
            cards = cards[cards.find(" ") + 1 :]
            cards = cards[0 : cards.find(" ")]

            # parse it and find the card's score
            self._score = parse_num(cards) / self.card.cmc
        else:
            self._score = None
        return

    def tokens2cmc(self) -> None:
        # see draw2cmc function for an explanation of what this does

        exp = r"[Cc]reate .* [X\d]/[X\d]"
        match = self.match_exp(exp)
        if match:
            tokens = self.card.oracle_text[match.start() + len("create ") :]
            tokens = tokens[0 : tokens.find(" ")]
            self._score = parse_num(tokens) / self.card.cmc
        else:
            self._score = None
        return

    def __str__(self):
        if self.score is not None:
            return f"{self.card.name}: {self.score}"
        else:
            return ""
