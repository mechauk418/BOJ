
N = int(input()) # 사자 최대 N마리

DP = [1] * (N+1)

if N==1:
    print(3)
else:
    DP[1],DP[2]=3,7
    for i in range(3,N+1):
        DP[i]=(2*DP[i-1]+DP[i-2]) % 9901
    print(DP[N])