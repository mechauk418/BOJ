from collections import deque

r,c = map(int,input().split())

graph = []

for i in range(r):
    temt = input()
    temt_list = []
    for j in range(c):
        temt_list.append(temt[j])
    graph.append(temt_list)

count = int(input())

throw_list = list(map(int,input().split()))


def destroy(height,turn):
    if turn % 2 ==1:
        for i in range(c-1,-1,-1):
            if graph[height][i]=='x':
                graph[height][i]='.'
                break

    else:
        for i in range(c):
            if graph[height][i]=='x':
                graph[height][i]='.'
                break

    return graph

def find(graph):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0 for _ in range(c)] for _ in range(r) ]

    q = deque()
    for i in range(c):
        if graph[r-1][i]=='x':
            q.append((r-1,i))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny]==0 and graph[nx][ny]=='x':
                    visited[nx][ny]=1
                    q.append((nx,ny))

    cluster = []
    for i in range(r-1,-1,-1):
        for j in range(c):
            if graph[i][j]=='x' and visited[i][j]==0:
                temt = [i,j]
                cluster.append(temt)

    if len(cluster)>0:
        return cluster,1,visited
    else:
        return cluster,0,visited

def down(graph, cluster, visited):
    down_min = 1e9
    for x, y in cluster:
        down_cnt = 0
        for i in range(x+1, r):
            if graph[i][y] == '.':
                down_cnt += 1
            if graph[i][y] == 'x' and visited[i][y] == True:
                break
        down_min = min(down_min, down_cnt)
    for x, y in cluster:
        graph[x][y] = '.'
        graph[x+down_min][y] = 'x'
    return graph

for i in range(count):
    graph = destroy(r-throw_list[i],i)
    cluster,check,visit = find(graph)
    if check==1:
        graph = down(graph,cluster,visit)

for i in range(r):
    for j in range(c):
        print(graph[i][j],end='')
    print()