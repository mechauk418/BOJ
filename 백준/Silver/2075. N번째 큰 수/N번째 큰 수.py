import sys, heapq
N = int(input())


heap = []

for i in range(N):

    input_num = list(map(int,input().split()))

    for j in input_num:

        if len(heap) < N:
            heapq.heappush(heap,j)

        else:

            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap,j)


print(heap[0])