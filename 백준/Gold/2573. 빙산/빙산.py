import sys
sys.setrecursionlimit(10**4)
from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):

    elem = list(map(int,input().split()))

    graph.append(elem)


def year(graph):

    array = deque([])

    for i in range(1,N-1):
        for j in range(1,M-1):
            if graph[i][j] !=0:
                check_list = [  graph[i-1][j],graph[i+1][j],graph[i][j-1],graph[i][j+1]]
                array.append(check_list.count(0))

    for i in range(1,N-1):
        for j in range(1,M-1):
            if graph[i][j] !=0:
                arround = array.popleft()
                graph[i][j]-=arround
                if graph[i][j]<0:
                    graph[i][j] = 0

    return graph


def dfs(x,y,visited,graph):

    visited[x][y]=True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and graph[nx][ny]!=0:
            if not visited[nx][ny]:
                dfs(nx,ny,visited,graph)

t = 0 # 년차

while True:
    result = 0
    visited = [ [False] * M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] != 0:
                dfs(i,j,visited,graph)
                result+=1

    if result > 1:
        print(t)
        break

    else:
        t += 1
        graph = year(graph)

        if sum(map(sum,graph))==0:
            print(0)
            break

