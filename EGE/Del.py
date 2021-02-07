def Del(x, D):
    return(x % D == 0)

def f(x):
    return (not(Del(x, A))) <= ((Del(x, 6)) <= (not(Del(x, 9)))) 

for A in range(1, 1000):
    if_del = True
    for x in range(1, 1000):
        if not f(x):
            if_del = False
            break
    if if_del:
        print(A)
