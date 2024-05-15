from collections import deque

N,M = map(int,input().split())

DP=[0]*101

visited = [False] * 101

sadari = dict()
snake = dict()

for _ in range(N):
    a,b = map(int,input().split())
    sadari[a]=b

for _ in range(M):
    a,b = map(int,input().split())
    snake[a]=b

q = deque([1])

while q:
    x = q.popleft()

    if x==100:
        print(DP[x])

        break

    for i in range(1,7):

        nx = x+i
        if nx<=100 and not visited[nx]:
            if nx in sadari.keys():
                nx = sadari[nx]

            if nx in snake.keys():
                nx = snake[nx]

            if not visited[nx]:
                visited[nx]=True
                DP[nx] = DP[x]+1

                q.append(nx)
