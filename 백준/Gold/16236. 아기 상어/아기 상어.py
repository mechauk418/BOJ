from collections import deque

N = int(input())

graph = []

for _ in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)


dx = [-1,0,1,0]
dy = [0,-1,0,1]


shark = 2


for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            start = (i,j)

x,y = start

def bfs(x,y,shark):

    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque([(x,y)])

    visited[x][y]=1
    temp = []

    while q:

        cur_x,cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny]=distance[cur_x][cur_y]+1

                    if graph[nx][ny] < shark and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))

    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
result = 0

while True:

    sk = bfs(x,y,shark)

    if len(sk)==0:
        break

    nx,ny,dist = sk.pop()

    result += dist
    graph[x][y],graph[nx][ny]=0,0

    x,y = nx,ny

    cnt +=1

    if cnt == shark:

        shark+=1

        cnt = 0


print(result)


