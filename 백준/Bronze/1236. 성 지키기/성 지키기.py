N,M=map(int,input().split())

s = [list(input()) for _ in range(N)    ]
s_rev = [ [ 0 for i in range(N) ]  for _ in range(M)    ]


ans_h = 0
ans_v = 0

for i in range(N):
    if 'X' not in s[i]:
        ans_h +=1

for i in range(M):
    for j in range(N):
        s_rev[i][j] = s[j][i]

for i in range(M):
    if 'X' not in s_rev[i]:
        ans_v +=1

print(max(ans_v,ans_h))