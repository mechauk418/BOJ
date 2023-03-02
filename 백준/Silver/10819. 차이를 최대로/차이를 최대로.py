import sys

def dfs(depth):
    if depth == N:
        result.append(sum(abs(explore[i] - explore[i + 1]) for i in range(N - 1)))
        return
    for i in range(N):
        if visited[i]:
            continue
        explore.append(A[i])
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0
        explore.pop()

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

visited = [0] * N
result, explore = [], []
dfs(0)
print(max(result))