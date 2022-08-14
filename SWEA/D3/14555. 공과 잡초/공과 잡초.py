

T = int(input())

for t in range(1,T+1):


    S = input()

    S_list = list(S)

    cnt = 0

    cnt += S_list.count('(') + S_list.count(')')


    cnt -= S.count('()')

    print(f'#{t} {cnt}')

