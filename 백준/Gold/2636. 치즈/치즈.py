from pprint import pprint
from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):

    ap_list = list(map(int,input().split()))

    graph.append(ap_list)


def bfs(graph):

    visited = [[0] * M for _ in range(N)]

    q = deque([(0,0)]) # 0,0은 항상 공기

    visited[0][0]=True

    while q:

        x,y = q.popleft()

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and graph[nx][ny]==0:
                visited[nx][ny]=True
                q.append((nx,ny))

            elif 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny]=True
                graph[nx][ny]=0

count = 0

while True:
    ans = 0
    for i in range(N):
        for j in range(M):
            ans += graph[i][j]
            
    bfs(graph)
    count+=1
    if max(map(max,graph))==0:

        break

print(count)
print(ans)