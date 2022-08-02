import heapq
import sys

N = int(sys.stdin.readline())

abs_heap = []

for i in range(N):
    x = int(sys.stdin.readline())


    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if len(abs_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])



