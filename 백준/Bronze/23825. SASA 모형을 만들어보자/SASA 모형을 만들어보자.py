import sys

N,M=map(int,sys.stdin.readline().split())

ans = int(min(N,M)//2)

print(ans)