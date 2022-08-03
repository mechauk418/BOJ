A,B = map(str,input().split())

A_list = list(A)
A_min = [0] * len(A_list)
A_max = [0] * len(A_list)

B_list = list(B)
B_min = [0] * len(A_list)
B_max = [0] * len(A_list)


for i in range(len(A_list)):
    if A_list[i] == '5':
        A_max[i] = 1 * 10**(len(B_list) -1 - i)
for i in range(len(A_list)):
    if A_list[i] == '6':
        A_min[i] = -1 * 10**(len(B_list) -1 - i)

for i in range(len(B_list)):
    if B_list[i] == '5':
        B_max[i] = 1 * 10**(len(B_list) -1 - i)

for i in range(len(B_list)):
    if B_list[i] == '6':
        B_min[i] = -1 * 10 ** (len(B_list) - 1 - i)


A_max_num = sum(A_max) + int(A)
A_min_num = sum(A_min) + int(A)
B_max_num = sum(B_max) + int(B)
B_min_num = sum(B_min) + int(B)

print( A_min_num+B_min_num  , A_max_num+B_max_num )