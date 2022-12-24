import sys

def bfs():                             
    for x in range(N):
        for y in range(M):
            if campus[x][y] == 'I':
                return (x, y)               


N, M = map(int, input().split())
campus = sys.stdin.read().splitlines()

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]   

stack = [bfs()]                         
flag = [[True]*M for _ in range(N)]        
cnt = 0                                     

while stack:

    dx, dy = stack.pop()                   
    for xy in move:                       
        x = dx + xy[0]
        y = dy + xy[1]

        if (0 <= x < N) and (0 <= y < M):   
            if (campus[x][y] != 'X') and flag[x][y]:
                stack.append((x, y))
                flag[x][y] = False         

                if campus[x][y] == 'P':
                    cnt += 1

if cnt:
    print(cnt)
else:
    print('TT')