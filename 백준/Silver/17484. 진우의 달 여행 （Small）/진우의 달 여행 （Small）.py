

route = [ -1,0,1 ]


n,m=map(int,input().split())

graph = [  list(map(int,input().split())) for _ in range(n)  ]


ans = 9999999999

def dfs(a,b,total,front):
    global ans
    total += graph[a][b]
    if a==(n-1):
        if ans>total:
            ans=total
        return

    for i in route:
        if i==front:
            continue

        if 0<=b+i<m:
            dfs(a+1,b+i,total,i)
        else:
            continue

for i in range(m):
    dfs(0,i,0,3)

print(ans)
