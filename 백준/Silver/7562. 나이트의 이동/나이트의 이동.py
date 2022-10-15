from pprint import pprint
from collections import deque


def bfs(x,y,end1,end2):

    q = deque([(x,y)])

    graph[x][y] = 1

    while q:

        x,y = q.popleft()

        if x == end1 and y == end2:
            return graph[x][y]-1



        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1


T = int(input())

for t in range(T):


    N = int(input())

    graph = [ [ 0 for _ in range(N)] for _ in range(N) ]

    x,y = map(int,input().split())
    end1,end2 = map(int,input().split())

    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    print(bfs(x,y,end1,end2))