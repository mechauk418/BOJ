S= [['' for x in range(15)] for y in range(5)]

for i in range(5):
    N_list = list(map(str,input()))

    for j in range(len(N_list)):
        S[i][j] = N_list[j]


for i in range(15):
    for j in range(5):
        print(S[j][i], end='')