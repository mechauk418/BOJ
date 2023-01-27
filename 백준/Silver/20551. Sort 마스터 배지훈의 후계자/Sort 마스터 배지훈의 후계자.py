from bisect import bisect_left
import sys

N,M = map(int,sys.stdin.readline().split())

A = [ int(sys.stdin.readline()) for _ in range(N) ]

A.sort()

D = [ int(sys.stdin.readline()) for _ in range(M) ]


for i in D:

    ans = bisect_left(A,i)

    if ans >= N:
        print(-1)

    elif A[ans]==i:
        print(ans)
    else:
        print(-1)
