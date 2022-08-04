S = [[ 0 for i in range(100)] for _ in range(100)]

cnt = 0

for i in range(4):
    a,b,c,d = map(int,input().split())

    for j in range(b,d):
        for k in range(a,c):
            if S[j-1][k-1]==0:
                S[j-1][k-1] = 1


for i in range(100):
    for j in range(100):
        if S[i][j]==1:
            cnt+=1

print(cnt)
