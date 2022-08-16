
T = int(input())

for t in range(T):

    N,D = map(int,input().split())

    one_block = 2*D+1

    if (N%one_block) !=0:

        ans = (N//one_block) +1
    else:
        ans = N//one_block

    print(f'#{t+1} {ans}')

