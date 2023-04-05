import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(N)]

t = 0

def background(a,b,visited):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    graph[a][b]=2

    visited[a][b]=True

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<N and 0<=ny<M:
            if not visited[nx][ny] and (graph[nx][ny]==0 or graph[nx][ny]==2):
                visited[nx][ny]=True
                graph[nx][ny]=2
                background(nx,ny,visited)


def arround(a,b):

    cnt = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if graph[nx][ny]==2:
            cnt+=1

    return cnt

while True:

    t += 1
    ch_list = []
    visited = [ [ False for _ in range(M)] for _ in range(N) ]
    background(0,0,visited)

    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and arround(i,j) >1:
                ch_list.append((i,j))

    for i in ch_list:
        graph[i[0]][i[1]] = 2

    check = True

    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                check = False

    if check:
        break

print(t)
