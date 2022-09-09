
T = int(input())

for t in range(1,T+1):


    S = input()

    S_list = list(S)

    H = int(input())

    H_list = list(map(int,input().split()))
    H_list.sort(reverse=True)

    for i in range(len(H_list)):

        S_list.insert(H_list[i],'-')


    print(f'#{t} {"".join(S_list)}'   )

