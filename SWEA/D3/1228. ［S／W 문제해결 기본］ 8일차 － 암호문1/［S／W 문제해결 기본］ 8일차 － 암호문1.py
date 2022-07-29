
for k in range(1,11):

    N_len = int(input())

    S_list = list(map(str,input().split()))


    N_com = int(input())

    S_com = list(map(str,input().split()))

    for i in range(len(S_com)):
        if S_com[i] == 'I':
            for j in range(int(S_com[i+2])):
                S_list.insert(int(S_com[i+1])+j,S_com[i+3+j])

    print(f'#{k} {" ".join(S_list[0:10])}')