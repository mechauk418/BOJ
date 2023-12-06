import sys
input = sys.stdin.readline

dp = [1,2,4,7]
l = 4
for i in range(int(input())):
    n = int(input())
    while(n > l):
        dp.append((dp[l-3]+dp[l-2]+dp[l-1])%1000000009)
        l+=1
    print(dp[n-1])