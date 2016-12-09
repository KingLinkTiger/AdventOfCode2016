from test.warning_tests import outer

def print_display(disp):
    for row in disp:
        out = ""
        for c in row:
            out += c
        print out

def count_display(disp):
    count = 0
    for row in disp:
        for c in row:
            if c == '#':
                count += 1
    return count

display = []

for i in range(6):
    row = []
    for j in range(50):
        row.append('_')
    display.append(row)


with open("Part1.txt") as f:
    ops = f.readlines()

for op in ops:
    parts = op.split()
    if parts[0] == "rect":
        a = int(parts[1][:parts[1].index('x')])
        b = int(parts[1][parts[1].index('x') + 1:])
        for y in range(b):
            for x in range(a):
                display[y][x] = "#"
    elif parts[0] == "rotate":
        if parts[1] == "row":
            y = int(parts[2][parts[2].index('=') + 1:])
            count = int(parts[4])
            for c in range(count):
                tmp = display[y][-1]
                del display[y][-1]
                display[y] = [tmp] + display[y]
        else:
            x = int(parts[2][parts[2].index('=') + 1:])
            count = int(parts[4])
            last = ' '
            tmp = ""
            for c in range(count):
                for r in display:
                    tmp = r[x]
                    r[x] = last
                    last = tmp
                display[0][x] = last
    else:
        print "ERROR"
        exit()

print_display(display)
print count_display(display)