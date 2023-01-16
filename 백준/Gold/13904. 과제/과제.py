import heapq

N = int(input())

S_list = []

for i in range(N):

    D,W = map(int,input().split())

    S_list.append((W,D))

heapq.heapify(S_list)

max_S_list = []

for i in S_list:

    heapq.heappush( max_S_list, ( -i[0] ,i[0],i[1] ) )

sum = 0

for i in range(N,0,-1):
    recycle = []
    while max_S_list:

        elem = heapq.heappop(max_S_list)

        if elem[2] >= i:
            sum += elem[1]
            max_S_list += recycle
            heapq.heapify(max_S_list)
            break

        else:
            recycle.append(elem)

        if not max_S_list:
            max_S_list = recycle
            break

print(sum)