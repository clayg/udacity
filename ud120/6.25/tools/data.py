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

import pickle
import os
import sys
from .__main__ import DATA_ROOT

data_file = os.path.join(DATA_ROOT, 'final_project_dataset.pkl')
try:
    with open(data_file, 'rb') as f:
        ENRON = pickle.load(f)
except FileNotFoundError:
    sys.exit('Unable to open dataset; try to initialize "python -m tools"')
