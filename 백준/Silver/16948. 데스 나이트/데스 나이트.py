from collections import deque

N = int(input())

distance = [  [ 0  for _ in range(N)] for _ in range(N)    ]

r1,c1,r2,c2 = map(int,input().split())




def bfs(X,Y):


    q = deque([(X,Y)])
    distance[X][Y] = 1

    while q:

        X,Y = q.popleft()
        dx = [-2, -2, 0, 0, 2, 2]
        dy = [-1, 1, -2, 2, -1, 1]

        for i in range(6):
            nx = X+dx[i]
            ny = Y+dy[i]

            if nx<0 or ny<0 or nx>= N or ny>=N:
                continue

            if distance[nx][ny] ==0:
                distance[nx][ny] = distance[X][Y] +1
                q.append((nx,ny))

    distance[X][Y] = 0

    return distance[r2][c2]

bfs(r1,c1)

print(distance[r2][c2]-1)