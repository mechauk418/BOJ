from collections import deque

N,M,K,X = map(int,input().split())

graph=[ [] for _ in range(N+1) ]

for i in range(M):
    A,B = map(int,input().split())

    graph[A].append(B)


distance = [-1] *(N+1)
distance[X] = 0

q = deque([X])

while q:
    now = q.popleft()

    for next_node in graph[now]:

        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False

for i in range(1,N+1):
    if distance[i]==K:
        print(i)
        check = True

if check == False:
    print(-1)