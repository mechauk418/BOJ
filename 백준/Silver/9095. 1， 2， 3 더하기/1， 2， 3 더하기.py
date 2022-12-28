def plus(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4

    return plus(x - 1) + plus(x - 2) + plus(x - 3)


T = int(input())

for i in range(T):

    N = int(input())

    print(plus(N))

