import re

with open("Part1.txt") as f:
    rules = f.readlines()

count = 0

for line in rules:
    sides = [int(x.replace(" ", "")) for x in re.sub(' +',' ',line).strip().split(' ')]
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]:
        count += 1

print count
print len(rules)