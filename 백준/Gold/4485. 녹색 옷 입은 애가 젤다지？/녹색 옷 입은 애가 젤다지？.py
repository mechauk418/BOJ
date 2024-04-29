import heapq

def dij():
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0] = 0

    while q:

        dist,now_x,now_y = heapq.heappop(q)

        if now_x == N-1 and now_y == N-1:
            print(f'Problem {cnt}: {distance[now_x][now_y]}')
            break

        for i in range(4):
            new_x = now_x+dx[i]
            new_y = now_y+dy[i]

            if 0<=new_x<N and 0<=new_y <N:
                cost = dist + graph[new_x][new_y]

                if cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = cost
                    heapq.heappush(q,(cost,new_x,new_y))


cnt = 0

while True:
    cnt+=1
    N = int(input())
    if N==0:
        break
    graph = [ list(map(int,input().split())) for _ in range(N)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    INF = int(1e9)
    distance = [[INF]*N for _ in range(N)]

    dij()



