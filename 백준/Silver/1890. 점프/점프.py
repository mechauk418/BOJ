N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

dp=[ [0]*N for _ in range(N)]

dp[0][0]=1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        if j + graph[i][j] < N:
            dp[i][j+graph[i][j]] += dp[i][j] 
        if i + graph[i][j] < N:
            dp[i+graph[i][j]][j] += dp[i][j]
            
print(dp[N-1][N-1])