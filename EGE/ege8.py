from itertools import product
counter = 0
for a, b, c in product('ШКОЛА', 'ШКОЛА', 'ШКОЛА'):
    if (a + b + c).count('К') == 1:
        counter += 1
print(counter)
print('aaa')
