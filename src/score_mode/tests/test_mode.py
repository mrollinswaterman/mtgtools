from constants import KEYWORDS
from src.cardfetcher import fetch
from src.cardparser import Card

MASTER_LIST = [
    "Shrike Force",
    "Lightning Skelemental",
    "Blood Artist",
    "Village Rites",
    "Doomed Traveler",
]

objects: list[Card] = fetch(MASTER_LIST, "score")

cards = {name: card for (name, card) in zip(MASTER_LIST, objects)}


def find_keyword_score(card_name: str):
    kw_score = 0
    if cards[card_name].keywords:
        kw_score += len(cards[card_name].keywords)
        for kw in cards[card_name].keywords:
            kw_score += KEYWORDS[kw]

    return kw_score


CONTROL = {
    "pow2cmc": {
        "Shrike Force": (1.0 + find_keyword_score("Shrike Force")) / 3.0,
        "Lightning Skelemental": (6.0 + find_keyword_score("Lightning Skelemental"))
        / 3.0,
        "Blood Artist": 0.0,
        "Village Rites": None,
        "Doomed Traveler": 1.0,
    },
    "tou2cmc": {
        "Shrike Force": (3.0 + find_keyword_score("Shrike Force")) / 3.0,
        "Lightning Skelemental": (1.0 + find_keyword_score("Lightning Skelemental"))
        / 3.0,
        "Blood Artist": 0.5,
        "Village Rites": None,
        "Doomed Traveler": 1.0,
    },
    "draw2cmc": {
        "Shrike Force": None,
        "Lightning Skelemental": None,
        "Blood Artist": None,
        "Village Rites": 2.0,
        "Doomed Traveler": None,
    },
    "tokens2cmc": {
        "Shrike Force": None,
        "Lightning Skelemental": None,
        "Blood Artist": None,
        "Village Rites": 2.0,
        "Doomed Traveler": 1.0,
    },
}


def test_cards():
    for name in MASTER_LIST:
        assert cards[name].name == name


def run_parameter_test(parameter: str):
    test_objects = cards
    for card_name in test_objects:
        card = test_objects[card_name]
        analyze = getattr(card.report, parameter)
        analyze()

    for card_name in CONTROL[parameter]:
        assert test_objects[card_name].report.score == CONTROL[parameter][card_name]


def test_pow2cmc():
    run_parameter_test("pow2cmc")


def test_tou2cmc():
    run_parameter_test("tou2cmc")
