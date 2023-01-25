from collections import deque

N,M,R = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(N) ]


def rev(y, x, height, width):
    global graph
    q = deque()

    for i in range(x, x + width):
        q.append(graph[y][i])

    for i in range(y + 1, y + height):
        q.append(graph[i][x + width - 1])

    for i in range(x + width - 2, x, -1):
        q.append(graph[y + height - 1][i])

    for i in range(y + height - 1, y, -1):
        q.append(graph[i][x])

    q.rotate(-R)

    for i in range(x, x + width):
        graph[y][i] = q.popleft()

    for i in range(y + 1, y + height):
        graph[i][x + width - 1] = q.popleft()

    for i in range(x + width - 2, x, -1):
        graph[y + height - 1][i] = q.popleft()

    for i in range(y + height - 1, y, -1):
        graph[i][x] = q.popleft()


height = N
width = M
y, x = 0, 0

while True:
    if height == 0 or width == 0:
        break

    rev(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in range(N):
    for j in range(M):
        print(graph[i][j], end=' ')
    print()