N = int(input())

graph = [ list(map(int,input())) for _ in range(N) ]

def divide(x,y,N):

    num = graph[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if num != graph[i][j]:
                num = -1
                break

    if num == -1:
        print('(',end='')
        divide(x,y,N//2)
        divide(x,y+N//2,N//2)
        divide(x+N//2, y, N // 2)
        divide(x+N//2, y+N//2, N // 2)
        print(')',end="")
    elif num ==1:
        print(1,end="")

    else:
        print(0,end="")

divide(0,0,N)