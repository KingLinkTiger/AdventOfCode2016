import hashlib

m = hashlib.md5()

passcode = ""
index = 0
base = "uqwqemis"

while len(passcode) < 8:
    key = base + `index`
    m = hashlib.md5()
    m.update(key)
    hash = m.hexdigest()
    
    if hash[:5] == "00000":
        print hash
        print key
        passcode += hash[5]
    index += 1
print passcode