
T=int(input())

for a in range(T):

    N,K=map(int,input().split())
    N_list = []
    for i in range(N):
        N_line= list(map(int,input().split()))
        N_list.append(N_line)


    cnt_row = 0
    for i in range(N):
        for j in range(1,N-K):
            if sum(N_list[i][j:K+j]) == K and N_list[i][K+j] == 0 and N_list[i][j-1] == 0:
                cnt_row += 1

    for i in range(N):
        if sum(N_list[i][0:K]) == K and N_list[i][3] == 0:
            cnt_row += 1
        if sum(N_list[i][-1:-1-K:-1]) == K and N_list[i][-1-K] ==0:
            cnt_row += 1


    K_list = [[ 0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            K_list[i][j] = N_list[j][i]


    cnt_col = 0
    for i in range(N):
        for j in range(1,N-K):
            if sum(K_list[i][j:K+j]) == K and K_list[i][K+j] == 0 and K_list[i][j-1] == 0:
                cnt_col += 1

    for i in range(N):
        if sum(K_list[i][0:K]) == K and K_list[i][3] == 0:
            cnt_col += 1
        if sum(K_list[i][-1:-1-K:-1]) == K and K_list[i][-1-K] ==0:
            cnt_col += 1


    print(f'#{a+1} {cnt_row+cnt_col}' )