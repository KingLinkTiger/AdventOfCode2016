import hashlib

m = hashlib.md5()

passcode = {}
index = 0
base = "uqwqemis"

while len(passcode) < 8:
    key = base + `index`
    m = hashlib.md5()
    m.update(key)
    hash = m.hexdigest()
    
    if hash[:5] == "00000":
        if (ord(hash[5]) >= ord('1') and ord(hash[5]) <= ord('7')) or ord(hash[5]) <= ord('0'):
            ind = int(hash[5])
            if not ind in passcode.keys():
                passcode[ind] = hash[6]
                print ind
                print hash
                print key
    index += 1
passcode_final = ""
for i in range(8):
    passcode_final += passcode[i]
print passcode_final