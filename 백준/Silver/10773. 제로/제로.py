K=int(input())
N_list = []
for _ in range(K):

    N=int(input())
    if N!=0:
        N_list.append(N)
    else:
        N_list.pop()

print(sum(N_list))
