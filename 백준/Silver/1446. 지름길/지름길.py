import heapq

N,D = map(int,input().split())

graph = [ [] for _ in range(D+1)]

for i in range(D):

    graph[i].append((i+1,1))

for i in range(N):
    start,end,dist = map(int,input().split())

    if end>D:
        continue
    graph[start].append((end,dist))

INF = 99999999

dp = [INF] * (D+1)

dp[0]=0

q = []

heapq.heappush(q,(0,0))

while q:
    d,now = heapq.heappop(q)
    if dp[now] < d:
        continue

    for x in graph[now]:
        cost = d+x[1]

        if dp[x[0]] > cost:
            dp[x[0]] = cost
            heapq.heappush(q,(cost,x[0]))


print(dp[D])

