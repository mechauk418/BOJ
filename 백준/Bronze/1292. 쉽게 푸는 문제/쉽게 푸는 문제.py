A,B=map(int,input().split())

N_list = [  ]

for i in range(1,1001):
    for k in range(i):
        N_list.append(i)

print(sum(N_list[A-1:B]))