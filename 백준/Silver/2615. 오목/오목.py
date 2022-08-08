S_list = [ [0]*21   ]

for i in range(19):
    S_line = [0] + list(map(int,input().split()))+[0]

    S_list.append(S_line)

S_list = S_list + [[0]*21]

cnt = 0

#가로

for i in range(1,16):
    for j in range(1,20):
        if S_list[i][j] == 1 and S_list[i + 1][j] == 1 and S_list[i + 2][j] == 1 and S_list[i + 3][j] == 1 and \
                S_list[i + 4][j] == 1 and S_list[i-1][j] != 1 and S_list[i+5][j] !=1:
            print(1)
            print(i, j)
            cnt = 1

for i in range(1,16):
    for j in range(1,20):
        if S_list[i][j] == 2 and S_list[i + 1][j] == 2 and S_list[i + 2][j] == 2 and S_list[i + 3][j] == 2 and \
                S_list[i + 4][j] == 2 and S_list[i-1][j] != 2 and S_list[i+5][j] !=2:
            print(2)
            print(i, j )
            cnt = 1

#세로

for i in range(1,20):
    for j in range(1,16):
        if S_list[i][j] == 1 and S_list[i][j+1] == 1 and S_list[i][j+2] == 1 and S_list[i][j+3] == 1 and \
                S_list[i][j+4] == 1 and S_list[i][j-1] != 1 and S_list[i][j+5] !=1:
            print(1)
            print(i, j)
            cnt = 1

for i in range(1,20):
    for j in range(1,16):
        if S_list[i][j] == 2 and S_list[i][j+1] == 2 and S_list[i][j+2] == 2 and S_list[i][j+3] == 2 and \
                S_list[i][j+4] == 2 and S_list[i][j-1] != 2 and S_list[i][j+5] !=2:
            print(2)
            print(i, j)
            cnt = 1

# \ 대각선

for i in range(1,16):
    for j in range(1,16):
        if S_list[i][j] == 1 and S_list[i+1][j+1] == 1 and S_list[i+2][j+2] == 1 and S_list[i+3][j+3] == 1 and \
                S_list[i+4][j+4] == 1 and S_list[i-1][j-1] != 1 and S_list[i+5][j+5] !=1:
            print(1)
            print(i , j )
            cnt = 1

for i in range(1,16):
    for j in range(1,16):
        if S_list[i][j] == 2 and S_list[i+1][j+1] == 2 and S_list[i+2][j+2] == 2 and S_list[i+3][j+3] == 2 and \
                S_list[i+4][j+4] == 2 and S_list[i-1][j-1] != 2 and S_list[i+5][j+5] !=2:
            print(2)
            print(i , j )
            cnt = 1

# / 대각선

for i in range(1,16):
    for j in range(5,21):
        if S_list[i][j]==1 and S_list[i+1][j-1] == 1 and S_list[i+2][j-2] == 1 and S_list[i+3][j-3] == 1 and \
                S_list[i + 4][j - 4] == 1 and S_list[i+5][j-5] != 1 and S_list[i-1][j+1] != 1:
            print(1)
            print(i+4, j-4)
            cnt=1

for i in range(1,16):
    for j in range(5,21):
        if S_list[i][j]==2 and S_list[i+1][j-1] == 2 and S_list[i+2][j-2] == 2 and S_list[i+3][j-3] == 2 and \
                S_list[i + 4][j - 4] == 2 and S_list[i+5][j-5] != 2 and S_list[i-1][j+1] != 2:
            print(2)
            print(i+4, j-4)
            cnt=1


if cnt ==0:
    print(0)