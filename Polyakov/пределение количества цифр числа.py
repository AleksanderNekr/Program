# 1 способ
n = int(input())
length = 0
while n != 0:
    n //= 10
    length += 1
print(length)

# 2 способ
i = int(input())
length = len(str(i))
print(length)
print('End of the program')

# 3 способ
word = int(input())
count = 0
for i in str(word):
    count += 1
print(count)
