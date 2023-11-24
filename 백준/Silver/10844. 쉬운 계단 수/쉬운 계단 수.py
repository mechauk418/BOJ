
N = int(input())

DP = [[0]*10 for _ in range(N+1)]

for i in range(1,10):
    DP[1][i]=1

for i in range(2,N+1):

    for j in range(10):
        if j==0:
            DP[i][j]=DP[i-1][1]
        elif j==9:
            DP[i][j] = DP[i - 1][8]
        else:
            DP[i][j] = DP[i - 1][j-1] + DP[i-1][j+1]

print(sum(DP[N])%1000000000)