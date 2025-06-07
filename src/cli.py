import argparse
import sys

from cardparser import Card

MASTER_LIST = []
card_objects: list[Card] = []

allowed_parameters = ["pow2cmc", "tou2cmc", "draw2cmc", "tokens2cmc"]

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)

parser.add_argument("-i", "--input", help="file path to input")

parser.add_argument(
    "-m",
    "--mode",
    help="""analysis mode, either 'm'/'math' for a purely mathematical analysis,
                    or 's'/'score' for a subjective analysis""",
)

parser.add_argument(
    "-p",
    "--parameter",
    help="""parameter for analysis. for a detailed list
                    of accepted parameters, please see documentation""",
)
args = parser.parse_args()

print()

if args.verbose:
    print("verbosity turned on")

if args.mode == "math" or args.mode == "m":
    # print("doing math stuff")
    pass

if args.mode == "score" or args.mode == "s":
    # print("doing score stuff")
    pass

if not args.mode:
    args.mode = ""

if args.input:
    # print(f"reading file {args.input}")
    from cardfetcher import fetch
    from readfile import read

    MASTER_LIST = read(args.input)
    card_objects = fetch(MASTER_LIST, args.mode)

if args.parameter:
    if args.parameter in allowed_parameters:
        print(
            f"analyzing with parameter '{args.parameter}' in {args.mode} mode (higher numbers are better)"
        )
        skipped = 0
        final: list[Card] = []
        for card in card_objects:
            analyze = getattr(card.report, args.parameter)
            analyze()
            if card.report.score is None:
                skipped += 1
            else:
                final.append(card)
        if skipped > 0:
            print(
                f"""some cards were unable to be analyzed with the parameter '{args.parameter}'.
                    {skipped} card(s) skipped.\n"""
            )
        final.sort(key=lambda x: x.report.score, reverse=True)
        for card in final:
            print(card.report)
    else:
        print(f"Invalid parameter '{args.parameter}'. Please try again.")
        sys.exit(1)

print()
