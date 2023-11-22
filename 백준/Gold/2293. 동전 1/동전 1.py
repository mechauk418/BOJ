n,k = map(int,input().split())

coin_list = []

for i in range(n):
    v = int(input())
    coin_list.append(v)

dp=[ 0 for _ in range(k+1)]
dp[0]=1
for i in coin_list:

    for j in range(i,k+1):
        if j-i >=0:
            dp[j]+=dp[j-i]
        else:
            print(i,j)


print(dp[k])