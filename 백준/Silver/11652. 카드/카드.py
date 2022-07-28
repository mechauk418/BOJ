import sys,collections

N=int(sys.stdin.readline())
num_dict={}
for i in range(N):
    Num=int(sys.stdin.readline())
    if not Num in num_dict:
        num_dict[Num]=1
    else:
        num_dict[Num]+=1




ans = list(num_dict.items())
ans_sort = sorted(ans, key=lambda x:(x[1],-x[0]))

print(ans_sort[-1][0])