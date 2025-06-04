COLORS = {
    "": "COLORLESS",
    "W": "WHITE",
    "U": "BLUE",
    "B": "BLACK",
    "R": "RED",
    "G": "GREEN",
    "BW": "ORZHOV",
    "BU": "DIMIR",
    "BR": "RAKDOS",
    "BG": "GOLGARI",
    "UW": "AZORIUS",
    "RU": "IZZET",
    "GU": "SIMIC",
    "RW": "BOROS",
    "GW": "SELANI",
    "GR": "GRUUL",
}

TO_NUM = {
    "x": 1,
    "an": 1,
    "a": 1,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7
}

REMOVAL = {
    "destroy": 0,
    "exile": .3,
    "remove": .3
}

PERMANENT_TYPES = {
    "creature": 0.25,
    "artifact": 0.3141,
    "enchantment": 0.3141,
    "planeswalker": 0.125,
    "permanent": 1.5
}

SPELL_TYPES = {
    "instant": 0.45,
    "sorcery": 0
}
