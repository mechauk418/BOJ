def dfs(visted, x, graph):
    visted[x] = True

    for i in graph[x]:
        if not visted[i] :
            dfs(visted, i, graph)


N = int(input())
M = int(input())

org_list = [[ 0 for _ in range(N+1) ] for _ in range(N+1)    ]

for i in range(M):
    u,v = map(int,input().split())
    org_list[u][v] = 1
    org_list[v][u] = 1

ad_list = [[ 0 for _ in range(N+1) ] for _ in range(N+1)    ]

for i in range(N+1):
    ad_list[i] = [ k for k in range(N+1) if org_list[i][k] == 1    ]

ans_list = []

visted = [0]*(N+1)


dfs(visted,1,ad_list)


true_list = [ i for i in visted if i == True  ]

print(len(true_list)-1)