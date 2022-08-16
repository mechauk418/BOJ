
T = int(input())

for t in range(1,T+1):

    N = int(input())

    N_list = [ list(input()) for _ in range(N)     ]

    index_list = []

    for i in range(N):
        for j in range(N):
            if N_list[i][j] == '#':
                index_list.append((i,j))

    check_list = []

    for i in range(index_list[0][0],index_list[-1][0]+1):
        for j in range(index_list[0][1],index_list[-1][1]+1):
            check_list.append((i,j))

    if index_list == check_list and len(index_list) == len(check_list) and (index_list[-1][0]+1 - index_list[0][0]) == (index_list[-1][1]+1 - index_list[0][1])      :
        print(f'#{t} yes' )
    else:
        print(f'#{t} no')