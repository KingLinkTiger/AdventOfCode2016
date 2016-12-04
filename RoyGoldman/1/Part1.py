

input_file = "part1.txt"
f = open(input_file, 'r')
data = f.read()

directions = [x.strip() for x in data.split(',')]

x = 0
y = 0
dir = 0

for d in directions:
    turn = d[0]
    count = int(d[1:])
    print dir
    print count
    if turn == "R":
        dir += 1
    else:
        dir -= 1
    dir = dir % 4
    if (dir % 2) == 0:
        if dir > 1:
            y -= count
        else:
            y += count
        print "y:"
        print y
    else:
        if dir > 1:
            x -= count
        else:
            x += count
        print "x:"
        print x

print x
print y

print abs(x) + abs(y)