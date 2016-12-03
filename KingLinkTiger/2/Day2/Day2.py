lines = [line.rstrip('\n') for line in open('input.txt')]



CurrentPosition = (1,1)


Values = {}
Values[7] = (0,0)
Values[4] = (0,1)
Values[1] = (0,2)
Values[8] = (1,0)
Values[5] = (1,1)
Values[2] = (1,2)
Values[9] = (2,0)
Values[6] = (2,1)
Values[3] = (2,2)

Answer1 = ""

for line in lines:
    for direction in line:
        X = CurrentPosition[0]
        Y = CurrentPosition[1]

        
        if direction == "U":
            if Y != 2:
                Y += 1
            
        if direction == "D":           
            if Y != 0:
                Y -= 1

        if direction == "L":
            if X != 0:
                X -= 1

        if direction == "R":
            if X != 2:
                X += 1
            
        CurrentPosition = (X, Y)
        
    #print "Current Position: " + str(CurrentPosition[0])  + "," + str(CurrentPosition[1])
    temp = dict((v,k) for k, v in Values.iteritems())
    OutputKey = temp[CurrentPosition]
    Answer1 += str(OutputKey)
    
print "Part 1: " + Answer1

Values2 = {}
Values2[1] = (3,5)
Values2[2] = (2,4)
Values2[3] = (3,4)
Values2[4] = (4,4)
Values2[5] = (1,3)
Values2[6] = (2,3)
Values2[7] = (3,3)
Values2[8] = (4,3)
Values2[9] = (5,3)
Values2["A"] = (2,2)
Values2["B"] = (3,2)
Values2["C"] = (4,2)
Values2["D"] = (3,1)

Values2_Rev = dict((v,k) for k, v in Values2.iteritems())
CurrentPosition2 = (0,3)

Answer2 = ""
for line in lines:
    for direction in line:
        X = CurrentPosition2[0]
        Y = CurrentPosition2[1]

        
        if direction == "U":
            if (X, Y+1) in Values2_Rev:
                Y += 1
            
        if direction == "D":           
            if (X, Y-1) in Values2_Rev:
                Y -= 1

        if direction == "L":
            if (X-1, Y) in Values2_Rev:
                X -= 1

        if direction == "R":
            if (X+1, Y) in Values2_Rev:
                X += 1
            
        CurrentPosition2 = (X, Y)
        
        #print "Current Position: " + str(CurrentPosition2[0])  + "," + str(CurrentPosition2[1])
    OutputKey = Values2_Rev[CurrentPosition2]
    Answer2 += str(OutputKey)
    
print "Part 2: " + Answer2