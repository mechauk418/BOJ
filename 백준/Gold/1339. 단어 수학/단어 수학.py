
N = int(input())

W_list = []
A_list = []

for i in range(N):

    W = input()
    W_list.append(W)
    M = list(W)

    for j in M:
        A_list.append(j)

A_list = list(set(A_list))
A_dict = dict.fromkeys(A_list,0)

for i in W_list:
    K = len(i)

    for j in range(len(i)):
        A_dict[i[j]] += 10**(K-j-1)


A_dict = list(A_dict.items())


A_dict.sort(key = lambda x:(-x[1]))

ans = 0
max_num = 9

for i in A_dict:

    ans += i[1]*max_num

    max_num -= 1

print(ans)