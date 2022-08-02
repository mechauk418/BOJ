
T = int(input())

for k in range(1,T+1):

    N,M = map(int,input().split()) # 3 5
    N_list = list(map(int, input().split())) # 1 5 3
    M_list = list(map(int, input().split())) # 3 6 -7 5 4

    if len(M_list) > len(N_list):
        big_list = M_list
    else:
        big_list = N_list

    mul = 0
    mul_list = []


    for i in range(max(N,M) - min(M,N)+1):
        for j in range(min(N,M)):
            mul += N_list[j]*M_list[j]
        mul_list.append(mul)
        mul=0
        big_list.reverse()
        big_list.pop()
        big_list.reverse()

    print(f'#{k} {max(mul_list)}')