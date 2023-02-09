from collections import deque

def bfs(x,y,graph):
    visited = [[ 0 for _ in range(5)] for _ in range(5)]
    visited[x][y] = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque([(x,y)])

    while q:

        now_x,now_y = q.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0<=nx<5 and 0<=ny<5 and graph[nx][ny] == 'O':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    q.append((nx,ny))

            elif 0<=nx<5 and 0<=ny<5 and graph[nx][ny] == 'P':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[now_x][now_y] + 1
                    return visited[nx][ny]-1

    return 3


def solution(places):
    answer = []


    for pac in places:
        graph = []
        check = True
        for i in range(5):
            graph.append(list(pac[i]))
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if bfs(i,j,graph)<=2:
                        check = False


        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer