# Guess 1599 = Too High


import re
from itertools import izip_longest


lines = [line.rstrip('\n') for line in open('input.txt')]


def check_valid_triangle(sides):
    for side in sides:
        other_sides = (sum(sides)-side)
        if side > other_sides:
            return 'No'
        elif side == other_sides:
            return 'Degenerated'
    else:
        return 'Yes'







numPossible = 0
numImpossible = 0

for line in lines:
    line = re.sub(' +',' ',line)
    sides = [int(x.strip()) for x in line.strip().split(' ')]
    if check_valid_triangle(sides) == "Yes":
        numPossible += 1
    #print sides
    
    

print "Part 1: " + str(numPossible)



# Part 2

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

sides = []


Column1 = []
Column2 = []
Column3 = []

Column = []
CurrentColumnNum = 1

numPossible2 = 0
numImpossible2 = 0
    
for line in lines:
    line = re.sub(' +',' ',line)
    sides = [x.strip() for x in line.strip().split(' ')]

    
    Column1.append(sides[0])
    Column2.append(sides[1])
    Column3.append(sides[2])

Column += (Column1)
Column += (Column2)
Column += (Column3)

groups = grouper(3,Column)


for group in groups:
    #print group
    
    curSides = []
    
    for side in group:
        curSides.append(int(side))
    
    if check_valid_triangle(curSides) == "Yes":
        numPossible2 += 1




#print sides[0::3]
#print sides[1::3]
#print sides[2::3]


print "Part 2: " + str(numPossible2)

