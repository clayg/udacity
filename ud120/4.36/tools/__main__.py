#!/usr/bin/env python
import os
import urllib.request

DATA_ROOT = os.path.join(os.path.dirname(__file__), '../data/')

if not os.path.isdir(DATA_ROOT):
    os.mkdir(DATA_ROOT)

for filename in ('word_data.pkl', 'email_authors.pkl'):
    url = 'https://github.com/udacity/ud120-projects/blob/master/' \
        'tools/%s?raw=true' % filename
    urllib.request.urlretrieve(url, filename=os.path.join(DATA_ROOT, filename))
print('Done!')
