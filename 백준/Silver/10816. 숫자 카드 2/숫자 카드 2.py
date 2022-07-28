import sys
from collections import Counter

N=int(sys.stdin.readline())
N_list = list(sys.stdin.readline().split())
M=int(sys.stdin.readline())
M_list=list(sys.stdin.readline().split())

counter_Nlist = Counter(N_list)

N_set=set(N_list)
M_set=set(M_list)

real_set=M_set & N_set
card_dict=dict()

for i in range(len(M_list)):
    if M_list[i] in real_set:
        card_dict[M_list[i]]= counter_Nlist[M_list[i]]
    else:
        card_dict[M_list[i]] = 0
    print(card_dict[M_list[i]], end=' ')
    card_dict.clear()
