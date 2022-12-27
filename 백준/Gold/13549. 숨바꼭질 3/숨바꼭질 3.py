from collections import deque

N,K = map(int,input().split())

dx = [2,-1,1]

visited = [0] * 100001

def bfs(N,K):

    if N==K:
        return 0

    q = deque([(N, 0)])

    while q:

        cur_x,time = q.popleft()

        for i in range(3):

            if i == 0:

                nx = cur_x * dx[0]

            else:

                nx = cur_x + dx[i]

            if 0<=nx<100001 and visited[nx]==0:
                visited[nx]=True
                if i == 0:
                    q.append((nx,time))
                    if nx == K:
                        return time
                else:
                    q.append((nx,time+1))
                    if nx == K:
                        return time+1


print(bfs(N,K))
