T=int(input())

for i in range(T):
    N,S=map(str,input().split())
    N=int(N)
    S=list(S)
    del S[N-1]
    print(''.join(S))

