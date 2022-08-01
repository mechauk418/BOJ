import sys

N,M = map(int,sys.stdin.readline().split())

M_list = []
M_AE_list = []

for i in range(M):
    M1 = int(sys.stdin.readline())
    M_list.append(M1)
    M_AE = list(map(int,sys.stdin.readline().split()))
    M_AE_list.append(M_AE)

cnt = 0
for i in range(M):
    if M_AE_list[i] == sorted((M_AE_list[i]),reverse=True):
        cnt+=1

if cnt == len(M_AE_list):
    print('Yes')
else:
    print('No')