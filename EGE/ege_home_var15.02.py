from itertools import product
print('x', 'y', 'z', 'w')
for x, y, z, w in product(range(2), range(2), range(2), range(2)):
    if (not(x == (not y)) or (y and (not z))) or (z and (not w)) is False:
        print(x, y, z, w)
