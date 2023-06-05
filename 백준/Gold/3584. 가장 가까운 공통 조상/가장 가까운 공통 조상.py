import sys
sys.setrecursionlimit(10**6)

T = int(input())

for t in range(T):


    N = int(input())

    graph = [ [] for _ in range(N+1) ]

    for i in range(N-1):
        A,B = map(int,input().split())

        graph[B].append(A)



    check1,check2 = map(int,input().split())

    def dfs(x,root):

        if graph[x]:

            root.append(graph[x][0])

            dfs(graph[x][0],root)

    root1=[check1]
    root2=[check2]

    dfs(check1,root1)

    dfs(check2,root2)

    while True:

        if not root1 or not root2:
            print(temt)
            break

        elem1 = root1.pop()
        elem2 = root2.pop()

        if elem1==elem2:
            temt = elem1
            continue
        else:
            print(temt)
            break
