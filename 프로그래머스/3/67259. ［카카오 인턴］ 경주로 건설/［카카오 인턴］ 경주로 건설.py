from collections import deque

def solution(board):
    def bfs(start):
        direc = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]} 
        length = len(board)
        visited = [[987654321]*length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start]) 
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4): 
                nx = x + direc[i][0]
                ny = y + direc[i][1]

                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    
                    if i == d : ncost = cost + 100
                    else : ncost =  cost + 600
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])
                        
        return visited[-1][-1]
    
    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])