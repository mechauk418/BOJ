import heapq
import sys
input = sys.stdin.readline
N = int(input())

M = int(input())
INF = 10**9
graph = [ [] for _ in range(N+1) ]
dis = [INF] * (N+1)

q = []

for i in range(M):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))

s,e = map(int,input().split())

def dij(start):

    heapq.heappush(q,(start,0)) # 노드, 가중치

    while q:

        now, dist = heapq.heappop(q)

        if dis[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

dij(s)

print(dis[e])