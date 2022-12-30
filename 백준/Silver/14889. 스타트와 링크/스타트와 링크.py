
N = int(input())

T = int(N/2) # 팀 인원수


def dfs(depth,idx):

    global min_diff

    if depth == T:

        power1,power2=0,0

        for i in range(N):
            for j in range(N):

                if visited[i] and visited[j]:
                    power1+=graph[i][j]

                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]


        min_diff = min(min_diff,abs(power1-power2))

        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1,i+1)
            visited[i]=False

visited = [ 0 for _ in range(N)]

graph = [ list(map(int,input().split())) for _ in range(N)]

min_diff = int(1e9)

dfs(0,0)
print(min_diff)