N = int(input())

S = list(map(int, input().split()))

DP = [1 for _ in range(N)]
DP[0]=1

DP2 = [1 for _ in range(N)]
DP2[0]=1

for j in range(1,N):
    for k in range(j):
        if S[j] > S[k]:
            DP[j]=max(DP[j],DP[k]+1)

S_reverse = S[::-1]

for j in range(1,N):
    for k in range(j):
        if S_reverse[j] > S_reverse[k]:
            DP2[j]=max(DP2[j],DP2[k]+1)

DP2=DP2[::-1]

ans_list = [  (DP[i]+DP2[i]-1) for i in range(N)     ]

print(max(ans_list))