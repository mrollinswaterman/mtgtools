import json

import constants

data = []
ORCALE = []

class Card():

    def __init__(self, name:str, source:dict[str, str]):

        self.name = name.lower()
        self.cost = source["cmc"]
        self.text = self.words = self.color = None
        self.caveat = False
        self.raw_data = source
        self.value = 0
        self.type = source["type_line"].lower()

        #set text and words_list if applicable
        if "oracle_text" in source:
            self.text = source["oracle_text"].lower()
            self.text = self.text.replace("\n", " ")
            self.text = self.text.replace(",", "")
            self.words = self.text.split(" ")

            if "whenever" in self.text:
                self.caveat = True

        #determine card's color combo, if applicable
        if "colors" in source:
            self.my_colors = ""
            for color in source["colors"]:
                self.my_colors = self.my_colors + color
            if self.my_colors in constants.COLORS:
                self.color = constants.COLORS[self.my_colors]

        #add heuristic based on card's spell type
        for type in constants.SPELL_TYPES:
            if type in self.type:
                self.value += constants.SPELL_TYPES[type]

    @property
    def score(self):
        if not self.value: return 0
        if self.cost == 0: return self.value
        return self.value/self.cost

    def filter(self, func):
        self.find_additional_costs()
        func(self)

    def find(self, phrase) -> tuple[str, int]:
        word = True
        if " " in phrase:
            word = False
        try:
            if word:
                return self.words.index(phrase)
            else:
                return self.text.index(phrase)

        except ValueError:
            return None

    def find_additional_costs(self):
        phrase = "additional cost to cast this spell"
        info = self.find(phrase)
        if info is None: return None
        index = info
        chunk = self.text[index+len(phrase)+len(","):self.text.index(".")]

        chunk = chunk.split(" ")

        method = chunk[0]
        num = 0
        if chunk[1] in constants.TO_NUM:
            num = constants.TO_NUM[chunk[1]]
        cost_types = chunk[1:len(chunk)]
        additional_cost = 0

        for permanent_type in constants.PERMANENT_TYPES:
            if permanent_type in cost_types:
                additional_cost = 1
                break
                if constants.PERMANENT_TYPES[permanent_type] > additional_cost:
                    additional_cost = constants.PERMANENT_TYPES[permanent_type]

        self.value -= (additional_cost * num)

    def cards_drawn(self):
        num_cards = None
        if not self.text: return None
        index = self.find("draw")
        if index is None:
            index = self.find("draws")
        if index is None: return None
        num_cards = self.words[index+1]
        self.value += constants.TO_NUM[num_cards]

    def removal(self):
        word = "target"
        index = self.find(word)

        #print(f"{self.name}: {self.words[index-1]} {self.words[index]} {self.words[index+1]}")

        removal_type = self.words[index-1].lower()

        self.value += constants.REMOVAL[removal_type]

        target_types = " ".join(self.words[index:])
        fullstop = target_types.index(".")
        target_types = target_types[:fullstop].split(" ")

        self.check_for_extras(target_types)

        for target in constants.PERMANENT_TYPES:
            if target in target_types:
                self.value += constants.PERMANENT_TYPES[target]

    def check_for_extras(self, chunk:list[str]):
        count = len(chunk)
        for item in chunk:
            if len(item) <= 2:
                count -= 1
            elif item in constants.PERMANENT_TYPES:
                count -= 1
            elif item == "nonland" or item == "target":
                count -= 1

        if count > 0:
            self.caveat = True

    def tokens_made(self):
        word = "create"
        index = self.find(word)
        if index is None: return None

        num_tokens = constants.TO_NUM[self.words[index+1]]
        if self.words[index+1] == "x":
            self.caveat = True

        self.value += num_tokens

    def __str__(self):
        return f"{self.raw_data['name']}: {self.score}"

    def pump(self):
        phrase = "equipped creature gets"
        index = self.find(phrase)
        if index is None: return None

        power = int(self.text[index+len(phrase)+2:self.text.index("/")])

        toughness = int(self.text[self.text.index("/")+2:self.text.index("/")+3])

        scale = 0.25
        for _ in range(power):
            print(scale)
            self.value += scale
            scale += power/1.5
        print("")
        #self.value += toughness / 2

def read_lookup(file_name:str) -> list[str]:
    with open(file_name+".txt") as file:
        content = file.read()
    return content.split("\n")[0:len(content.split("\n"))-1]

def run(filename:str, filter):
    if filter is None or filename is None: return None
    cards = read_lookup(filename)

    ret:dict[str, list[Card]] = {}
    for color in constants.COLORS:
        ret[constants.COLORS[color]] = []

    for name in cards:
        if name != "":
            name = name.lower()
            card = ORACLE[name]
            card.filter(filter)
            ret[card.color].append(card)


    for color in ret:
        if len(ret[color]) == 0:
            continue
        print(f"{color}\n")
        ret[color].sort(key=lambda x: x.score, reverse=True)
        for card in ret[color]:
            text = f"\t{card}\n"
            if card.caveat:
                text = f"\t*{card}\n"

            print(text)

types = {
    "removal": Card.removal,
    "card_draw":Card.cards_drawn,
    "boardwipe":None,
    "tokens":Card.tokens_made,
    "equipment":Card.pump,
}

if __name__ == "__main__":
    f = open('oracle.json')
    data = json.load(f)
    #add all cards to ORACLE
    ORACLE:dict[str, Card] = {}
    for i in data:
        card = Card(i["name"], i)
        ORACLE[card.name] = card
    for catagory in types:
        print("")
        print(catagory.upper())
        print("-"*30)
        run(catagory, types[catagory])
