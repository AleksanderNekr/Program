from math import floor
n = int(input())
k = int(input())

fl = int(floor(k / n))

print(k - (n * fl))
