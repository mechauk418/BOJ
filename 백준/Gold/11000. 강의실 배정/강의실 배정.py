import heapq

N = int(input())

L_list = []

for i in range(N):

    S,T = map(int,input().split())

    L_list.append([S,T])


L_list.sort()

room = []

heapq.heappush(room,L_list[0][1])

for i in range(1,N):
    if L_list[i][0] < room[0]:
        heapq.heappush(room,L_list[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,L_list[i][1])


print(len(room))