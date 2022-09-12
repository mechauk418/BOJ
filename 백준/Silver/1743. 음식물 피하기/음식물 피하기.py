import sys
sys.setrecursionlimit(10**6)


N,M,K = map(int,input().split())

graph = [ [0] * M  for _ in range(N)  ]

for i in range(K):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1


def dfs(x,y):

    if x<0 or x>=N or y<0 or y>=M:
        return False


    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt+=1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True

    return False




count_list = []

for i in range(N):
    for j in range(M):
        cnt = 0

        if dfs(i,j) == True:

            count_list.append(cnt)
            cnt=0

count_list.sort()

print(count_list[-1])