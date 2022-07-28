import sys, collections

N=int(input())
S_list=[]
for i in range(N):
    S=sys.stdin.readline().rstrip()
    S_list.append(S)

ans_dict = collections.Counter(S_list)

max_num = max(list(ans_dict.values()))


ans_list = list(ans_dict.items())

ans_list = list(map(list,ans_list))
ans_eng=[]
for i in range(len(ans_list)):
    if ans_list[i][1] == max_num:
        ans_eng.append(ans_list[i][0])

ans_eng.sort()

print(ans_eng[0])