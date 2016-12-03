f = open('input', 'r')

input = f.read()

directions = [x.strip() for x in input.split(',')]


x = 0
y = 0

facing = 1

for direction in directions:
    
    if direction[:1]=="L":
        facing -= 1
    
    if direction[:1]=="R":
        facing += 1
    
    if facing > 4:
        facing = 1
    
    if facing < 1:
        facing = 4
    
    #turn right adds 1
    #turn left subtracts 1
    #loop if > 4 or < 1
    
    #If even change X value


    if facing == 2:
        x += int(direction[1:])
    
    if facing == 4:
        x -= int(direction[1:])

    if facing == 1:
        y += int(direction[1:])
    
    if facing == 3:
        y -= int(direction[1:])
        

    print "Facing: " + str(facing)
    print "X: " + str(x) + " Y: " + str(y)

print x+y