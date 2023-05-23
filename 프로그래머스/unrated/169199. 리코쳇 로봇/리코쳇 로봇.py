from collections import deque

def solution(board):

    graph = []
    answer = 0
    for i in board:
        graph.append(list(i))
    N = len(graph)
    M = len(graph[0])
    q = deque([])
    visited = [ [0 for _ in range(M)] for _ in range(N) ]
    start_x, start_y = 0,0
    for i in range(N):
        for j in range(M):
            if graph[i][j]=='R':
                start_x,start_y = i,j
                q.append([start_x,start_y])

    visited[start_x][start_y] = 1

    while q:

        x,y = q.popleft()

        if board[x][y]=='G':
            answer = visited[x][y]-1
            break

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]


        for i in range(4):
            nx = x
            ny = y

            while True:
                nx = nx+dx[i]
                ny = ny+dy[i]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])

    if answer == 0:
        answer = -1
    return answer