from itertools import product
for x, y, z, w in product(range(2), range(2), range(2), range(2)):
    if (not x != y) or (y and (not z)) or (z and (not w)) is False:
        print(w, z, y, x)
