import hashlib
key = 'iwrupvqb'
n = 0
while True:
    s = key + str(n)
    h = hashlib.md5(s.encode('utf-8')).hexdigest()
    if h[:6] == '000000':
        break
    n += 1
print(n)
