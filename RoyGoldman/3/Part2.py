import re

with open("Part1.txt") as f:
    rules = f.readlines()

count = 0
i = 0
data = []

for line in rules:
    sides = [int(x.replace(" ", "")) for x in re.sub(' +',' ',line).strip().split(' ')]
    data.append(sides)
while i < len(data):
    for n in range(3):
        if data[i][n] + data[i + 1][n] > data[i + 2][n] and  data[i][n] + data[i + 2][n] > data[i + 1][n] and data[i + 2][n] + data[i + 1][n] > data[i][n]:
                    count += 1
    i += 3
print count
print len(rules)