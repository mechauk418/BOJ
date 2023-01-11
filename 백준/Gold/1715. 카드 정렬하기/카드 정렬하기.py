import heapq

N = int(input())

N_list = []

for i in range(N):

    N_list.append(int(input()))


heapq.heapify(N_list)


ans = 0

while True:

    if N==1:
        break

    elem1 = heapq.heappop(N_list)
    elem2 = heapq.heappop(N_list)

    sum_elem = elem1+elem2
    ans += sum_elem

    if not N_list:
        break

    heapq.heappush(N_list,sum_elem)


if N==1:
    print(0)
else:
    print(ans)

