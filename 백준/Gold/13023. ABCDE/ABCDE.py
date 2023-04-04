import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

graph = [ [] for _ in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(x,visited,cnt):

    global answer

    if cnt == 4:
        answer = 1
        return

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:

            dfs(i,visited,cnt+1)

    visited[x] = False


for i in range(N):
    answer = 0

    visited = [False for _ in range(N)]
    dfs(i,visited,0)
    if answer == 1:
        print(answer)
        break

else:
    print(0)
