import pytest
import src
import src.cardfetcher

MASTER_LIST = [
    "Kudo, King Among Bears", # 1.0
    "Lightning Skelemental", # 2.0
    "Blood Artist", # 0.0
    "Village Rites" # None
]

test_objects = src.cardfetcher.fetch(MASTER_LIST, "math")

def test_card_objects():
    assert test_objects[0].name == MASTER_LIST[0]
    assert test_objects[1].name == MASTER_LIST[1]
    assert test_objects[2].name == MASTER_LIST[2]
    assert test_objects[3].name == MASTER_LIST[3]

test_card_objects()