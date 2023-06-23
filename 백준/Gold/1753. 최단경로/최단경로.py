import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V + 1)]
INF = 10 ** 9
dis = [INF] * (V + 1)
for i in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))

q = []

def move(start):
    heapq.heappush(q, (0, start))

    dis[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[0]
            if cost < dis[i[1]]:
                dis[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


move(K)
for i in range(1, V + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
