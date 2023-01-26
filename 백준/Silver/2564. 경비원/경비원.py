

M,N = map(int,input().split())

S = int(input())

S_list = []

for i in range(S):

    P,A = map(int,input().split())
    S_list.append((P,A))

Dong_P,Dong_A = map(int,input().split())

ans = 0

for i in S_list:

    if Dong_P == 1:
        dis = N+N+M+(M-Dong_A)
    elif Dong_P == 2:
        dis = N+Dong_A
    elif Dong_P == 3:
        dis = Dong_A
    else:
        dis = N+M+(N-Dong_A)

    if i[0] == 1:
        dis_i = N+N+M+(M-i[1])
    elif i[0] == 2:
        dis_i = N+i[1]
    elif i[0] == 3:
        dis_i = i[1]
    else:
        dis_i = N+M+(N-i[1])

    len_T = 2*(N+M)

    real_dis = abs(dis-dis_i)

    if real_dis>=(N+M):
        real_dis = len_T - real_dis


    ans+=real_dis

print(ans)
