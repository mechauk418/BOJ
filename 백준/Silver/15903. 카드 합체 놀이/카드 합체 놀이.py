import heapq

N,M = map(int,input().split())

N_list = list(map(int,input().split()))

heapq.heapify(N_list)

for i in range(M):


    A = heapq.heappop(N_list)
    B = heapq.heappop(N_list)

    heapq.heappush(N_list,A+B)
    heapq.heappush(N_list, A + B)


print(sum(N_list))