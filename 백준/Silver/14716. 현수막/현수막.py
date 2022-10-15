import sys
sys.setrecursionlimit(10**6)
R,C = map(int,input().split())

graph = [  list(map(int,input().split())) for _ in range(R)       ]

cnt = 0

def dfs(x,y):

    if x<0 or x>=R or y<0 or y>=C:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y+1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x-1, y-1)

        return True

    return False

for i in range(R):
    for j in range(C):
        if dfs(i,j) == True:
            cnt+=1


print(cnt)