
T = int(input())

for t in range(1,T+1):


    N,A,B = map(int,input().split())

    max_gu = min(A,B)
    min_gu = A+B - N

    if min_gu < 0:
        min_gu = 0


    print(f'#{t} {max_gu} {min_gu}')