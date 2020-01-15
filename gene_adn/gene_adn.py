import re

s = 'ACTCGTTTCGT' 
g = 'CGT'

indexes = []
n = 0

for match in re.finditer(g, s):
    n += 1
    indexes.append(match.start())

print(n)
print(' '.join(str(x) for x in indexes))