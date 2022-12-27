from pprint import pprint
from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):

    ap_list = list(input())

    graph.append(ap_list)



def bfs(x,y):

    visited = [[0] * M for _ in range(N)]
    distance = [[0] * M for _ in range(N)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque([(x,y)])
    visited[x][y]=True

    while q:

        cur_x,cur_y = q.popleft()

        for i in range(4):

            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and graph[nx][ny]=='L':
                visited[nx][ny]=True
                q.append((nx,ny))
                distance[nx][ny] = distance[cur_x][cur_y]+1


    return max(map(max,distance))


ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':

            check_num = bfs(i,j)

            if check_num>ans:
                ans = check_num

print(ans)
