from collections import deque

N,M,V = map(int,input().split())

graph = [ [] for _ in range(N+1) ]

for i in range(M):
    A,B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)


for i in graph:
    i.sort()

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

root_dfs = []
root_bfs = []

def dfs(x):
    visited_dfs[x] = True

    root_dfs.append(x)

    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)

dfs(V)

print(*root_dfs)


def bfs(x):

    queue = deque([x])

    visited_bfs[x] = True

    while queue:

        t = queue.popleft() # 1
        root_bfs.append(t)

        for i in graph[t]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


bfs(V)
print(*root_bfs)