#!/usr/bin/env python

import argparse
import re
import sys
import time

parser = argparse.ArgumentParser(description="Get a time.")
parser.add_argument('interval', metavar='interval', nargs='?', default='5m', help='Interval at which to beep')
parser.add_argument('-n', '--num-beeps', dest='limit', default=None, type=int, help='Maximum number of beeps to emit')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', default=False, help='Write a message with every beep')
args = parser.parse_args()

match = re.match("([0-9]+)(.?)", args.interval)
if match is not None and match.group(2) in ['h', 'm', 's', '']:
    multipliers = {'h' : 3600, 'm' : 60, 's' : 1, '' : 1}
    interval = int(match.group(1))
    interval *= multipliers[match.group(2)]
    count = 1
    while True:
        sys.stdout.write(chr(7))
        sys.stdout.flush()
        if args.verbose:
            sys.stdout.write(time.strftime("%a, %d %b %Y %H:%M:%S +0000") + ": Beep!\n")
            sys.stdout.flush()
        if args.limit is None or count < args.limit:
            time.sleep(interval)
            count += 1
        else:
            break
else:
    sys.stderr.write("Usage: beepevery.py NN[hms]\n")
    sys.exit(1)
