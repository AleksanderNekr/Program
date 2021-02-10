a = int(23)
b = int(43)
x = int(input())

print('Результат:', a + b)

print('a', 'b', 'c', sep=':')

print('a', 'b', 'c', sep='\n')
print('a', 'b', 'c', sep='\\')

print('a', 'b', 'c', sep='\\', end=' Done! \n')

print(-17 // 3, 17 // 3, 17 % 3, -17 % 3, sep='\n')

if x >= 0:
    print(x)
else:
    x = -x
    print(x)
