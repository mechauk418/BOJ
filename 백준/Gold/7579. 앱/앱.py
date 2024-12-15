import sys

N, M = map(int, sys.stdin.readline().split())
memories = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))

dp = [ [0] * (sum(cost) + 1) for _ in range(N + 1) ]

answer = sum(cost)

for i in range(1, N + 1):
    for j in range(sum(cost) + 1):
        dp[i][j] = dp[i - 1][j]

    for j in range(cost[i], sum(cost) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memories[i])
        if (dp[i][j] >= M):
            answer = min(answer, j)

print(answer)