# сама программа
def d(n, b):
    d.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = ''
    while n:
        n, y = divmod(n, b)
        r = d.t[y] + r
    return r


# ввод данных
n = int(input())
b = int(input())

print(d(n, b))
