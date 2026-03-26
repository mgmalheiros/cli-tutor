#!/usr/bin/env python
import argparse
import sys

parser = argparse.ArgumentParser(description='Changes character case')
parser.add_argument('-u', '--upper', help='makes upper case', action='store_true')
parser.add_argument('-f', '--file', help='reads from the given file name')
args = parser.parse_args()

#print(args)''

if args.file:
    file = open(args.file, 'r')
else:
    file = sys.stdin

for line in file:
    if args.upper:
        print(line.upper(), end='')
    else:
        print(line.lower(), end='')

if args.file:
    file.close()
