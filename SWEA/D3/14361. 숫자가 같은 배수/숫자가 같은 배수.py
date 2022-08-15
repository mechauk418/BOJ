
T = int(input())

for t in range(T):


    N = int(input())

    N_list = list(str(N))
    N_list.sort()
    N_x_list = [ i * N for i in range(1,10) if len(str(i*N)) == len(str(N)) ]

    cnt = 0

    for i in N_x_list:
        check_list = list(str(i))
        check_list.sort()

        if N_list == check_list:
            cnt += 1


    if cnt > 1:
        print(f'#{t+1} possible')
    else:
        print(f'#{t + 1} impossible')
