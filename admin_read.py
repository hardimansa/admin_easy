### Populate "keyword.txt with information used in manual STIG

z="Audit Keyword Matched"

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
           print(f' \n \v \t "{z}" "{line.rstrip()}" ')




