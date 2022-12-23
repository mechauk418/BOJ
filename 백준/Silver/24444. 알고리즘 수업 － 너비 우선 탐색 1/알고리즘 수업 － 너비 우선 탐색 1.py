from collections import deque
import sys
N,M,R = map(int,sys.stdin.readline().split())

graph = [ [] for _ in range(N+1) ]

for i in range(M):
    A,B = map(int,sys.stdin.readline().split())

    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

visited_bfs = [0] * (N+1)

root_bfs = []


def bfs(x):

    queue = deque([x])

    visited_bfs[x] = 1
    count = 2

    while queue:

        t = queue.popleft() # 1
        root_bfs.append(t)

        for i in graph[t]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = count
                count +=1


bfs(R)

for i in visited_bfs[1::]:
    print(i)