#!/usr/bin/env python
import urllib.request
import tarfile
import os
import time

print()
print("checking for nltk")
try:
    import nltk  # noqa
except ImportError:
    print("you should install nltk before continuing")

print("checking for numpy")
try:
    import numpy  # noqa
except ImportError:
    print("you should install numpy before continuing")

print("checking for scipy")
try:
    import scipy  # noqa
except ImportError:
    print("you should install scipy before continuing")

print("checking for sklearn")
try:
    import sklearn  # noqa
except ImportError:
    print("you should install sklearn before continuing")


class ProgressBar():

    def __init__(self, wait=2):
        self.last_update = 0
        self.wait = wait

    def __call__(self, num_chunks, chunk_size, total_bytes):
        if time.time() < self.last_update + self.wait:
            return
        columns, _ = os.get_terminal_size(0)
        p = ((num_chunks * chunk_size) / total_bytes) * columns
        print(''.join('#' if p > i else '.' for i in range(columns)))
        self.last_update = time.time()


DATA_ROOT = os.path.join(os.path.dirname(__file__), '../data/')
if not os.path.isdir(DATA_ROOT):
    os.mkdir(DATA_ROOT)

FILENAME = "enron_mail_20150507.tar.gz"
if not os.path.exists(os.path.join(DATA_ROOT, FILENAME)):
    progress_bar = ProgressBar()
    print("Downloading the Enron dataset (this may take a while).")
    url = "https://www.cs.cmu.edu/~./enron/%s" % FILENAME
    urllib.request.urlretrieve(url, filename=os.path.join(DATA_ROOT, FILENAME),
                               reporthook=progress_bar)
    print()
    print("download complete!")


print
print("unzipping Enron dataset (this may take a while)")
os.chdir(DATA_ROOT)
tfile = tarfile.open(FILENAME, "r:gz")
tfile.extractall(".")

print("you're ready to go!")
