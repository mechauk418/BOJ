from collections import deque

a,b = map(int,input().split())
N,M = map(int,input().split())

graph = [ [] for _ in range(N+1)  ]

for i in range(M):

    A,B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)



def bfs():

    visited = [False] * (N + 1)
    q = deque([(a, 0)])
    visited[a] = True

    while q:

        x,cnt = q.popleft()


        if x == b:
            print(cnt)
            return

        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                q.append((i,cnt+1))

    print(-1)

bfs()