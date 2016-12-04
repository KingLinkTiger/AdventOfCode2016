
import re
from collections import Counter
import string

lines = [line.rstrip('\n') for line in open('input.txt')]


def calculateChecksum(EncryptedName):
    x = Counter(EncryptedName)

    checksum = ""
    
    topFive = x.most_common(6)
    topFive = dict(topFive)


    uniqueChars = []
    notUniqueChars = []
    
    
    
    rev_multidict = {}
    for key, value in topFive.items():
        rev_multidict.setdefault(value, set()).add(key)
            

    
    
    
    
    i = 0
    for group in sorted(rev_multidict, reverse=True):
        #For each group of characters

            for character in sorted(rev_multidict.get(group)):
                if i <= 4:
                    checksum += character
                    i += 1

    return checksum    
    
    
    
    
    
    
'''    
    for character, value in topFive.iteritems():
        
        changeableTopFive = topFive.copy()
        del changeableTopFive[character]
        
        if value in changeableTopFive.values():
            #There is another value that is the same and we need to add them in alphabetical order
            notUniqueChars.append(character)
        else: 
            uniqueChars.append(character)
            checksum += character

    print notUniqueChars

    for character in sorted(notUniqueChars):
        checksum += character
'''



countGood = 0
sumSectorIDs = 0

for line in lines:
    sectorHash = re.search("([0-9]+)\[([a-z]+)\]", line)
    SectorID = re.search("([0-9]+)", sectorHash.group(0)).group(0)
    ProvidedChecksum = re.search("([a-z]+)", sectorHash.group(0)).group()
       


    
    EncryptedName = re.search("^(.*?)([0-9]+)\[([a-z]+)\]", line)
    EncryptedName = re.sub('-', '', EncryptedName.group(1))
    CalculatedChecksum = calculateChecksum(EncryptedName)

    
    
    
    
    
    
    if CalculatedChecksum == ProvidedChecksum:
        countGood += 1
        sumSectorIDs += int(SectorID)


print "Part 1: " + str(sumSectorIDs)







#Part 2
'''
    Guesses:
        487 - LOW
'''

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def caeser_shift(s, rotation):
    return ''.join(chr(((ord(c) - ord('a') + rotation) % 26) + ord('a')) for c in s)




lines = [line.rstrip('\n') for line in open('input.txt')]
for line in lines:
    sectorHash = re.search("([0-9]+)\[([a-z]+)\]", line)
    SectorID = re.search("([0-9]+)", sectorHash.group(0)).group(0)
    ProvidedChecksum = re.search("([a-z]+)", sectorHash.group(0)).group()
    EncryptedName = re.search("^(.*?)([0-9]+)\[([a-z]+)\]", line)
    if EncryptedName != None:
        #print EncryptedName.group(1)
        
        for grouping in EncryptedName.group(1).split("-"):
            for y in range(1,26):
                #print caesar(grouping, y)
                if caesar(grouping, y) == "northpole":
                    print "Part 2: " + SectorID
                    exit()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





