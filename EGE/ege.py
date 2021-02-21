import string


# сама программа
def d(n, b):
    d.t = string.digits + string.ascii_uppercase
    r = ''
    while n:
        n, y = divmod(n, b)
        r = d.t[y] + r
    return r


def replacer(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '3', 1)
        s = s.replace('333', '1', 1)
    print(s, end='\n')


s = '1' * 1300
replacer(s)

a = (7 * (2 ** 3000)) + (8 ** 500) - (4 ** 200) - (7 * (4 ** 100)) + 35
aS = d(a, 4)


countZ = 0
countO = 0
countT = 0
countTh = 0

for i in range(len(aS)):
    if aS[i] == '0':
        countZ += 1
    elif aS[i] == '1':
        countO += 1
    elif aS[i] == '2':
        countT += 1
    elif aS[i] == '3':
        countTh += 1
print(countZ, countO, countT, countTh)
