#!/usr/bin/env python3
import urllib.parse
import sys

if len(sys.argv) != 2:
    exit(1)
elif len(sys.argv[1]) > 9999:    
    exit(1)
elif len(sys.argv[1]) == 0:
    exit(1)
else:
    # handle spaces in names
    decoded_string = urllib.parse.unquote_plus(sys.argv[1])
    print(f"<div>Voter name {decoded_string} registered.</div>")