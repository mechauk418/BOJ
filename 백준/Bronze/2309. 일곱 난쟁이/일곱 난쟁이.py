N_list = []

for i in range(9):
    N = int(input())
    N_list.append(N)


allsum = sum(N_list)
sum2_list = []

for i in range(9):
    for j in range(i+1,9):
        sum2 = N_list[i] + N_list[j]
        sum2_list.append([sum2, N_list[i] , N_list[j]      ])

for i in range( len(sum2_list) ):
    if allsum - sum2_list[i][0] == 100:
        two = [sum2_list[i][1], sum2_list[i][2]]

ans_list = [ i for i in N_list if not i in two   ]

ans_list.sort()

for i in range(7):
    print(ans_list[i])