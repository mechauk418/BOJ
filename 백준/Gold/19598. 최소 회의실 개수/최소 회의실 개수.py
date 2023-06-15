import heapq

N = int(input())

S = []

for i in range(N):
    start,end = map(int,input().split())

    S.append([start,end])


S.sort(key=lambda x:(x[0]))

time = 0
cnt = 1


b = [0]

for start ,end in S:
    if start >= b[0]:
        heapq.heappop(b)
    else:
        cnt+=1
    heapq.heappush(b, end)

print(cnt)