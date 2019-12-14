#!/bin/bash
set -xe
./main.py  --feature total_payments | tail -n 10
./main.py  --feature salary | wc -l
./main.py  --feature email_address | wc -l
