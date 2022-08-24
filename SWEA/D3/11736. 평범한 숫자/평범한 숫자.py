
T = int(input())

for t in range(1,T+1):

    N = int(input())

    N_list = list(map(int,input().split()))

    cnt = 0

    for i in range(1,N):
        if N_list[i] != max(N_list[i-1:i+2]) and N_list[i] != min(N_list[i-1:i+2]):
            cnt+=1

    print(f'#{t} {cnt}')