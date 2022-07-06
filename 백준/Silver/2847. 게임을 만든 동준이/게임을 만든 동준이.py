import sys

N=int(sys.stdin.readline())
ans=0
S_list=[]
for i in range(N):
    S=int(sys.stdin.readline())
    S_list.append(S)

S_list.reverse()

for i in range(N-1):
    if S_list[i]<=S_list[i+1]:
        ans+= S_list[i+1] - (S_list[i]-1)
        S_list[i+1]=S_list[i]-1


print(ans)