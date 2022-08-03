N = int(input())

S = [list(map(int,input().split())) for _ in range(N) ]

S_rev = [ [ 0 for i in range(N) ]  for _ in range(3)    ]

for i in range(3):
    for j in range(N):
        S_rev[i][j] = S[j][i]

ans_list = [0] * N

for i in range(N):
    sum = 0
    for j in range(3):
        if S_rev[j].count(S[i][j]) > 1:
            sum += 0
        else:
            sum += S[i][j]
    ans_list[i] = sum

for i in ans_list:
    print(i)


