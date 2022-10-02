from collections import deque


N,M = map(int,input().split())

graph = [ [] for _ in range(N+1) ]

for i in range(M):

    A,B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)


def bfs(X,N):

    distance = [0] * (N + 1)
    distance[X] = 0

    q = deque([X])

    while q:
        now = q.popleft()

        for next_node in graph[now]:

            if distance[next_node] == 0:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    distance[X] = 0

    return sum(distance)


bfs_list = []

for i in range(1,N+1):
    bfs_list.append(bfs(i,N))


print(bfs_list.index(min(bfs_list))+1)




