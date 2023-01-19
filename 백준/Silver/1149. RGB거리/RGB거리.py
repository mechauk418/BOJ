N = int(input())
H_list = []
for i in range(N):
    H_list.append(list(map(int, input().split())))

for i in range(1, N):
    H_list[i][0] = min(H_list[i - 1][1], H_list[i - 1][2]) + H_list[i][0]
    H_list[i][1] = min(H_list[i - 1][0], H_list[i - 1][2]) + H_list[i][1]
    H_list[i][2] = min(H_list[i - 1][0], H_list[i - 1][1]) + H_list[i][2]


print(min(H_list[N - 1][0], H_list[N - 1][1], H_list[N - 1][2]))



# 26 40 83
# 89 86 83
# 96 172 185


