import copy,sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [  list(map(int,input().split())) for _ in range(N)      ]
ori_graph = copy.deepcopy(graph)

def dfs(x,y,k):

    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False


    if ori_graph[x][y] > k:
        ori_graph[x][y] = 0

        dfs(x+1, y,k)
        dfs(x-1, y,k)
        dfs(x, y+1,k)
        dfs(x, y-1,k)

        return True

    return False



result_max = 0

for k in range(1,100):
    result = 0

    for i in range(N):
        for j in range(N):
            if dfs(i,j,k) == True:
                result +=1

    ori_graph = copy.deepcopy(graph)

    if result > result_max:
        result_max = result


if result_max == 0:
    print(1)
else:
    print(result_max)
