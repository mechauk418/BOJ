
N,M = map(int,input().split())

S = list(map(int,input().split()))

S.sort()

out = []

def back(depth,idx,N,M):

    if depth == M:
        print(' '.join(map(str,out)))

        return

    for i in range(N):

        out.append(S[i])
        back(depth+1,S[i],N,M)
        out.pop()


back(0,0,N,M)


