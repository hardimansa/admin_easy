from dis import findlinestarts
from gettext import find

z="Audit Keyword Matched"
y="not matched"

 # STIG reference checklist (keyword)
with open('keyword.txt', 'r') as f:
    keyword = f.read().splitlines()

# configuration files to be audited
with open('1.ios', 'r') as f:
    lines = f.readlines()

# Search for each keyword in the file
for keyword in keyword:
    for line in lines:
        if keyword in line:
           # print(f'"{keyword}" found in "{line.strip()}"')
            print(f' \n \v \t \t \t \t \t \t "{z}" "{line.rstrip()}" ')
         





