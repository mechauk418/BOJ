

N,M = map(int,input().split())

A=[]
B=[]

for i in range(N):
    a = list(map(int,input()))
    A.append(a)

for i in range(N):
    b = list(map(int,input()))
    B.append(b)


cnt=0


if N>=3 and N>=3:

    for i in range(N-2):
        for j in range(M-2):
            if A[i][j]!=B[i][j]:
                A[i][j] = 1 - A[i][j]
                A[i+1][j] = 1 - A[i+1][j]
                A[i+2][j] = 1 - A[i+2][j]
                A[i][j+1] = 1 - A[i][j+1]
                A[i][j+2] = 1 - A[i][j+2]
                A[i+1][j+1] = 1 - A[i+1][j+1]
                A[i+1][j+2] = 1 - A[i+1][j+2]
                A[i+2][j+1] = 1 - A[i+2][j+1]
                A[i+2][j+2] = 1 - A[i+2][j+2]

                cnt+=1


if A==B:
    print(cnt)
else:
    print(-1)