from itertools import product
for x, y, z, w in product(range(2), range(2), range(2), range(2)):
    if (not x != y) or (y and (not z)) or (z and (not w)) is False:
        print(w, z, y, x)

# for s1 in range(10, 100):
#     s = s1
#     s = (s+1) // 7
#     n = 36
#     while s < 2050:
#         s = s * 2
#         n = n + 3
#     if n == 60:
#         print(s1, '!OOOO!')
name = 'ТИМОФЕЙ'
counter = 0
for a, b, c, d, e in product(name, name, name, name, name):
    wor = a + b + c + d + e
    if wor.count('Т') >= 1 and wor.count('Й') <= 1:
        counter += 1
        # print(wor)
print(counter)
