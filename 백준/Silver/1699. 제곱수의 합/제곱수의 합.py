

N = int(input())

DP = [i for i in range(N+1)]

for i in range(1,N+1):

    for j in range(1,i):

        if j*j > i:
            break
        if DP[i]>DP[i-j*j]+1:
            DP[i] = DP[i - j * j] + 1

print(DP[N])