import sys
input=sys.stdin.readline
n=int(input())
d=[0]*20
tplist=[[0,0]]
for _ in range(n):
  t,p=map(int,input().split())
  tplist.append([t,p])

for i in range(1,n+1):
  x=tplist[i][0]-1
  d[i]=max(d[i-1],d[i])
  d[i+x] = max(d[i-1]+tplist[i][1],d[i+x])
  
print(d[n])