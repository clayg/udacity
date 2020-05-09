"""
Starter code for exploring the Enron dataset (emails + finances);
loads up the dataset (pickled dict of dicts).

The dataset has the form:
ENRON["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

{features_dict} is a dictionary of features associated with that person.
You should explore features_dict as part of the mini-project,
but here's an example to get you started:

ENRON["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import os
import re
import sys
import pickle
from .__main__ import DATA_ROOT

PATTERN = re.compile(r'\((?P<email>[y,n])\) (?P<name>.*)')

_DATA_FILE = os.path.join(DATA_ROOT, 'poi_names.txt')


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


# EMAILS keys are "Last, First"
try:
    with open(_DATA_FILE, 'r') as f:
        EMAILS = process_lines(f)
except FileNotFoundError:
    sys.exit('Unable to open dataset; try to initialize "python -m tools"')


# ENRON keys are "LAST FIRST M"
_DATA_FILE = os.path.join(DATA_ROOT, 'final_project_dataset.pkl')
try:
    with open(_DATA_FILE, 'rb') as f:
        ENRON = pickle.load(f)
except FileNotFoundError:
    sys.exit('Unable to open dataset; try to initialize "python -m tools"')


POI_DATA = {}
for key, data in ENRON.items():
    if key == 'TOTAL':
        continue
    last, first = key.split()[:2]
    email_k = '%s, %s' % (last.title(), first.title())
    if email_k in EMAILS:
        POI_DATA[key] = data
