import os
import re
import sys

from .__main__ import DATA_ROOT

PATTERN = re.compile(r'\((?P<email>[y,n])\) (?P<name>.*)')

data_file = os.path.join(DATA_ROOT, 'poi_names.txt')


def is_yes(char):
    return char.lower() == 'y'


def process_lines(f):
    emails = {}
    for line in f:
        match = PATTERN.match(line)
        if not match:
            continue
        emails[match.group('name')] = is_yes(match.group('email'))
    return emails


try:
    with open(data_file, 'r') as f:
        EMAILS = process_lines(f)
except FileNotFoundError:
    sys.exit('Unable to open dataset; try to initialize "python -m tools"')
