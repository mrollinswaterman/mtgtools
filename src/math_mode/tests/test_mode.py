import pytest
from src.cardfetcher import fetch
from src.cardparser import Card

MASTER_LIST = [
    "Kudo, King Among Bears", # 1.0
    "Lightning Skelemental", # 2.0
    "Blood Artist", # 0.0
    "Village Rites", # None
    "Doomed Traveler"
]

CONTROL = {
    "pow2cmc": {"Kudo, King Among Bears": 1.0,
                "Lightning Skelemental": 2.0,
                "Blood Artist": 0.0,
                "Village Rites": None,
                "Doomed Traveler": 1.0},

    "tou2cmc": {"Kudo, King Among Bears": 1.0,
                "Lightning Skelemental": 0.3333333333333333,
                "Blood Artist": 0.5,
                "Village Rites": None,
                "Doomed Traveler": 1.0},
    
    "draw2cmc": {"Kudo, King Among Bears": None,
                "Lightning Skelemental": None,
                "Blood Artist": None,
                "Village Rites": 2.0,
                "Doomed Traveler": None},

    "tokens2cmc": {"Kudo, King Among Bears": None,
                "Lightning Skelemental": None,
                "Blood Artist": None,
                "Village Rites": None,
                "Doomed Traveler": 1.0},
}

objects:list[Card] = fetch(MASTER_LIST, "math")

cards = {name:card for (name,card) in zip(MASTER_LIST, objects)}

def test_cards():
    for name in MASTER_LIST:
        assert cards[name].name == name

def run_parameter_test(parameter:str):
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

def test_draw2cmc():
    run_parameter_test("draw2cmc")
