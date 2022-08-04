N = int(input())

S_list = [ [0]*12   ]

for i in range(N):
    S_line = [0] + list(input()) + [0]
    S_list.append(S_line)

S_list = S_list + [[0]*12]

I_list = [ [0]*12   ]

for i in range(N):
    I_line = [0] + list(input()) + [0]
    I_list.append(I_line)

I_list = I_list + [[0]*12]

result_list = [ ['.' for i in range(N)] for _ in range(N)   ]

cnt_list = [ [0 for i in range(N)] for _ in range(N)   ]

for i in range(N):
    for j in range(N):
        cnt_list[i][j] = S_list[i][j:j+3].count('*') + S_list[i+1][j:j+3].count('*') + S_list[i+2][j:j+3].count('*')

cnt=0

for i in range(1,N+1):
    for j in range(1,N+1):
        if S_list[i][j] == '.' and I_list[i][j]== '.' :
            result_list[i-1][j-1] = '.'
        elif S_list[i][j] == '.' and I_list[i][j]== 'x' :
            result_list[i-1][j-1] = cnt_list[i-1][j-1]
        elif S_list[i][j] == '*' and I_list[i][j] == 'x':
            cnt+=1

if cnt>=1:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if S_list[i][j] == '*':
                result_list[i-1][j-1] = '*'


for i in range(N):
    for j in range(N):
        print(result_list[i][j],end='' )
    print()


