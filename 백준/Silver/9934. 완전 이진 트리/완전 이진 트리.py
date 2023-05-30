
K = int(input())

bn = list(map(int,input().split()))

graph = []

for i in range(K):

    A = bn[::2]

    graph.append(A)

    bn = bn[1::2]


for i in range(K-1,-1,-1):

    print(*graph[i])