
T = int(input())

for k in range(1,T+1):

    N_list=[]
    check_list = [1,2,3,4,5,6,7,8,9]
    for _ in range(9):
        N_line = list(map(int,input().split()))
        N_list.append(N_line)

    horizn = 0
    vert = 0
    sum_block = 0

    for i in range(9):
        ver_list = []
        for j in range(9):
            N_list_sort = sorted(N_list[i])
            if N_list_sort == check_list:
                horizn += 1

            if i in [0,3,6] and j in [0,3,6]:
                check_block_list = []
                for a in range(3):
                    for b in range(3):
                        check_block_list.append(N_list[i+a][j+b])
                check_block_list.sort()
                if check_block_list == check_list:
                    sum_block += 1




            ver_list.append(N_list[j][i])
        ver_list_sort = sorted(ver_list)
        if ver_list_sort == check_list:
            vert += 1



    if horizn == 81 and vert == 9 and sum_block == 9:
        print(f'#{k} {1}')
    else:
        print(f'#{k} {0}')
