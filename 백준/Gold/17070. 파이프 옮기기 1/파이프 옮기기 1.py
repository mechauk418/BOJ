import sys

input = sys.stdin.readline

N = int(input())

arr = [[0 for _ in range(N)]]
for _ in range(N):
    arr.append([*map(int, input().split())])

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N + 1)]
dp[1][1] = [1, 0, 0]

for i in range(1, N + 1):
    for j in range(1, N):
        if i == j == 1:
            continue
        if arr[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if arr[i - 1][j] == arr[i][j - 1] == 0:
                dp[i][j][2] = sum(dp[i - 1][j - 1])
print(sum(dp[N][N - 1]))