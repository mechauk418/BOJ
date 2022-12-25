from collections import deque



def bfs():

    while q:
        x = q.popleft()

        for i in range(8):
            if i<6:
                nx = x+dx[i]
                if 0<= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx]=1
                    s[nx] = s[x]+1
            else:
                nx = x * dx[i]
                if 0<= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx]=1
                    s[nx] = s[x]+1


A,B,N,M = map(int,input().split())

s = [0 for i in range(100001)]
visited = [0 for i in range(100001)]
visited[N] = 1
q = deque([N])
dx = [1,-1,A,-A,B,-B,A,B]
bfs()
print(s[M])