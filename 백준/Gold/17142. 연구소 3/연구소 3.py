from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

com = [0] * M 
result = 10000000


def comb(cur, cnt): 
    global result
    if (cnt == M): 
        result = min(result, bfs()) 
        return
    for i in range(cur, len(v)):
        com[cnt] = i
        comb(i + 1, cnt + 1)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():  # bfs   
    queue = deque()
    visited = [[-1] * N for _ in range(N)]  
    for i in com:  
        queue.append([v[i][0], v[i][1]])
        visited[v[i][0]][v[i][1]] = 0 

    while queue: 
        cx, cy = queue.popleft()  
        for d in range(4):  
            nx = cx + dx[d]
            ny = cy + dy[d]
            if (nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] != -1):  
                continue
            if (arr[nx][ny] == 0 or arr[nx][ny] == 2):  
                queue.append([nx, ny])  
                visited[nx][ny] = visited[cx][cy] + 1 

    time = 0
    for i in range(N):
        for j in range(N):
            if (arr[i][j] == 0):  
                if (visited[i][j] == -1):  
                    return 10000000 
                time = max(time, visited[i][j]) 
    return time  


v = []  
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:  
            v.append([i, j]) 

comb(0, 0)  # 조합

if result == 10000000:  
    result = -1

print(result)