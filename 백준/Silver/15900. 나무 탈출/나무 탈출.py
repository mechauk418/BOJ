import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
ans = 0

for i in range(N-1):
    a,b = map(int,input().split())

    tree[a].append(b)
    tree[b].append(a)


def dfs(x,depth):
    global ans
    visited[x]=1
    if len(tree[x])==1:
        ans+=depth
    for i in tree[x]:
        if visited[i]==0:
            dfs(i,depth+1)

dfs(1,0)

if (ans%2 == 0):
    print("No")
else:
    print('Yes')