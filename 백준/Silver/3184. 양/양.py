from pprint import pprint
import copy, sys
sys.setrecursionlimit(10**6)


R,C = map(int,input().split())

graph = [  list(input()) for _ in range(R)       ]

sheep = 0
wolf = 0

def dfs(x,y):

    global sheep, wolf

    if x<0 or x>=R or y<0 or y>=C:
        return False

    if graph_copy[x][y] != '#':

        if graph_copy[x][y] == 'v':
            wolf += 1
        if graph_copy[x][y] == 'o':
            sheep += 1

        graph_copy[x][y] = '#'

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        if sheep>wolf:
            return sheep
        else:
            return wolf

    return False


graph_copy = copy.deepcopy(graph)

ans1 = 0
ans2 = 0

for i in range(R):
    for j in range(C):
        if dfs(i,j) != False:
            if sheep > wolf:
                ans1 += sheep
            else:
                ans2 += wolf

        wolf = 0
        sheep = 0

print(ans1,ans2)