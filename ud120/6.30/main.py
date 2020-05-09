#!/usr/bin/env python

from argparse import ArgumentParser
import sys

from tools.data import POI_DATA

parser = ArgumentParser()
parser.add_argument('--feature', required=True,
                    help='feature to display')


class UnknownFilterError(Exception):
    pass


def main():
    args = parser.parse_args()
    for name, features in POI_DATA.items():
        if args.feature not in features:
            msg = 'Unable to find feature %r' % args.feature
            alternatives = {f for f in features
                            if args.feature.lower() in f.lower()}
            if alternatives:
                msg += ', did you mean %r' % sorted(alternatives)
            raise UnknownFilterError(msg)
        print(f"{name}: {features[args.feature]}")


if __name__ == "__main__":
    sys.exit(main())
