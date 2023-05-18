from collections import defaultdict

N,K = map(int,input().split())

A = list(map(int,input().split()))

DP = [A[0]]*N

history = defaultdict(int)

history[A[0]]=1

ans = 0

for i in range(1,N):

    DP[i]=DP[i-1]+A[i]

    if (DP[i]-K) in history:

        ans+= history[DP[i]-K]

    history[ DP[i] ] +=1

for i in DP:
    if i==K:
        ans+=1

print(ans)
