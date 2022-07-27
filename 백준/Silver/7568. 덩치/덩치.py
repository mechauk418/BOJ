import sys

N=int(sys.stdin.readline())

H_list = []

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    H_list.append([x,y])

cnt_list=[]

for k in range(N):
    cnt = 1
    for i in range(N):

        if H_list[k][0] < H_list[i][0] and H_list[k][1] < H_list[i][1]:
            cnt+=1

    cnt_list.append(cnt)

print(' '.join(map(str,cnt_list)))