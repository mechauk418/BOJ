
N = int(input())
S_list = list(map(int,input().split()))

P = int(input())

P_list = []

for i in range(P):

    G,S = map(int,input().split())
    P_list.append((G,S))


for i in P_list:

    if i[0] == 1:
        for j in range(1,(N//i[1])+1):
            idx = i[1]*j # 3 6
            S_list[idx-1]=1-S_list[idx-1]

    else:
        rng = min(i[1]-1,N-i[1]) # 3
        S_list[i[1] - 1] = 1 - S_list[i[1] - 1]
        for k in range(1,rng+1):
            if S_list[i[1]-1-k]==S_list[i[1]-1+k]:
                S_list[i[1] - 1 - k] = 1-S_list[i[1]-1-k]
                S_list[i[1] - 1 + k] = 1-S_list[i[1]-1+k]
            else:
                break


cnt = 0
for i in S_list:
    print(i, end=' ')
    
    cnt+=1
    if cnt==20:
        print()
        cnt=0

