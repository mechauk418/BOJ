import heapq

N,M,X = map(int,input().split())
graph = [ [] for _ in range(N+1)]


for i in range(M):

    s,e,t = map(int,input().split())

    graph[s].append((e,t))


q = []

def dij(start):

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:

        dist,now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

ans_list = [0] * (N+1)

for i in range(1,N+1):

    if i==X:
        INF = 10 ** 9
        distance = [INF] * (N + 1)
        dij(i)
        for j in range(1,N+1):
            ans_list[j]+=distance[j]

    else:

        INF = 10 ** 9
        distance = [INF] * (N + 1)
        dij(i)
        ans_list[i]+=distance[X]


print(max(ans_list))