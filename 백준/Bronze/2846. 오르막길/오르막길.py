import sys

N = int(sys.stdin.readline())

N_list = list(map(int,sys.stdin.readline().split()))

N_list.reverse()

ans = 0
ans_list=[]
for i in range(len(N_list)-1):
    if N_list[i] - N_list[i+1]>0:
        ans+= (N_list[i] - N_list[i+1])
        if i+1==len(N_list)-1:
            ans_list.append(ans)

    else:
        ans_list.append(ans)
        ans=0

print(max(ans_list))

