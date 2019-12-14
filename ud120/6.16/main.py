#!/usr/bin/env python
from argparse import ArgumentParser
import json
import sys

from tools import data

parser = ArgumentParser()
parser.add_argument('--json', action='store_true',
                    help='just dump raw data for use with jq')


def display_summary(data):
    print("Total Entries: %s" % len(data))
    print("Have email: %s" % sum(data.values()))


def main():
    args = parser.parse_args()
    if args.json:
        print(json.dumps(data.EMAILS, indent=2))
    else:
        display_summary(data.EMAILS)


if __name__ == "__main__":
    sys.exit(main())
