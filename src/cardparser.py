from __future__ import annotations
import re

class Card():
    def __init__(self, source:dict, mode:str):

        if mode == "" or mode == "math":
            self.report:MathReport = MathReport(self)
        elif mode == "score":
            self.report:ScoreReport = ScoreReport(self)

        self.name = source["name"]
        self.cmc = source["cmc"]
        self.type_line = source["type_line"]
        self.oracle_text = source["oracle_text"]

        #strip reminder text
        reminder = r"\(.*.\)"

        while "(" in self.oracle_text:
            self.oracle_text = re.sub(reminder, "", self.oracle_text)

        self.mana_cost = source["mana_cost"]
        self.power = None
        self.toughness = None
        self.keywords = None

        if "Creature" in self.type_line:
            self.power = source["power"]
            self.toughness = source["toughness"]
            self.keywords = source["keywords"]

    def __str__(self):
        return f"{self.cmc} | {self.name}"

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

class ScoreReport():
    pass

def create_df_card(data:dict, mode:str) -> list[Card]:
    front = data
    for i in data["card_faces"][0]:
        front[i] = data["card_faces"][0][i]

    back = data
    for i in data["card_faces"][1]:
        back[i] = data["card_faces"][1][i]

    back["cmc"] = parse_mana_cost(back["mana_cost"])

    return [Card(front, mode), Card(back, mode)]

def parse_mana_cost(input:str) -> float:
    if input == "":
        return ""
    colorless_index = input.index("}")+1
    colorless = input[0:colorless_index]
    input = input[colorless_index:]
    color = input.count("{")

    try:
        colorless = int(colorless[1:-1])
    except TypeError:
        color += 1
        colorless = 0.0
    
    return float(colorless + color)

def parse_num(text:str) -> int|bool:
    from constants import TO_NUM
    if text in TO_NUM: return TO_NUM[text]
    else: return False