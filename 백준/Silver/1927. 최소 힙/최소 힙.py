import heapq
import sys

input = sys.stdin.readline
N = int(input())

arr = []
heapq.heapify(arr)
for i in range(N):
    x=int(input())
    if x > 0:
        heapq.heappush(arr,x)
    elif x==0:
        if arr:
            result = heapq.heappop(arr)
            print(result)
        else:
            print(0)
