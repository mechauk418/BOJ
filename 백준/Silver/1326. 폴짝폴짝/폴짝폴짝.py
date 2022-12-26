import sys
from collections import deque


def bfs():
    queue = deque([a - 1]) 
    visited = [-1] * 100000
    visited[a - 1] = 0 


    while queue:
        target = queue.popleft()


        for i in range(target, n, m[target]):
            if visited[i] == -1:
                queue.append(i) 
                visited[i] = visited[target] + 1 

                if i == b - 1:
                    return visited[i]

        for i in range(target, -1, -m[target]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[target] + 1
                if i == b - 1:
                    return visited[i]

    return -1


n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())
print(bfs())