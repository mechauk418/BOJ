
T = int(input())

for t in range(1,T+1):


    N = int(input())

    ans = 0

    for i in range(N):
        P,N = map(float,input().split())

        ans += P*N


    print(f'#{t} {ans}')

