import re
import operator
from collections import defaultdict

with open("Part1.txt") as f:
    rooms = f.readlines()

sum_ids = 0

for room in rooms:
    name = re.search(r'^((((\w+)-)+))+', room).group()[:-1]
    sector = int(re.search(r'(\d+)', room).group())
    check = re.search(r'\[([^\]]+)\]', room).group()
    check = re.search(r'\w+', check).group()
    
    chars = {}
    
    for l in name:
        if l == "-":
            continue
        if not l in chars.keys():
            chars[l] = 1
        else:
            chars[l] += 1
            
    order = {}

    for key, value in sorted(chars.items()):
        if not value in order.keys():
            order[value] = []
        order[value].append(key)
        
    order = sorted(order.items(), reverse = True)
    
    check_c = ""
    
    for k, list in order:
        for i in list:
            check_c += i
            if len(check_c) == 5:
                break
        if len(check_c) == 5:
            break
    
    if check == check_c:
        sum_ids += sector

print sum_ids