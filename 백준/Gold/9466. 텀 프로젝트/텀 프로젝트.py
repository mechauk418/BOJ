import sys
sys.setrecursionlimit(10**6)

T = int(input())

for t in range(T):


    N = int(input())
    fir = [ i for i in range(1,N+1) ]
    sec = list(map(int,input().split()))

    ans_list = []

    def dfs(x,visited):

        global ans_list

        visited[x-1] = True

        route.append(x)

        if visited[sec[x-1]-1]:
            if sec[x-1] in route:
                ans_list += route[ route.index(sec[x-1]) : ]

            return

        else:
            dfs(sec[x-1],visited)

    visited = [False]*N

    for i in range(1,N+1):
        if not visited[i-1]:
            route=[]
            dfs(i,visited)

    print(N-len(ans_list))

