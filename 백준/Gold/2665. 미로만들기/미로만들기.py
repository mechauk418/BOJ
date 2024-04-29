import heapq

n = int(input())

graph = [ list(map(int,input())) for _ in range(n) ]

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=1
        else:
            graph[i][j]=0


INF = int(1e9)

distance = [ [INF]*(n) for _ in range(n) ]
distance[0][0]=0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = []

def dij():

    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:

        dist, now_x, now_y = heapq.heappop(q)

        if now_x == n-1 and now_y == n-1:
            break

        for i in range(4):

            next_x = now_x+dx[i]
            next_y = now_y+dy[i]

            if 0<=next_x<n and 0<=next_y<n:

                cost = dist + graph[next_x][next_y]

                if cost<distance[next_x][next_y]:
                    distance[next_x][next_y] = cost
                    heapq.heappush(q,(cost,next_x,next_y))

dij()

print(distance[n-1][n-1])