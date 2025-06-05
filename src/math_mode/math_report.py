from cardparser import Card, parse_num

class MathReport():
    
    def __init__(self, target:Card):
        self.card:Card = target
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
        else: self._score = None

    def tou2cmc(self) -> None:
        if not self.card.toughness:
            self._score = None
            return
        if self.card.toughness.isdigit():
            self._score = int(self.card.toughness) / self.card.cmc
        else: self._score = None

    def find_star(self, pattern_string) -> bool:
        pattern_chunks = pattern_string.split("*")
        flag1 = pattern_chunks[0]
        flag2 = pattern_chunks[1]
        search_in = self.card.oracle_text

        # find flag 1, move pointer to flag1's index
        flag1_idx = search_in.find(flag1)
        if flag1_idx == -1: return ""
        search_in = search_in[flag1_idx:]

        #starting from the new pointer, find flag2
        flag2_idx = search_in.find(flag2)
        if flag2_idx == -1: return ""

        # return the chunk of text between flag1 and flag2
        star = search_in[len(flag1)+1:flag2_idx]
        return star.strip()
    
    def draw2cmc(self) -> None:

        card_count = self.find_star("raw*card")
        card_count = parse_num(card_count)
        if not card_count: 
            self._score = None
            return

        self._score = card_count / self.card.cmc
        return

    def __str__(self):
        if self.score is not None:
            return f"{self.card.name}: {self.score}"
        else: return ""