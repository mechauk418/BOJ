from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

parent = list(map(int,input().split()))

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(1,n):
    graph[i+1].append(parent[i])
    graph[parent[i]].append(i+1)



ans_list = [ 0 for _ in range(n)]

def dfs(x,depth):
    visited[x]=True
    ans_list[x-1] = depth
    for i in graph[x]:
        if not visited[i]:
            if i in par:
                dfs(i,depth+par[i])
            else:
                dfs(i,depth)

par = defaultdict(int)

for _ in range(m):
    i,w = map(int,input().split())
    par[i]+=w

dfs(1,0)
print(*ans_list)