from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
tree = defaultdict(list)
root = dict()

def dfs(start,end,visited,dis):
    if start == end:
        print(dis)
        return

    for i in tree[start]:
        if not visited[i]:
            visited[i]=True
            dis_list = [start,i]
            dis_list.sort()
            dis_list=tuple(dis_list)
            dis+=root[dis_list]
            dfs(i,end,visited,dis)
            visited[i]=False
            dis -= root[dis_list]

for i in range(N-1):
    A,B,R = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)
    elem = [A,B]
    elem.sort()
    elem = tuple(elem)
    root[elem]=R

for i in range(M):
    start,end = map(int,input().split())
    visited = [ False ] * (N+1)
    visited[start]=True
    dis=0
    dfs(start,end,visited,dis)
