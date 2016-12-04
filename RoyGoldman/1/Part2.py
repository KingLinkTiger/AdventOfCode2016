

input_file = "part1.txt"
f = open(input_file, 'r')
data = f.read()

directions = [x.strip() for x in data.split(',')]

locations = {}

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
        
    while count > 0:
        if (dir % 2) == 0:
            if dir > 1:
                y -= 1
            else:
                y += 1
        else:
            if dir > 1:
                x -= 1
            else:
                x += 1
        if not x in locations:
            locations[x] = {}
        if y in locations[x] and locations[x][y] == 1:
            print x
            print y
            
            print abs(x) + abs(y)
            exit()
        locations[x][y] = 1
        count -= 1