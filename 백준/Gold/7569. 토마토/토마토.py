from collections import deque
M,N,H = map(int,input().split()) # 2 <= M,N <= 100, 1<=H<=100


graph = []

for i in range(H):

    graph_part = []

    for j in range(N):

        line = list(map(int,input().split()))


        graph_part.append(line)


    graph.append(graph_part)

queue = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])


dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while queue:

    x,y,z = queue.popleft()

    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]

        if 0<=a<H and 0<=b<N and 0<=c<M and graph[a][b][c] == 0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z] +1

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)




