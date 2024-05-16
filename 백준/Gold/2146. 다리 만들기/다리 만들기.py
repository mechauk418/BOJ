from collections import deque
from pprint import pprint
N = int(input())

graph = [ list(map(int,input().split())) for _ in range(N) ]
vistied = [ [ 0 for _ in range(N) ] for _ in range(N) ]



def bfs(x,y,cnt):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append((x,y))

    while q:

        now_x,now_y = q.popleft()
        for i in range(4):
            nx = now_x+dx[i]
            ny = now_y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N or vistied[nx][ny]>0 or graph[nx][ny]==0:
                continue
            vistied[nx][ny]=1
            graph[nx][ny]=cnt
            q.append([nx,ny])

cnt=1
res = 1e9
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and vistied[i][j]==0:
            vistied[i][j]=1
            graph[i][j]=cnt
            bfs(i,j,cnt)
            cnt+=1


def dis(v):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    dist = [ [-1]*N for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if graph[i][j]==v:
                dist[i][j]=0
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] and graph[nx][ny]!=v:
                    return dist[x][y]
                elif not graph[nx][ny] and dist[nx][ny]==-1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))

    return int(1e9)

for v in range(1,cnt):
    res = min(res,dis(v))
print(res)