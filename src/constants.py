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

KEYWORDS = {
    "Haste": 1.0,
    "Double strike": 1.25,
    "First strike": 1.0,
    "Trample": 1.25,
    "Flying": 1.25,
    "Deathtouch": 0.9,
    "Vigilance": 0.70,
    "Cascade": 1.0,
    "Annihilator": 1.75,
    "Hexproof": 1.75,
    "Ward": 1.5,
    "Lifelink": 0.9,
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
