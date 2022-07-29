T = int(input())

for k in range(1,T+1):
    N_list = list(map(int,input().split()))
    ans = 0

    for i in range(3):
        if N_list.count(N_list[i]) == 1 or N_list.count(N_list[i]) == 3:
            ans = N_list[i]

    print(f'#{k} {ans}')