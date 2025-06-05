import pytest
from src.cardfetcher import fetch
from src.cardparser import Card

MASTER_LIST = [
    "Kudo, King Among Bears", # 1.0
    "Lightning Skelemental", # 2.0
    "Blood Artist", # 0.0
    "Village Rites" # None
]

cards:list[Card] = fetch(MASTER_LIST, "math")

def test_cards():
    assert cards[0].name == MASTER_LIST[0]
    assert cards[1].name == MASTER_LIST[1]
    assert cards[2].name == MASTER_LIST[2]
    assert cards[3].name == MASTER_LIST[3]

def test_pow2cmc():
    skipped = 0

    test_objects = cards

    final:list[Card] = []

    for card in test_objects:
        analyze = getattr(card.report, "pow2cmc")
        analyze()
        if card.report.score is None: 
            skipped += 1
        else: final.append(card)

        assert skipped == 1
        #assert