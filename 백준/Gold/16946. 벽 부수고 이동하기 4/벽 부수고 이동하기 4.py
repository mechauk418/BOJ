import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

graph = [ list(map(int,input())) for _ in range(N) ]

ans_graph = [[0] * M for _ in range(N)]
area_dict=dict()

def dfs(x,y,visited,area):
    global cnt
    cnt+=1
    visited[x][y]=True
    graph[x][y]=area

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):

        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if not visited[nx][ny] and graph[nx][ny]==0:
                dfs(nx,ny,visited,area)

visited = [[False] * M for _ in range(N)]

area = 2

for i in range(N):
    for j in range(M):
        cnt=0
        if graph[i][j]==0:
            dfs(i,j,visited,area)
            area_dict[area] = cnt
            area +=1

for i in range(N):
    for j in range(M):
        ans_list = []
        if graph[i][j]==1:
            ans_graph[i][j] +=1
            ans = 0
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for k in range(4):

                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] >1:
                        ans_list.append(graph[nx][ny])

            ans_list = list(set(ans_list))
            for t in ans_list:
                ans_graph[i][j]+=area_dict[t]

            ans_graph[i][j] = ans_graph[i][j] % 10


for i in ans_graph:
    print(''.join(map(str,i)))
