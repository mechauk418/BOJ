import sys
sys.setrecursionlimit(10**9)

def solution(n, lighthouse):
    answer = 0
    visited = [False] * (n+1)
    dp = [ [0,0] for _ in range(n+1) ]
    
    graph = [[] for _ in range(n+1)]
    for i in lighthouse:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    def dfs(x):
        visited[x]=True
        dp[x][0]=0
        dp[x][1]=1

        for i in graph[x]:
            if not visited[i]:
                dfs(i)
                dp[x][0] += dp[i][1]
                dp[x][1] += min(dp[i][0],dp[i][1])
    
    dfs(1)
    answer = min(dp[1][0],dp[1][1])
    
    return answer

