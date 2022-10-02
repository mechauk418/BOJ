from collections import deque

N = int(input())

a,b=map(int,input().split())

M = int(input())

graph = [  [] for _ in range(N+1) ]

for i in range(M):

    A,B = map(int,input().split())

    graph[A].append(B)
    graph[B].append(A)



distance = [ -1 ] * (N+1)
distance[a] = 0

q = deque([a])

while q:
    now = q.popleft()

    for next_nod in graph[now]:


        if distance[next_nod] == -1:
            distance[next_nod] = distance[now] +1
            q.append(next_nod)





print(distance[b])


