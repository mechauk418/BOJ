import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

dp = [ [0,0] for _ in range(N+1) ]

def dfs(x):
    visited[x] = True
    dp[x][0]=0
    dp[x][1]=1

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += dp[i][1]
            dp[x][1] += min(dp[i][0],dp[i][1])

dfs(1)
print(min(dp[1][0],dp[1][1]))