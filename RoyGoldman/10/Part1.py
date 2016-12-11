
with open("Part1.txt") as f:
    ops = f.readlines()

bots = {}
outputs = {}
    
def process(bot):
    if len(bot["values"]) >= 2:
        a = bot["values"].pop()
        b = bot["values"].pop()
        low = min(a, b)
        high = max(a, b)
        if low == 17 and high == 61:
            print "TARGET: " + str(bot["id"])
        if bot["low"]["type"] == "output":
            outputs[bot["low"]["id"]].append(low)
        else:
            bots[bot["low"]["id"]]["values"].append(low)
            process(bots[bot["low"]["id"]])
        if bot["high"]["type"] == "output":
            outputs[bot["high"]["id"]].append(high)
        else:
            bots[bot["high"]["id"]]["values"].append(high)
            process(bots[bot["high"]["id"]])

for line in ops:
    parts = line.split()
    if parts[0] == "bot":
        id = int(parts[1])
        dest_low_type = parts[5]
        dest_low_id = int(parts[6])
        dest_high_type = parts[10]
        dest_high_id = int(parts[11])
        if dest_low_type == "output" and dest_low_id not in outputs.keys():
            outputs[dest_low_id] = []
        if dest_high_type == "output" and dest_high_id not in outputs.keys():
            outputs[dest_high_id] = []
        if id not in bots.keys():
            bots[id] = {"id": id, "values": []}
        bots[id]["low"] = {"type": dest_low_type, "id": dest_low_id}
        bots[id]["high"] = {"type": dest_high_type, "id": dest_high_id}
    else:
        value = int(parts[1])
        id = int(parts[5])
        if id not in bots.keys():
            bots[id] = {"id": id, "values": []}
        bots[id]["values"].append(value)

running = True
for id in bots:
    process(bots[id])