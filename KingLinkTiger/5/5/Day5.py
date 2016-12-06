import hashlib

input = "reyedfim"

outputPassword = ""
index = 0

fiveZero = 0

#while fiveZero < 8:
while len(outputPassword) < 8:
    m = hashlib.md5()
    m.update(input+str(index))
    
    hash = m.hexdigest()
    if hash[:5] == "00000":
        fiveZero += 1
        #print hash
        outputPassword += hash[5]

    index += 1


print "Part 1: " + outputPassword



#Part 2

outputPassword2 = ""
passwordDict = {}
index2 = 0
fiveZero2 = 0

while len(passwordDict) < 8:
    m = hashlib.md5()
    m.update(input+str(index2))
    
    hash = m.hexdigest()
    if hash[:5] == "00000":
        
        
        if hash[5].isdigit():
            if int(hash[5]) in range(0,8):
                if not int(hash[5]) in passwordDict:
                    passwordDict[int(hash[5])] = hash[6]
                    #print hash
                    #print len(passwordDict)

    
    index2 += 1


for key, value in passwordDict.iteritems():
    outputPassword2 += value

print "Part 2: " + outputPassword2
