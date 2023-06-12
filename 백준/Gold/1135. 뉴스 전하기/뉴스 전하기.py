import sys
sys.setrecursionlimit(10**6)

N = int(input())

S = list(map(int,input().split()))

graph = [[] for _ in range(N)]
visited = [False] *(N)
dp = [0] *(N)

for i in range(N):
    if i==0:
        continue
    graph[i].append(S[i])
    graph[S[i]].append(i)


def dfs(x):
    visited[x]=True
    elem = []
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            elem.append(dp[i])
    if not elem:
        return
    elem.sort(reverse=True)
    max_num = 0
    for i in range(len(elem)):
        check = elem[i] + (i+1)
        if check>max_num:
            max_num=check
    
    dp[x] = max_num            

dfs(0)
print(max(dp))

# 아래 가지의 갯수 -1 만큼 더해준다.