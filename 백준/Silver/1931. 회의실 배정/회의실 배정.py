
N = int(input())

graph = []

for i in range(N):

    A = list(map(int,input().split()))

    graph.append(A)


graph.sort(key=lambda x:(x[1],x[0]))


cnt = 1
end_time = graph[0][1]

for i in range(1,N):

    if graph[i][0] >= end_time:
        cnt += 1
        end_time = graph[i][1]


print(cnt)