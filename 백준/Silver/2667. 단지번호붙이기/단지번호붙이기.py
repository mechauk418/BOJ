
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False



    if graph[x][y] == 1:
        graph[x][y] = 0
        global cnt
        cnt += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)


        return True

    return False


N = int(input())

graph = [ list(map(int,input()))   for _n in range(N) ]

count_list = []

result = 0

for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(i,j) == True:
            result +=1
            count_list.append(cnt)
            cnt=0


print(result)
count_list.sort()
for i in count_list:
    print(i)
