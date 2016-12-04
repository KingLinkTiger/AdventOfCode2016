
keypad = [['1', '2', '3'],['4', '5', '6'], ['7', '8', '9']]
x = y = 1

with open("Part1.txt") as f:
    rules = f.readlines()

buttons = []

for line in rules:
    for move in line:
        if move == 'U':
            if y > 0:
                y -= 1
        if move == 'D':
            if y < 2:
                y += 1
        if move == 'L':
            if x > 0:
                x -= 1
        if move == 'R':
            if x < 2:
                x += 1
    buttons.append(keypad[y][x])
print ''.join(buttons)