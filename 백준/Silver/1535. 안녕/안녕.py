
N = int(input())
loss = list(map(int,input().split()))
gain = list(map(int,input().split()))
loss, gain = [0] + loss, [0] + gain
dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if loss[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + gain[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])
