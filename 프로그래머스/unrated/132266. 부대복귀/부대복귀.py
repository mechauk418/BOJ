from collections import deque

def bfs(start,graph,visited):
    q = deque([[start,0]])
    visited[start] = 0
    while q:

        now,cnt = q.popleft()

        for i in graph[now]:
            if visited[i] == -1:
                visited[i]= visited[now]+1
                q.append([i,cnt+1])



def solution(n, roads, sources, destination):
    answer = []

    graph = [ [] for _ in range(n+1) ]

    for i in roads:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [-1]*(n+1)
    bfs(destination,graph,visited)
    for i in sources:
        answer.append(visited[i])

    return answer