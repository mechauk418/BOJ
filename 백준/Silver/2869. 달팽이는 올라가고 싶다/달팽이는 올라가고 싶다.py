import sys, math

A,B,V=map(int,sys.stdin.readline().split())


div = ((V-A) / (A-B))

ans = math.ceil(div)+1

print(ans)