import copy,sys
sys.setrecursionlimit(10**6)

def dfs(x,y):

    if x<0 or x>=M or y<0 or y>=N:
        return False


    if graph[x][y] == 0:
        graph[x][y] = 1
        global cnt
        cnt+=1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True

    return False


M,N,K = map(int,input().split())

graph = [  [0 for _ in range(N)] for _ in range(M)    ]


for _ in range(K):
    a,b,c,d = map(int,input().split())

    for i in range(b,d):
        for j in range(a,c):
            graph[i][j] = 1


count_list = []
result = 0

for i in range(M):
    for j in range(N):
        cnt = 0

        if dfs(i,j) == True:
            result +=1
            count_list.append(cnt)
            cnt=0

print(result)
count_list.sort()
for i in count_list:
    print(i,end=' ')

