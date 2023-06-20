import os

directory = 'configs'
output_file = 'combined.txt'

with open(output_file, "a") as outfile:
   for filename in os.listdir(directory):
      filepath = os.path.join(directory, filename)
      if os.path.isfile(filepath):
         with open(filepath, 'r') as infile:
            contents = infile.read()
            outfile.write(contents + '\n')

### Populate "keyword.txt with information used in manual STIG

z="Audit Keyword Matched"

#configs = [" 192.168.56.10", " 192.168.56.11", " 192.168.56.12", " 192.168.56.13", " 192.168.56.14"]
configs = ["combined.txt"]

 # STIG reference checklist (keyword)
with open('keyword.txt', 'r') as f:
    keyword = f.read().splitlines()

# configuration files to be audited
for v in configs:
    print(f'Reading {v}') 
    with open(v, 'r') as f: 
#with open('1.ios', 'r') as f:
     lines = f.readlines()
     

# Search for each keyword in the file
for keyword in keyword:
    for line in lines:
        if keyword in line:
           print(f' \n \v \t "{z}" "{line.rstrip()}" ')



