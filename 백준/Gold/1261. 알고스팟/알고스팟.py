import heapq

M,N = map(int,input().split())

graph = []

for i in range(N):

    graph.append(list(map(int,input())))


dist = [ [99999999] * M for _ in range(N) ]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dij():

    q= []

    heapq.heappush(q,(0,0,0))
    dist[0][0] = 0
    while q:
        cost,x,y = heapq.heappop(q)

        if cost > dist[x][y]:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx >= N or ny < 0 or ny >= M:
                continue

            if cost + graph[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(q,(dist[nx][ny],nx,ny))

dij()

print(dist[N-1][M-1])