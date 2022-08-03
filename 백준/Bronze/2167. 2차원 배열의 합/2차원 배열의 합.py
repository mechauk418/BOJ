import sys

N,M = map(int,sys.stdin.readline().split())

S_list = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)   ]


K = int(sys.stdin.readline())


for k in range(K):
    sum_line = 0
    i,j,x,y = map(int,sys.stdin.readline().split()) # 1 1 2 3

    for row in range(i,x+1):  # 1,3 => 1~ 2
        sum_line += sum(S_list[row-1][j-1:y])

    print(sum_line)

