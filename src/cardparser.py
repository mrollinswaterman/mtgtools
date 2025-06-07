from __future__ import annotations

import re


class Card:
    def __init__(self, source: dict, mode: str):
        from math_mode.math_report import MathReport

        self.report: MathReport = None

        if mode == "" or mode == "math":
            self.report: MathReport = MathReport(self)
        elif mode == "score":
            self.report: ScoreReport = ScoreReport(self)

        self.name = source["name"]
        self.cmc = source["cmc"]
        self.type_line = source["type_line"]
        self.oracle_text = source["oracle_text"]

        # strip reminder text
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


class ScoreReport:
    pass


def create_df_card(data: dict, mode: str) -> list[Card]:
    front = data
    for i in data["card_faces"][0]:
        front[i] = data["card_faces"][0][i]

    back = data
    for i in data["card_faces"][1]:
        back[i] = data["card_faces"][1][i]

    back["cmc"] = parse_mana_cost(back["mana_cost"])

    return [Card(front, mode), Card(back, mode)]


def parse_mana_cost(input: str) -> float:
    if input == "":
        return ""
    colorless_index = input.index("}") + 1
    colorless = input[0:colorless_index]
    input = input[colorless_index:]
    color = input.count("{")

    try:
        colorless = int(colorless[1:-1])
    except TypeError:
        color += 1
        colorless = 0.0

    return float(colorless + color)


def parse_num(text: str) -> int | bool:
    from constants import TO_NUM

    if text in TO_NUM:
        return TO_NUM[text]
    else:
        return False
