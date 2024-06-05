from collections import deque

T = int(input())

for t in range(T):

    n,k = map(int,input().split())

    dlist = list(map(int,input().split()))

    graph = [[] for _ in range(n+1)]

    inDegree = [0 for _ in range(n+1)]

    DP = [0 for _ in range(n+1)]
    q = deque()

    for i in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
        inDegree[y]+=1

    w = int(input())

    for i in range(1,n+1):
        if inDegree[i]==0:
            q.append(i)
            DP[i]=dlist[i-1]

    while q:
        temt = q.popleft()

        for i in graph[temt]:
            inDegree[i]-=1
            DP[i] = max(DP[i],DP[temt]+dlist[i-1])
            if inDegree[i]==0:
                q.append(i)

    print(DP[w])

