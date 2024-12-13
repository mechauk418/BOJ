import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):

    K = int(input())

    C = [0]+list(map(int,input().split()))

    Sum = [0] * (K+1)

    for i in range(1,K+1):
        Sum[i]=Sum[i-1]+C[i]

    dp = [ [0] * (K+1) for _ in range(K+1) ]

    for cnt in range(1, K):
        for start in range(1, K - cnt + 1):
            end = start + cnt

            MIN = sys.maxsize
            for mid in range(start, end):
                MIN = min(MIN, dp[start][mid] + dp[mid + 1][end])

            dp[start][end] = MIN + Sum[end] - Sum[start - 1]

    print(dp[1][K])

