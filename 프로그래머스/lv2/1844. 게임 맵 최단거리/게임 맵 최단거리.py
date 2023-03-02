from collections import deque

def bfs(x,y,maps,n,m):
    q = deque([(x,y)])
    graph = [[ 1 for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        now_x,now_y = q.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and graph[nx][ny]==1:
                graph[nx][ny] = graph[now_x][now_y] +1
                q.append((nx,ny))

    return graph[n-1][m-1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0,0,maps,n,m)
    if answer ==1:
        answer = -1

    return answer