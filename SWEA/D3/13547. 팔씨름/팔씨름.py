import collections

T = int(input())

for t in range(1,T+1):


    S = input()

    S_list = list(S)

    S_dict = collections.Counter(S_list)

    check = len(S_list) - S_dict['o']

    if check > 7:
        print(f'#{t} NO')
    else:
        print(f'#{t} YES')