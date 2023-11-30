
n = int(input())

lines=[]
dp=[1 for _ in range(n)]
for i in range(n):
    f,b = map(int,input().split())
    lines.append([f,b])

lines.sort()

for i in range(1,n):
    for j in range(i):
        if lines[j][1]<lines[i][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))