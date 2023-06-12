import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

N = int(input())

S = list(map(int,input().split()))

S = [0] + S

graph = defaultdict(list)
visited =  [ 0 for _ in range(N+1)]

dp = [[0,S[i]] for i in range(N+1)]


for i in range(N-1):
    A,B =map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)

def dfs(x):
    visited[x]=True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][1] += dp[i][0]
            dp[x][0] += max( dp[i][0], dp[i][1] )

dfs(1)
print(max(dp[1][0], dp[1][1]))