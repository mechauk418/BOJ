import sys

def dfs(x, y, z):
    global answer
    visited = graph[x][y]

    for i in range(x, x + z):
        for j in range(y, y + z):
            if graph[i][j] != visited:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0, 0]
dfs(0, 0, n)
[print(res) for res in answer]