from collections import deque

N,k = map(int,input().split())

graph_left = list(map(int,input()))
graph_right = list(map(int,input()))
visited_left = [ 0 for _ in range(N) ]
visited_rigth = [ 0 for _ in range(N) ]
graph = [ graph_left, graph_right]
visted = [visited_left, visited_rigth]
visted[0][0]=True

def bfs():
    i = 0
    q = deque([(i, 0,0)])

    while q:

        i,pos,t = q.popleft()
        dx = [1,-1,k]

        for j in range(3):

            nx = i + dx[j]

            if nx >= N:
                return print(1)

            if t< nx and graph[pos][nx] == 1 and j != 2:
                if not visted[pos][nx]:
                    visted[pos][nx] = True
                    q.append((nx,pos,t+1))

            elif t< nx and graph[1-pos][nx] == 1 and j == 2:
                if not visted[1-pos][nx]:
                    visted[1 - pos][nx] = True
                    q.append((nx,1-pos,t+1))

    print(0)


bfs()