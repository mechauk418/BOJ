import sys

N = int(sys.stdin.readline())

S_list = []
S_set = set()
cnt = 0

for i in range(N):
    S = sys.stdin.readline().rstrip()
    S_list.append(S)

for i in range(len(S_list)):
    if S_list[i] == 'ENTER':
        cnt += len(S_set)
        S_set = set()
    else:
        S_set.add(S_list[i])
        if i == len(S_list)-1:
            cnt += len(S_set)

print(cnt)



