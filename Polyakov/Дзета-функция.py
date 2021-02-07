from math import sqrt
result = 0
for i in range(1, 11):
    result = result + 1 / (i ** 2)
result = sqrt(6 * result)
print(result)
