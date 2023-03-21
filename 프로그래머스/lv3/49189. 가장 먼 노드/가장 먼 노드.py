from collections import deque

def solution(n, vertex):
    answer = 0

    graph = [ [] for _ in range(n+1) ]
    visited = [False] * (n+1)
    distance = [0] * (n+1)

    for v in vertex:

        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    for g in graph:
        g.sort()

    q= deque([1])
    visited[1] = True
    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                distance[i] = distance[now]+1
                visited[i] = True
                q.append(i)


    answer = distance.count(max(distance))


    return answer