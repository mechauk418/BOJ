from collections import deque

R,C = map(int,input().split())

graph = []
water = []

for i in range(R):
    temt = list(input())

    graph.append(temt)

for i in range(R):
    for j in range(C):
        if graph[i][j]=='*':
            water.append([i,j])
        elif graph[i][j]=='D':
            D=[i,j]
        elif graph[i][j] == 'S':
            S=[i,j]

dist =[ [ 0 for _ in range(C) ] for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append(S)

    for w in water:
        q.append(w)

    while q:

        now_x,now_y = q.popleft()

        if graph[D[0]][D[1]]=='S':
            return dist[D[0]][D[1]]

        for i in range(4):
            nx = now_x+dx[i]
            ny = now_y + dy[i]

            if 0<=nx<R and 0<=ny<C:
                if graph[now_x][now_y]=='S' and (graph[nx][ny] == '.' or graph[nx][ny]=='D'):
                    graph[nx][ny]='S'
                    dist[nx][ny]=dist[now_x][now_y]+1
                    q.append([nx,ny])

                elif graph[now_x][now_y]=='*' and (graph[nx][ny]=='.' or graph[nx][ny]=='S'):
                    graph[nx][ny] = '*'
                    q.append([nx, ny])

    return "KAKTUS"

print(bfs())