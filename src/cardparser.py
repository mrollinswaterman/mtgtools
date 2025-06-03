from __future__ import annotations

class Card():
    def __init__(self, source:dict):
        self.report:ScoreReport = ScoreReport(self)
        self.name = source["name"]
        self.cmc = source["cmc"]
        self.type_line = source["type_line"]
        self.oracle_text = source["oracle_text"]

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
    
def create_df_card(data:dict) -> list[Card]:
    front = data
    for i in data["card_faces"][0]:
        front[i] = data["card_faces"][0][i]

    back = data
    for i in data["card_faces"][1]:
        back[i] = data["card_faces"][1][i]

    back["cmc"] = parse_mana_cost(back["mana_cost"])

    return [Card(front), Card(back)]

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

class ScoreReport():
    
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

    def __str__(self):
        if self.score is not None:
            return f"{self.card.name}: {self.score}"
        else: return ""
