from collections import deque
N,K = map(int,input().split())

visited = [-1]*100001
visited[N]=0
route =[ [] for i in range(100001)]
route[N].append(N)
q = deque([N])


def move(now):
    data =[ ]
    temt = now
    for _ in range(visited[now]+1):
        data.append(temt)
        temt = route[temt]

    print(' '.join(map(str,data[::-1])))

while q:

    now = q.popleft()
    if now==K:
        print(visited[K])
        move(now)
        break

    rot = [2*now, now+1, now-1]

    for i in rot:
        nx = i


        if 0<=nx<=100000:
            if visited[nx]==-1:
                visited[nx]=visited[now]+1
                route[nx] = now
                q.append(nx)

            if nx==K:
                break
