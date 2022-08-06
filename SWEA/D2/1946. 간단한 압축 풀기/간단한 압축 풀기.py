
T = int(input())

for t in range(T):

    N = int(input())
    C_list = []
    K_list = []
    for i in range(N):
        C,K = input().split()
        K = int(K)
        C_list.append(C)
        K_list.append(K)

    ans_s = ''

    for i in range(N):
        ans_s += C_list[i] * K_list[i]

    print(f'#{t+1}')

    for i in range(len(ans_s)):
        print(ans_s[i],end='')
        if i%10==9:
            print()
    print()




