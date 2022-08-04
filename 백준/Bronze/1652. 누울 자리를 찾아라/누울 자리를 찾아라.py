import sys

N = int(sys.stdin.readline())

S = [ list(input()) for i in range(N)]
S_rev = [ [ '0' for i in range(N) ]  for _ in range(N)    ]

for i in range(N):
    for j in range(N):
        S_rev[i][j] = S[j][i]

ans_list = []
ans_rev_list = []

for i in range(N):

    ans = (''.join(S[i])).split('X')
    ans_list.append(ans)

for i in range(N):
    ans_rev = (''.join(S_rev[i])).split('X')
    ans_rev_list.append(ans_rev)

cnt = 0
cnt_rev = 0

for i in range(N):
    for j in range(len(ans_list[i])):
        if '..' in ans_list[i][j] :
            cnt+=1

for i in range(N):
    for j in range(len(ans_rev_list[i])):
        if '..' in ans_rev_list[i][j] :
            cnt_rev+=1

print(cnt, cnt_rev)