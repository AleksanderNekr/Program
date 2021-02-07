def Del():
    for A in range(1, 1001):
        count = 0
        for x in range(1, 1001):
            if (x % A == 0) or not(x % 6 == 0) or not(x % 9 == 0):
                count += 1
        if count == 1000:
            print(A)


Del()

# list()
