N = int(input())

row = [0]*N
ans = 0

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False

    return True


def n_queens(x):
    global ans

    if x==N:
        ans+=1

    else:
        for i in range(N):
            row[x]=i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
