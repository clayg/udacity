#!/usr/bin/env python
import os
import sys
import urllib
import urllib.request

DATA_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../data/'))


def main():
    if not os.path.isdir(DATA_ROOT):
        os.mkdir(DATA_ROOT)

    for filename in ('poi_names.txt',):
        data_file = os.path.join(DATA_ROOT, filename)
        if os.path.exists(data_file):
            continue
        url = 'https://github.com/udacity/ud120-projects/blob/master/' \
            'final_project/%s?raw=true' % filename
        urllib.request.urlretrieve(url, filename=data_file)
    print('Done!')


if __name__ == "__main__":
    sys.exit(main())
