A,B=map(int,input().split())

N_list = [  ]

for i in range(1,B+1):
    for k in range(i):
        N_list.append(i)

print(sum(N_list[A-1:B]))