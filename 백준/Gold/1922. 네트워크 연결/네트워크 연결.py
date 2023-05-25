

N = int(input())

M = int(input())


S = []

parent = [0] * (N+1)

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

ans = 0

for i in range(1,N+1):
    parent[i]=i


for i in range(M):
    A,B,C = map(int,input().split())


    S.append( [A,B,C] )


S.sort(key=lambda x:(x[2]))


for i in S:
    a,b,cost = i
    if find(a) != find(b):
        union(a,b)
        ans += cost

print(ans)