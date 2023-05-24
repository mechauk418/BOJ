import sys
sys.setrecursionlimit(10**6)


input = sys.stdin.readline
N,R,Q = map(int,input().split())

graph = [[] for _ in range(N+1)]
dp = [ 0 for _ in range(N+1)]

for i in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(x):
    dp[x] = 1
    for n in graph[x]:
        if not dp[n]:
            dfs(n)
            dp[x] += dp[n]


dfs(R)


for i in range(Q):
    U = int(input())
    print(dp[U])
