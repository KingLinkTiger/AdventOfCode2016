with open("Part1.txt") as f:
    lines = f.readlines()

counts = {}

for line in lines:
    for i in range(len(line)):
        if not i in counts.keys():
            counts[i] = {}
        c = line[i]
        if not c in counts[i].keys():
            counts[i][c] = 0
        counts[i][c] += 1
final = ""

for key, chars in counts.items():
    for char, count in sorted(chars.items(), key=lambda (k, v): chars[k], reverse = True):
        final += char
        break
    
print final