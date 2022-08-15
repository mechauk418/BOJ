
T = int(input())


for t in range(T):

    N,M = map(int,input().split())

    S_list = [   list(input()) for _ in range(N)    ]

    S_odd_list = S_list[::2]
    S_even_list = S_list[1::2]
    if len(S_even_list) == 0:
        one_line_check = [True,True]
        for i in S_odd_list:
            if '.' in i[::2] or '#' in i[1::2]:
                one_line_check[0] = False
        for i in S_odd_list:
            if '#' in i[::2] or '.' in i[1::2]:
                one_line_check[1] = False

        if one_line_check[0] or one_line_check[1]:
            print(f'#{t + 1} possible')
        else:
            print(f'#{t + 1} impossible')


        continue


    check_list = [True, True]

    # 1/3/5행에 시작이 .
    for i in S_odd_list:
        if '.' in i[::2] or '#' in i[1::2]:
            check_list[0] = False

    for i in S_even_list:
        if '#' in i[::2] or '.' in i[1::2]:
            check_list[0] = False


    for i in S_odd_list:
        if '#' in i[::2] or '.' in i[1::2]:
            check_list[1] = False

    for i in S_even_list:
        if '.' in i[::2] or '#' in i[1::2]:
            check_list[1] = False



    if check_list[0] or check_list[1]:
        print(f'#{t+1} possible')
    else:
        print(f'#{t+1} impossible')