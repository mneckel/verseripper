#!/usr/bin/env python3

'''
VERSE RIPPER  1.7
---------------------------
This will extract all the verses from a txt document into a nice list.
Verse formatting is assumed to be from BSF study questions.  
ref:  https://www.bsfinternational.org/

1. Copy-paste the study questions into a text file.
2. Execute at command line against the file like this:  "verserip questions.txt"
3. Copy-paste the list of verses into your verse retrieval application. 
You can then use this list for retrieval from your favorite application.
Like this one:  https://www.blueletterbible.org/search.cfm#srchMulti

'''

import argparse
import re

print('running')
parser = argparse.ArgumentParser(description='Process a file.')
parser.add_argument('filename', type=str, help='The name of the file to process')
args = parser.parse_args()
with open(args.filename, 'r') as f:
    # Process the file here
    orgtxt = f.read()
# a list of tuples is returned       
wholeverse = r"((\d*)\s+([A-Z]\w*\b)\s+(\d+[:]\d+[-–—]?\d?\d?\d?([:]\d+)?))|((?:((\d*)\s+)?(?:[A-Z]\w*\b)\s+)?(\d+[:]\d+[-–—]?\d?\d?\d?))"
matches = re.findall(wholeverse, orgtxt)
# print(matches)
print("--------------------------------------------------")

# Account for subsequent verses in the same book
for book in matches:
    if book[2] != '':     # Yes book is specified
        prebook = book[1]+" "+book[2]   # Book number(opt) + Book name
        lookup = (book[1]+" "+book[2]+" "+book[3]) # number, book, verse number
    if book[2] == '':     # assume use of the same book specified previously
        lookup = (prebook+" "+book[5])  # number, book, standalone verse number
    print(lookup.lstrip())
