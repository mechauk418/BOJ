

N = int(input())
N_list = list(map(int,input().split()))

inc_list = [1]*N
dcre_list = [1]*N

for i in range(1,N):

    if N_list[i] <= N_list[i-1]:
        inc_list[i]=max(inc_list[i], inc_list[i-1]+1)
    if N_list[i] >= N_list[i-1]:
        dcre_list[i]=max(dcre_list[i], dcre_list[i-1]+1)

print(max(max(inc_list),max(dcre_list)))