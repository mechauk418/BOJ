import sys
from itertools import permutations

K = int(input())

num_list = list(permutations([1,2,3,4,5,6,7,8,9],3))
ans_list = []

for _ in range(K):

    N,s,b = map(int,input().split())

    N = list(str(N))

    remove_cnt = 0

    for i in range(len(num_list)):

        s_cnt = b_cnt = 0

        i -= remove_cnt

        for j in range(3):

            N[j] = int(N[j])

            if N[j] in num_list[i]:
                if j == num_list[i].index(N[j]):

                    s_cnt += 1
                else:
                    b_cnt += 1


        if s_cnt != s or b_cnt != b:
            num_list.remove(num_list[i])
            remove_cnt+=1


print(len(num_list))