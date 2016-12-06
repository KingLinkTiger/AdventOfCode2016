import collections

lines = [line.rstrip('\n') for line in open('input.txt')]

outputCode = ""
outputCode_Part2 = ""

testdata_columns = zip(*lines)

for line in testdata_columns:
    outputCode += collections.Counter(line).most_common()[0][0]
    least_common = collections.Counter(line).most_common()[-1]
    outputCode_Part2 += least_common[0]
    
print "Part 1: " + outputCode
print "Part 2: " + outputCode_Part2