
A = input()
B = input()
C = input()

ans = 0
DP = [[ [0] * (len(C)+1) for _ in range(len(B)+1)] for _ in range(len(A)+1) ]


for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        for k in range(1,len(C)+1):

            if A[i-1] == B[j-1]==C[k-1]:
                DP[i][j][k]+=DP[i-1][j-1][k-1]+1
            else:
                DP[i][j][k]+=max(DP[i-1][j][k],DP[i][j-1][k],DP[i][j][k-1])

            ans = max(DP[i][j][k],ans)

print(ans)