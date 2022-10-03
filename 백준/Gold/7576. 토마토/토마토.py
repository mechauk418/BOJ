from pprint import pprint
from collections import deque

M,N = map(int,input().split())

distance = [  list(map(int,input().split())) for _ in range(N)    ]

one_list = []

for i in range(N):
    for j in range(M):
        if distance[i][j] == 1:
            one_list.append((i,j))


def bfs(list_):

    q = deque(list_)

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:

        x,y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>= N or ny>=M:
                continue

            if distance[nx][ny]==0:
                distance[nx][ny] = distance[x][y] +1
                q.append((nx,ny))

bfs(one_list)

check = False

for i in range(N):
    for j in range(M):
        if distance[i][j] == 0:
            check = True


max_distance = max(map(max,distance))

if check == True:
    print(-1)
else:
    print(max_distance-1)