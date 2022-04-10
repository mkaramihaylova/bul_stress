#!/usr/bin/env python3

""" Deletes entire row if second column contains '/en.wiktionary.org.' """

import argparse
import csv


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as file:
        with open(args.output, "w") as sink:
            source = csv.reader(file, delimiter="\t")
            for line in source:
                if "/en.wiktionary.org" not in line:
                    print("\t".join(line), file=sink)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="no space file path")
    main(parser.parse_args())
