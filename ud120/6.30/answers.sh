#!/bin/bash
set -xe
./main.py --feature total_payments | grep NaN | wc -l
