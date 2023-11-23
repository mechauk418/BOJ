
N = int(input())

A_list = list(map(int,input().split()))

dp = [ 1 for _ in range(N)]
dp[0]=A_list[0]


for i in range(1,N):

    for j in range(i):

        if A_list[i] > A_list[j]:

            dp[i]=max(dp[i],dp[j]+A_list[i])
        else:
            dp[i] = max(dp[i], A_list[i])

print(max(dp))