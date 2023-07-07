from collections import deque

def solution(n, m, x, y, r, c, k):

    dirs = ['d','l','r','u']

    def check(x,y,r,c):
        return abs(r-x) + abs(c-y)

    answer = ''

    def bfs():

        dx = [1,0,0,-1]
        dy = [0,-1,1,0]

        q = deque([])
        q.append([x,y,0,''])

        while q:

            now_x,now_y,cnt,root = q.pop()

            if now_x == r and now_y == c:
                if cnt==k:
                    return root

                elif (k-cnt) % 2 == 1:
                    return 'impossible'

            temt = []
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0<nx<=n and 0<ny<=m and check(nx,ny,r,c)+cnt<k:
                    temt.append([nx,ny,cnt+1,root+dirs[i]])

            temt.reverse()
            q += temt

        return 'impossible'

    answer = bfs()

    return answer