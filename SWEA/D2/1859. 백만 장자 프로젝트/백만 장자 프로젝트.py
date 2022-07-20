
T=int(input())

for k in range(T):
    N=int(input())

    N_list=list(map(int,input().split()))

    N_list.reverse()


    A_list=[]
    ans = 0
    start=N_list[0]

    for i in range(1,len(N_list)):

        if start > N_list[i]:
            A_list.append(N_list[i])

        else:
            ans += start * len(A_list) - sum(A_list)
            start = N_list[i]
            A_list=[]

        if i == len(N_list) - 1:
            ans += start * len(A_list) - sum(A_list)
            start = N_list[i]
            A_list = []

    print( f'#{k+1} {ans}')