
T = int(input())

for k in range(1,T+1):

    N = int(input())
    S_list = []
    v0 = 0
    for i in range(N):
        com_ace_list = list(map(int,input().split()))
        if len(com_ace_list)==2:
            com = com_ace_list[0]
            ace = com_ace_list[1]
        else:
            com = 0
            ace = 0

        if com == 2:
            com = -1

        v = v0+ace*com
        if v<0:
            v=0
        S_list.append(v)
        v0 = v
    print(f'#{k} {sum(S_list)}')

