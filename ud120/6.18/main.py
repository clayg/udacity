#!/usr/bin/env python

from argparse import ArgumentParser
import json
import sys

from tools.data import ENRON

parser = ArgumentParser()
parser.add_argument('--json', action='store_true',
                    help='just dump raw data for use with jq')
parser.add_argument('--name', help='filter just one name')
parser.add_argument('--feature', help='filter just one filter')


class UnknownFilterError(Exception):
    pass


def apply_filters(args, orig_data):
    data = {}
    for name, features in orig_data.items():
        if args.feature:
            if args.feature not in features:
                msg = 'Unable to find feature %r' % args.feature
                alternatives = {f for f in features
                                if args.feature.lower() in f.lower()}
                if alternatives:
                    msg += ', did you mean %r' % sorted(alternatives)
                raise UnknownFilterError(msg)
            value = {args.feature: features[args.feature]}
        else:
            value = features
        if args.name and name != args.name:
            continue
        data[name] = value
    if args.name and not data:
        msg = 'Unable to find name %r' % args.name
        alternatives = {name for name in orig_data
                        if args.name.lower() in name.lower()}
        if alternatives:
            msg += ', did you mean %r' % sorted(alternatives)
        raise UnknownFilterError(msg)
    return data


def main():
    args = parser.parse_args()
    try:
        data = apply_filters(args, ENRON)
    except UnknownFilterError as e:
        return 'ERROR: %s' % e
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    sys.exit(main())
