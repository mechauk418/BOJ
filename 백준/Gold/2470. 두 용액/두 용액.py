import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()
start = 0
end = n-1
minTake = sys.maxsize

while start < end:
    take = array[start] + array[end]
    if abs(take) < minTake:
        minTake = abs(take)
        result = [array[start], array[end]]
    if take < 0:
        start += 1
    elif take > 0:
        end -= 1
    else:
        break

print(result[0], result[1])