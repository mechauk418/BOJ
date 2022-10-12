from pprint import pprint

N,M = map(int,input().split())

graph = [   list(input()) for _ in range(M)    ]

cnt_w = 0
cnt_b = 0

def dfs(x,y):
    global cnt_w
    if x<0 or x>=M or y<0 or y>=N:

        return

    if graph[x][y] == 'W':
        graph[x][y] = 1
        cnt_w +=1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True

    return

def dfs2(x,y):
    global cnt_b
    if x<0 or x>=M or y<0 or y>=N:

        return False

    if graph[x][y] == 'B':
        graph[x][y] = 2
        cnt_b +=1
        dfs2(x+1, y)
        dfs2(x-1, y)
        dfs2(x, y+1)
        dfs2(x, y-1)

        return True

    return False

def countgraph(list,n):
    cnt = 0
    for i in range(M):
        for j in range(N):
            if list[i][j] == n:
                cnt+=1

    return cnt

cnt_list = []
cnt_list2 = []

cnt = 0
for i in range(M):
    for j in range(N):
        if dfs(i,j) == True:
            cnt_list.append(cnt_w)
            cnt_w = 0
        if dfs2(i,j) == True:
            cnt_list2.append(cnt_b)
            cnt_b = 0


ans1 = 0
ans2 = 0

for i in cnt_list:
    ans1 += i*i

for j in cnt_list2:
    ans2 += j*j

print(ans1, ans2)