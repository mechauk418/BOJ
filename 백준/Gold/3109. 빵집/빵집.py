import sys
sys.setrecursionlimit(10**4)
R,C = map(int,input().split())

graph = [ list((input())) for _ in range(R) ]
visited = [ [False]*C for _ in range(R)  ]
cnt = 0

def dfs(a,b):
    global cnt

    dx = [-1,0,1]
    dy = [1,1,1]


    if b==(C-1):
        return True

    for i in range(3):

        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<R and 0<=ny<C:
            if not visited[nx][ny] and graph[nx][ny]=='.':
                visited[nx][ny]=True
                if dfs(nx,ny):
                    return True

    return False


for i in range(R):
    visited[i][0]=True
    if dfs(i,0):
        cnt+=1

print(cnt)