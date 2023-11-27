import heapq
import sys

input = sys.stdin.readline
n = int(input())

left = []
right = []

for i in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        leftValue = heapq.heappop(left)
        rightValue = heapq.heappop(right)

        heapq.heappush(left, -rightValue)
        heapq.heappush(right, -leftValue)

    print(-left[0])