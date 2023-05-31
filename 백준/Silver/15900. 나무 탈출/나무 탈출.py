import sys
sys.setrecursionlimit(10**5)
N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
ans = 0
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dep(a):
    visit[a] = 1
    for i in tree[a]:
        if visit[i] == 0:
            depth[i] = depth[a] + 1
            dep(i)

dep(1)
for i in range(2,N+1):
    if len(tree[i]) == 1:   # 리프노드이면
        ans += depth[i]

if (ans % 2 == 0):  # 짝수
    print("No")
else:	# 홀수
    print("Yes")