import rater


def run(filename):
    decklist = rater.read_lookup(filename)

    ret = ""

    for card in decklist:
        start = card.index("(")
        end = card.index(")")
        code = card[start+1:end]
        if code == "PLST".lower():
            code = "LIST"
        code = f"[{code.upper()}]"

        final = card[0:start]
        final = final + code
        final = final + card[end+1:len(card)]

        ret = ret + final + "\n"

    f = open(f"new{filename}", "w")
    f.write(ret)

if __name__ == "__main__":
    run("decklist")