import sys

N,L=map(int,sys.stdin.readline().split())
S=list(map(int,sys.stdin.readline().split()))
S.sort()
S_minus=[]
count=1

for i in range(N-1):
    S_minus.append(S[i+1]-S[i])

sm=0
for i in range(len(S_minus)):
    sm+=S_minus[i]
    if sm<L:
        continue
    elif sm == S_minus[i] and S_minus[i]>=L:
        count+=1
        sm=0
    else:
        count+=1
        sm=0

else:
    print(count)
