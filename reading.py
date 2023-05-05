import re
import json

with open('BOC-A12.ios') as f:
    for line in f:
        print(line.strip())





STIG = open('xios')
for line in STIG:
    line = line.rstrip()
    if re.search('secret', line):
        print(line)
        print(f'STIG-1 found')

STIG = open('x2.ios')
for line in STIG:
    line = line.rstrip()
    if re.search('username', line):
        print(line.split())

STIG = open('x.ios')
for line in STIG:
    line = line.rstrip()
    if re.search('access-list', line):
        print(line.split())




