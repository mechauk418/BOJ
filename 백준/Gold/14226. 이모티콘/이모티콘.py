from collections import deque

s = int(input())

visited = [ [0] * 1001 for _ in range(1001) ]

def bfs():

    q = deque()

    ans = 0

    q.append((1,0))

    while q:
        x_screen,x_clip = q.popleft()

        if x_screen == s:
            ans = visited[x_screen][x_clip]
            break

        arr = [(x_screen,x_screen),  (x_screen+x_clip,x_clip),  (x_screen-1,x_clip)  ]

        for screen,clip in arr:
            if 0<=screen<1001 and 0<=clip<1001 and not visited[screen][clip]:
                q.append((screen,clip))
                visited[screen][clip] = visited[x_screen][x_clip]+1

    return ans


print(bfs())