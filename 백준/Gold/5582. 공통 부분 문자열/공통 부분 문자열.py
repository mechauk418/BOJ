import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()


N = len(A)
M = len(B)

ans = 0

DP = [ [0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):

        if A[i-1] == B[j-1]:
            DP[i][j]+=DP[i-1][j-1]+1
            ans = max(DP[i][j],ans)

print(ans)