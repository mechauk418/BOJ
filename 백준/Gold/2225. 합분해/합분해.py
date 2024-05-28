
N,K = map(int,input().split())

ans = 0

DP = [ [0] * (K+1) for _ in range(N+1) ]

DP[0][0]=1

for i in range(0,N+1):
    for j in range(1,K+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

print(DP[N][K]%1000000000)