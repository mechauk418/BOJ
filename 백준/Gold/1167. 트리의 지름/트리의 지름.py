
V = int(input())

graph = [[] for _ in range(V + 1)]


for i in range(V):
    temt = list(map(int,input().split()))

    N = temt[0]


    for j in range(1,len(temt),2):
        elem = temt[j:j+2]

        if elem==[-1]:
            break
        else:
            graph[N].append(elem)


distance = [-1] * (V + 1)
distance[1] = 0

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

dfs(1,0)


start = distance.index(max(distance))

distance = [-1] * (V + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))