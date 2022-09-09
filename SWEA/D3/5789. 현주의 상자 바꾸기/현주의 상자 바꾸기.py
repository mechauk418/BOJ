
T = int(input())

for t in range(1,T+1):


    N,Q = map(int,input().split())

    N_list = [0] * N

    for i in range(Q):
        L,R = map(int,input().split())

        for j in range(L,R+1):

            N_list[j-1] = i+1


    ans = ' '.join( map(str,N_list)    )

    print(f'#{t} {ans}')