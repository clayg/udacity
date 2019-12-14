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
    num_features = set()
    poi_count = 0
    for name, featrues in data.items():
        num_features.add(len(featrues))
        if featrues.get('poi', False):
            poi_count += 1
    print("Total Featres: %r" % sorted(num_features))
    print("Total POI: %d" % poi_count)


def main():
    args = parser.parse_args()
    if args.json:
        print(json.dumps(data.ENRON, indent=2))
    else:
        display_summary(data.ENRON)


if __name__ == "__main__":
    sys.exit(main())
