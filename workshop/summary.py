import sys
from collections import Counter
filename = sys.argv[1] # for number of file you give to the system to count 
with open(filename) as f:
    lines = f.readlines()
print("Total lines:",len(lines))
counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > 7:
        key = fields[7]
        counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)
