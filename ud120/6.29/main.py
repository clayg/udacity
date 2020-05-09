#!/usr/bin/env python

from argparse import ArgumentParser
import sys

from tools.data import ENRON

parser = ArgumentParser()
parser.add_argument('--feature', required=True,
                    help='missing feature to count')


class UnknownFilterError(Exception):
    pass


def count_missing(args):
    missing = 0.0
    for name, features in ENRON.items():
        if args.feature not in features:
            msg = 'Unable to find feature %r' % args.feature
            alternatives = {f for f in features
                            if args.feature.lower() in f.lower()}
            if alternatives:
                msg += ', did you mean %r' % sorted(alternatives)
            raise UnknownFilterError(msg)
        if features[args.feature] == 'NaN':
            missing += 1
    return missing


def main():
    args = parser.parse_args()
    try:
        count = count_missing(args)
    except UnknownFilterError as e:
        return 'ERROR: %s' % e
    percent = 100.0 * count / len(ENRON)
    print(f"{args.feature}: {percent:.1f} %")


if __name__ == "__main__":
    sys.exit(main())
