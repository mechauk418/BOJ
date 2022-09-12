R,C = map(int,input().split())

graph = []

for i in range(R):

    graph.append(list(input()))

ans = 0
route = set()

def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)

    if x<0 or x>= R or y<0 or y>=C:
        return False

    if graph[x][y] not in route:
        route.add(graph[x][y])

        dfs(x, y + 1, cnt + 1)
        dfs(x, y - 1, cnt + 1)
        dfs(x+1, y,cnt+1)
        dfs(x-1, y,cnt+1)
        
        route.remove(graph[x][y])


dfs(0,0,0)

print(ans)