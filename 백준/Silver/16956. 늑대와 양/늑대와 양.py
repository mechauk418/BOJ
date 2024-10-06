r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'S':
                        print(0)
                        exit()
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'D'
print(1)
for i in range(r):
    print(*graph[i], sep='')