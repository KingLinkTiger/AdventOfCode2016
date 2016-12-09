
input_file = "Part1.txt"
f = open(input_file, 'r')
data = f.read()


def decom_len(str):
    result = 0
    i = 0
    while i < len(str):
        chr = str[i]
        if chr == '(':
            close = str.index(")", i)
            split = str.index("x", i, close)
            length = int(str[i+1:split])
            count = int(str[split + 1:close])
            addit = decom_len(str[close+1:close+length+1])
            result += addit * count
            i = close+length
        else:
            result += 1
        i += 1
    return result

print decom_len(data)