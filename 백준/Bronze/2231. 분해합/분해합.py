import sys
N=int(sys.stdin.readline())

ans = 0
S=0
for k in range(1,N):
    S = k + sum (map(int,list(str(k)) ) )
    if S==N:
        ans = k
        break

if S==N:
    print(ans)
else:
    print(0)