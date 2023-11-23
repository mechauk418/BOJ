n = int(input())

P = []



for i in range(n):
    P.append(int(input()))

DP = [0 for _ in range(n)]
DP[0]=P[0]

for i in range(1,n):
    if i==1:
        DP[i]=P[0]+P[1]
    elif i==2:
        DP[i] = max( P[2]+P[1],P[2]+P[0],DP[1] )
    else:
        DP[i]= max(DP[i-1], DP[i-3]+P[i-1]+P[i], DP[i-2]+P[i])

print(max(DP))