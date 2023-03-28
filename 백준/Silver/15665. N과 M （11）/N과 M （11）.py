
N,M = map(int,input().split())

S = list(map(int,input().split()))

S.sort()

array = []

check = []

def solve(depth,M):

    if depth == M:
        print(' '.join(map(str,array)))
        return
    temt = 0
    for i in range(N):
        if temt != S[i]:
            array.append(S[i])
            temt = S[i]
            solve(depth+1,M)
            array.pop()

solve(0,M)