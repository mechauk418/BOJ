

for i in range(3):

    N = int(input())
    N_list = list(str(N))

    ans_list = []
    sum_list = []

    for i in N_list:
        if len(ans_list) == 0:
            ans_list.append(i)
        else:
            if i == ans_list[0]:
                ans_list.append(i)
                if i == N_list[-1]:
                    sum_list.append(len(ans_list))


            else:
                sum_list.append(len(ans_list))
                ans_list = []
                ans_list.append(i)
    if len(sum_list) == 0:
        print(8)
    else:
        print(max(sum_list))





