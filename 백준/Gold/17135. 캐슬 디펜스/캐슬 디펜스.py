from itertools import combinations
from collections import deque

n,m,d = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(n) ]

dx = [0,-1,0]
dy = [-1,0,1]

def bfs(arrow):

    temt = [x[:] for x in graph]

    killed = [ [0] *m for _ in range(n) ]

    result = 0

    for i in range(n-1,-1,-1):
        this_turn = []

        for ay in arrow:

            q = deque(  [  (i,ay,1) ] )

            while q:

                x,y,dist = q.popleft()

                if temt[x][y]==1:
                    this_turn.append((x,y))

                    if killed[x][y]==0:
                        killed[x][y]=1
                        result+=1

                    break

                if dist<d:
                    for di in range(3):
                        nx = x+dx[di]
                        ny = y + dy[di]
                        if 0<=nx<n and 0<=ny<m:
                            q.append((nx,ny,dist+1))

        for x,y in this_turn:
            temt[x][y]=0

    return result

ans = 0

arrow_pos = list(combinations([i for i in range(m)],3))

for a in arrow_pos:
    ans = max(ans,bfs(a))

print(ans)