N,M = map(int,input().split())


def axis(x):
    if x % 4 !=0:
        row = (x //4)+1
        col = (x % 4)
    else:
        row = (x//4)
        col = 4

    return row, col

ans = abs(axis(N)[0] - axis(M)[0]) + abs(axis(N)[1] - axis(M)[1])

print(ans)