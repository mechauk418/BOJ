
N = int(input())

graph = [ [] for _ in range(N) ]
visited = [0]*N

N_list = list(map(int,input().split()))

for i in range(len(N_list)):

    if N_list[i] != -1:
        graph[N_list[i]].append(i)

# print(graph)

D = int(input())

# graph = [ [1,2], [3,4], [], [] ,[]    ]

def dfs(D):

    visited[D]=True

    for i in graph[D]:
        if not visited[i]:
            dfs(i)

dfs(D)

# print(visited)
cnt = 0
for i in range(len(graph)):
    if visited[i] == 0 and (len(graph[i]) == 0 or [D] == graph[i]):
        cnt+=1

print(cnt)
