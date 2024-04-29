import heapq

n,m = map(int,input().split())

graph = [ [] for _ in range(n+1) ]

INF = int(1e9)

ans_list = [ ['-' for _ in range(n) ] for _ in range(n) ]

for i in range(m):

    a,b,c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a, c))


def dij(start):
    q = []
    distance = [INF] * (n + 1)
    distance[0] = 0
    distance[start] = 0
    root = [ [] for _ in range(n+1) ]

    heapq.heappush(q,(0,start,[start]))

    while q:

        dist,now,temt_route = heapq.heappop(q)

        if dist>distance[now]:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost<distance[i[0]]:
                distance[i[0]] = cost
                new_route = temt_route + [i[0]]
                heapq.heappush(q,(cost,i[0],new_route))
                root[i[0]] = new_route

    for i in root[1:]:
        if i:
            print(i[1],end=' ')
        else:
            print('-',end=' ')

    print()

for i in range(1,n+1):
    dij(i)