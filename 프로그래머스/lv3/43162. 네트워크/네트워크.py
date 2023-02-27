def dfs(visited,x,n,graph):
    visited[x] = True
    for k in graph[x]:
        if not visited[k]:
            dfs(visited,k,n,graph)


def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    ans_vis = []
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                if j+1 not in graph[i+1]:
                    graph[i+1].append(j+1)
                if i+1 not in graph[j+1]:
                    graph[j+1].append(i+1)


    for i in range(1,n+1):
        visited=[False]*(n+1)
        dfs(visited,i,n,graph)
        if visited not in ans_vis:
            ans_vis.append(visited)


    answer = len(ans_vis)

    print(answer)

    return answer