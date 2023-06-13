import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())

graph = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)
animal = [0] * (N+1)
mari = [0] * (N+1)
dp = [0] * (N+1)

for i in range(N-1):

    t,a,p = input().split()

    a = int(a)
    p = int(p)

    animal[i+2]= t
    mari[i+2] = a

    graph[i+2].append(p)
    graph[p].append(i+2)

def dfs(x):
    visited[x]=True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x]+=dp[i]

    if animal[x]=='W':
        dp[x] -= mari[x]
        if dp[x] < 0:
            dp[x]=0
    elif animal[x]=='S':
        dp[x] += mari[x]

    if len(graph[x])==1 and animal[x]=='S':
        dp[x]=mari[x]

dfs(1)
print(dp[1])
