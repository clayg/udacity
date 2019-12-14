#!/usr/bin/env python

from argparse import ArgumentParser
from bisect import insort
import sys

from tools.data import ENRON

parser = ArgumentParser()
parser.add_argument('--feature', required=True, help='feature to rank')


class UnknownFilterError(Exception):
    pass


def rank(args, orig_data):
    data = []
    for name, features in orig_data.items():
        if args.feature:
            if args.feature not in features:
                msg = 'Unable to find feature %r' % args.feature
                alternatives = {f for f in features
                                if args.feature.lower() in f.lower()}
                if alternatives:
                    msg += ', did you mean %r' % sorted(alternatives)
                raise UnknownFilterError(msg)
        item = (features[args.feature], name)
        if item[0] == 'NaN':
            continue
        insort(data, item)
    return data


def main():
    args = parser.parse_args()
    try:
        data = rank(args, ENRON)
    except UnknownFilterError as e:
        return 'ERROR: %s' % e
    for feature, name in data:
        print(feature, name)


if __name__ == "__main__":
    sys.exit(main())
