
N = int(input())

dp = [ 0 for _ in range(N+1)]

dp[0]=1
dp[1]=1

for i in range(2,N+1):

    dp[i]=(dp[i-2]+dp[i-1])%15746

print(dp[N])