from collections import deque

N = int(input())

N_list = list(map(int,input().split()))

visited = [0]*N



queue = deque([(0,N_list[0])])

while queue:

    pos, jump = queue.popleft()

    for i in range(1,jump+1):

        if pos + i >= N or visited[pos+i]:

            continue

        visited[pos+i] = visited[pos] + 1

        queue.append((pos+i,N_list[pos+i]))


if N==1:
    print(0)
else:
    print(visited[-1] if visited[-1] else -1)



