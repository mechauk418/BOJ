
N = int(input())

N_list = []

for i in range(N):

    N_list.append( list(map(int,input().split())) )


for i in range(1,N):
    for j in range(i+1):

        if i == 1:
            N_list[i][j] += N_list[0][0]
        else:
            if j==0:
                N_list[i][j] += N_list[i-1][0]
            elif j==i:
                N_list[i][j] += N_list[i-1][j-1]
            else:
                N_list[i][j] += max(N_list[i-1][j-1],N_list[i-1][j])


print(max(N_list[-1]))