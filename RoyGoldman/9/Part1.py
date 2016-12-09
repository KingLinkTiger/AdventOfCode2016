
input_file = "Part1.txt"
f = open(input_file, 'r')
data = f.read()

result = ""

i = 0
while i < len(data):
    chr = data[i]
    if chr == '(':
        close = data.index(")", i)
        split = data.index("x", i, close)
        length = int(data[i+1:split])
        count = int(data[split + 1:close])
        for c in range(count):
            result += data[close+1:close+length+1]
        i = close+length
    else:
        result += chr
    i += 1

print len(result)