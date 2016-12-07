import re
from audioop import reverse

def matcher_aba(str):
    matches = []
    for i in range(len(str) - 2):
        if str[i:i+3] == ''.join(reversed(str[i:i+3])) and str[i] != str[i+1]:
            matches.append(str[i:i+3])
    return matches

def aba_bab(abas, babs):
    for a in abas:
        for b in babs:
            if a[0] == b[1] and b[0] == a[1]:
                print a + " " + b
                return True
    return False

with open("Part1.txt") as f:
    addrs = f.readlines()

count = 0

for addr in addrs:
    parts = re.split(r'\[([^\]]+)\]', addr)
    odd = parts[::2]
    even = parts[1::2]
    for s in odd:
        for s2 in even:
            if aba_bab(matcher_aba(s), matcher_aba(s2)):
                count += 1
print count