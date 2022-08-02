N=int(input())
S=[]
for i in range(N):
    S.append(int(input()))

S=sorted(S)

for i in range(N):
    print(S[i])