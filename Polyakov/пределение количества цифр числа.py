# 1 способ
n = int(input())
length = 0
while n > 0:
    n //= 10
    length += 1
print(length)

# 2 способ
i = input()
length = len(str(i))
print(length)
print('End of the program')

# 3 способ
word = str(input())
count = 0
for i in word:
    count += 1
print(count)
