from collections import deque

K = int(input())
W,H = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(H) ]

start = [0,0,0]


nor = [ [1,0],[-1,0],[0,1],[0,-1] ]
spc = [[-2,-1], [-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

    q = deque()

    q.append(start)
    visited[0][0][0]=1

    while q:

        x,y,z = q.popleft()
        if x==H-1 and y==W-1:
            return visited[x][y][z]-1

        for i,j in nor:

            dx,dy = x+i,y+j
            if 0<=dx<H and 0<=dy<W and not visited[dx][dy][z] and not graph[dx][dy]:
                visited[dx][dy][z] = visited[x][y][z]+1
                q.append([dx,dy,z])

        if z<K:
            for (hi,hj) in spc:
                hx, hy = x + hi, y + hj
                if 0 <= hx < H and 0 <= hy < W:
                    if not graph[hx][hy]:
                        if not visited[hx][hy][z + 1]:
                            visited[hx][hy][z + 1] = visited[x][y][z] + 1
                            q.append([hx, hy, z + 1])

    return -1

print(bfs())