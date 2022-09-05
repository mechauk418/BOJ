T = int(input())

for t in range(1,T+1):


    N = int(input())

    N_list=[0] * 5000
    C_list = []

    for i in range(N):
        A,B = map(int,input().split())
        for j in range(A-1,B):
            N_list[j]+=1


    P = int(input())

    for i in range(P):
        C = int(input())
        C_list.append(C)

    print(f'#{t}',end=' ')
    for c in C_list:
        print(f'{ N_list[c-1]}',end=' ')
        
    print()

