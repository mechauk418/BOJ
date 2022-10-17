
N,M = map(int,input().split())

graph = [ list(input()) for _ in range(N) ]

cnt_garo = 0
cnt_sero = 0

def dfs_garo(x,y):

    if x<0 or x>=N or y<0 or y>=M:
        return False

    if graph[x][y] == '-':
        graph[x][y] = 1

        dfs_garo(x,y+1)

        return True

    return False


def dfs_sero(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == '|':
        graph[x][y] = 1

        dfs_sero(x+1, y)

        return True

    return False




for i in range(N):
    for j in range(M):
        if dfs_garo(i,j) == True:
            cnt_garo += 1

        if dfs_sero(i,j) == True:
            cnt_sero += 1

print(cnt_garo+cnt_sero)

