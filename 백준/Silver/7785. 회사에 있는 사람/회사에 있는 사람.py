import sys

N=int(sys.stdin.readline())

ans_list=[]
ans_dict = {}

for i in range(N):
    name,status = map(str,sys.stdin.readline().split())

    ans_dict[name]=status


for i in ans_dict:
    if ans_dict[i] == 'enter':
        ans_list.append(i)

ans_list.sort(reverse=True)

for i in range(len(ans_list)):
    print(ans_list[i])
