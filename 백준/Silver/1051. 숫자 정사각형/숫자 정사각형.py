
N,M = map(int,input().split())

limit_length = min(N,M) # 3

graph = [ list(map(int,input())) for _ in range(N) ]

i_list = []

# 1 2
for i in range(1,limit_length):

    input_graph = [ [0 for i in range(M-i) ] for _ in range(N-i) ]

    for j in range(N-i):
        for k in range(M-i):
            input_graph[j][k] = graph[j][k]


    for j in range(N-i):
        for k in range(M-i):
            if input_graph[j][k] == graph[j+i][k] == graph[j][k+i] == graph[j+i][k+i]:
                i_list.append(i)



if i_list:

    print( (max(i_list)+1)**2 )

else:
    print(1)