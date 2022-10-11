from itertools import product

N,K = map(int,input().split())

K_list = list(map(int,input().split()))

AE_NUM = len(str(N))

Num_list = []
ans_list = []

for i in product(K_list,repeat = AE_NUM):
    if int(''.join(map(str,i)))<=N:

        Num_list.append(int(''.join(map(str,i))))


if Num_list:
    ans_list.append(max(Num_list))

Num_list=[]

for i in product(K_list,repeat = AE_NUM-1):
    Num_list.append(int(''.join(map(str,i))))

ans_list.append(max(Num_list))

print(max(ans_list))