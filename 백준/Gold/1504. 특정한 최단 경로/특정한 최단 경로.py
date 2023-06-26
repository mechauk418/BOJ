import heapq
import sys
input = sys.stdin.readline

N,E = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
INF = 10**9

distance = [INF] * (N+1)

for i in range(E):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))

    graph[b].append((a,c))


v1,v2 = map(int,input().split())

q = []

def dij(start):

    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:

        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

ans1 = 0
ans2 = 0

dij(1)

ans1+=distance[v1]
ans2+=distance[v2]

distance = [INF] * (N+1)

dij(v1)

ans1+=distance[v2]
ans2+=distance[N]

distance = [INF] * (N+1)

dij(v2)

ans1+=distance[N]
ans2+=distance[v1]

ans = min(ans1,ans2)
if ans >= INF:
    print(-1)
else:
    print(ans)

