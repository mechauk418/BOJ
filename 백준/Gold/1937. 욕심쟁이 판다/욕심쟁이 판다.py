import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [ list(map(int,input().split())) for _ in range(N) ]

DP = [ [ 0 for _ in range(N) ] for _ in range(N)]

def dfs(a,b):

    if DP[a][b]:
        return DP[a][b]

    DP[a][b]=1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] > graph[a][b]:
                DP[a][b] = max(DP[a][b],dfs(nx,ny)+1)

    return DP[a][b]

ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i,j))
        
print(ans)