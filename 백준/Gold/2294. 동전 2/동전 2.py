
n,k = map(int,input().split())

coin = []

for i in range(n):
    coin.append(int(input()))

coin = list(set(coin))

coin.sort()

dp = [ 10000000 for _ in range(k+1)]
dp[0]=0
for i in coin:
    for j in range(i,k+1):

        dp[j]=min(dp[j],dp[j-i]+1)

if dp[k]==10000000:
    print(-1)
else:
    print(dp[k])