import re
from audioop import reverse

def matcher(str):
    for i in range(len(str) - 3):
        if str[i:i+4] == ''.join(reversed(str[i:i+4])) and str[i] != str[i+1]:
            return True
    return False

with open("Part1.txt") as f:
    addrs = f.readlines()

count = 0

for addr in addrs:
    parts = re.split(r'\[([^\]]+)\]', addr)
    matches = []
    for i in range(len(parts)):
        if matcher(parts[i]):
            matches.append(i)
    even = odd = False
    for match in matches:
        if match % 2 == 0:
            even = True
        else:
            odd = True
    if even and not odd:
        count += 1
print count