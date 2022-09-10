import sys
sys.setrecursionlimit(10**6)

while True:

    w,h = map(int,input().split())
    if w == 0 and h ==0:
        break

    S_graph = [ list(map(int,input().split())) for _ in range(h) ]

    def dfs(x,y):
        if x<=-1 or x>=h or y<=-1 or y>=w:
            return False

        if S_graph[x][y] == 1:
            S_graph[x][y] = 0

            dfs(x+1,y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x+1,y+1)
            dfs(x-1,y-1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)

            return True
        return False

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result +=1

    print(result)

