from collections import deque
from pprint import pprint

n,m = map(int,input().split())


graph = []
visited = [[ 0 for i in range(m) ] for _ in range(n)]
visited_check = [[ 0 for i in range(m) ] for _ in range(n)]


for i in range(n):
    asdf = list(map(int,input().split()))

    graph.append(asdf)


for i in range(n):
    for j in range(m):

        if graph[i][j] ==2:
            start = (i,j)





q = deque([start])


while q:

    x,y = q.popleft()

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny] ==1 and visited_check[nx][ny]==0:
            visited_check[nx][ny]=1
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j]==0:
            visited[i][j]=-1

        if graph[i][j]==0:
            visited[i][j]=0

for i in visited:
    print(*i)


