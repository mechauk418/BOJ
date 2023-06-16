from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    ans = 0

    def bfs(a, b, graph, visited):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited[a][b] = 1
        q = deque([(a, b)])
        N = len(maps)
        M = len(maps[0])
        while q:

            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] in ['O', 'L', 'E', 'S']:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                leva = [i, j]
            elif maps[i][j] == 'E':
                end = [i, j]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    bfs(start[0], start[1], maps, visited)

    ans += visited[leva[0]][leva[1]] - 1

    visited2 = [[0 for _ in range(M)] for _ in range(N)]

    bfs(leva[0], leva[1], maps, visited2)

    ans += visited2[end[0]][end[1]] - 1

    if visited[leva[0]][leva[1]] == 0 or visited2[end[0]][end[1]] == 0:
        return -1
    else:
        return ans