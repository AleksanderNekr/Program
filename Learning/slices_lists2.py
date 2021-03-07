print('Введите целочисленный список через пробел:', end=' ')

try:
    A = list(map(int, input().split()))
except ValueError:
    print('\n===============!СПИСОК ДОЛЖЕН БЫТЬ ЦЕЛОЧИСЛЕННЫМ!=============')
    exit(0)

print('Введите i:', end=' ')
i = int(input())
print('Введите j:', end=' ')
j = int(input())

print(A[i:j:-1])
