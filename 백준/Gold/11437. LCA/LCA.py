import sys
sys.setrecursionlimit(10**5)

N = int(input())

graph = [ [] for _ in range(N+1) ]

for i in range(N-1):
    A,B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)


parent = [ i for i in range(N+1)]

visited = [False] * (N+1)

d = [0]*(N+1)

def dfs(x,depth):
    visited[x]=True
    d[x]=depth

    for i in graph[x]:
        if visited[i]:
            continue
        parent[i]=x
        dfs(i,depth+1)

dfs(1,0)

def lca(a,b):

    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b= parent[b]

    while a!=b:
        a = parent[a]
        b = parent[b]

    return a

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))