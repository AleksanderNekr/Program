from itertools import product
for x, y, z, w in product(range(2), range(2), range(2), range(2)):
    if (not x != y) or (y and (not z)) or (z and (not w)) is False:
        print(w, z, y, x)

s = int(input())
s = (s+1) // 7
n = 36
while s < 2050:
    s = s * 2
    n = n + 3
print(n)
