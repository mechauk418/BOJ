import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

idx = 0
while True:
    idx += 1
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    parents = [i for i in range(n+1)]
    cycle = set()
    for _ in range(m):
        a,b = map(int,input().split())
        if find(a) == find(b):
            cycle.add(parents[a])
            cycle.add(parents[b])
        # 두 정점 중 하나가 사이클에 포함되는 정점이라면 나머지 정점도 사이클로 포함한다.
        if parents[a] in cycle or parents[b] in cycle: 
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a,b)
    
    # find 함수를 쭉 돌려서 각 정점의 parents를 갱신한다.
    for i in range(n+1):
        find(i)
    
    parents = set(parents)
    ans = sum([1 if i not in cycle else 0 for i in parents])-1
    if ans == 0:
        print('Case %d: No trees.' %idx)
    elif ans == 1:
        print('Case %d: There is one tree.' %idx)
    else:
        print('Case %d: A forest of %d trees.' %(idx,ans))