import sys
sys.setrecursionlimit(100000)
M,N = map(int,sys.stdin.readline().split())
N,M = M,N # 편하게 보기 위해 M,N 스왑
graph = []

for i in range(N):
    temt = list(map(int,sys.stdin.readline().split()))
    graph.append(temt)

DP = [ [-1] *M for _ in range(N)]

def dfs(x,y):

    if (x,y) == (N-1,M-1):
        return 1

    if DP[x][y]==-1:
        DP[x][y]=0

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]<graph[x][y]:
                DP[x][y] += dfs(nx,ny)

    return DP[x][y]

print(dfs(0,0))

