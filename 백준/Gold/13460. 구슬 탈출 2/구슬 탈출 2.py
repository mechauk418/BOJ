from collections import deque

N,M = map(int,input().split())

graph = [ list(input()) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if graph[i][j]=='R':
            start_x,start_y = i,j

        elif graph[i][j] == 'B':
            blue_x, blue_y = i, j


def bfs(red_x,red_y,blue_x,blue_y):


    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visited = [(red_x,red_y,blue_x,blue_y)]
    cnt = 0

    q = deque()
    q.append((red_x,red_y,blue_x,blue_y))

    while q:

        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()

            if cnt>10:
                print(-1)
                return

            if graph[rx][ry]=='O':
                print(cnt)
                return

            for i in range(4):
                nrx,nry = rx,ry
                while True:
                    nrx+=dx[i]
                    nry += dy[i]
                    if graph[nrx][nry]=='#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry]=='O':
                        break

                nbx,nby=bx,by
                while True:
                    nbx+=dx[i]
                    nby += dy[i]
                    if graph[nbx][nby]=='#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby]=='O':
                        break

                if graph[nbx][nby]=='O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))

        cnt+=1

    print(-1)

bfs(start_x,start_y,blue_x,blue_y)

