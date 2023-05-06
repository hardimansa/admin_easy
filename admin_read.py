
z="matched"
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
            print(f' "{z}" "{line.strip()}" ')
         
    else:
        if keyword not in line:
           print(f' "{keyword}" !__! "{y}" BRO')
