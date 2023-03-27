
N,M = map(int,input().split())

S = list(map(int,input().split()))

S = list(set(S))


S.sort()


array = []


def solve(depth,N):

    if depth == M:
        print(' '.join(map(str,array)))

        return

    for i in range(len(S)):
        if depth == 0 or array[-1] <= S[i]:
            array.append(S[i])
            solve(depth+1,N)
            array.pop()


solve(0,N)

