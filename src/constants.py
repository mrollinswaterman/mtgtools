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


# Keyword Weights:
# Each keyword gives +1 to the cards score, plus the weight listed below
KEYWORDS = {
    "Annihilator": 2.0,
    "Cascade": 1.5,
    "Deathtouch": 0.5,
    "Double strike": 0.75,
    "First strike": 0.5,
    "Flying": 1.25,
    "Haste": 0.5,
    "Hexproof": 1.0,
    "Indestructible": 1.25,
    "Lifelink": 0.2,
    "Trample": 0.5,
    "Vigilance": 0.25,
    "Ward": 0.75,
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
    "seven": 7,
}

REMOVAL = {"destroy": 0, "exile": 0.3, "remove": 0.3}

PERMANENT_TYPES = {
    "creature": 0.25,
    "artifact": 0.3141,
    "enchantment": 0.3141,
    "planeswalker": 0.125,
    "permanent": 1.5,
}

SPELL_TYPES = {"instant": 0.45, "sorcery": 0}
