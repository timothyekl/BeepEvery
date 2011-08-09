#!/usr/bin/env python

import argparse
import re
import sys
import time

parser = argparse.ArgumentParser(description="Get a time.")
parser.add_argument('interval', metavar='interval', nargs='?', default='5m', help='Interval at which to beep')
args = parser.parse_args()

match = re.match("([0-9]+)(.?)", args.interval)
if match is not None and match.group(2) in ['h', 'm', 's', '']:
    multipliers = {'h' : 3600, 'm' : 60, 's' : 1, '' : 1}
    interval = int(match.group(1))
    interval *= multipliers[match.group(2)]
    while True:
        sys.stdout.write(chr(7))
        sys.stdout.flush()
        time.sleep(interval)
else:
    sys.stderr.write("Usage: beepevery.py NN[hms]\n")
    sys.exit(1)
