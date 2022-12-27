import sys

input = sys.stdin.readline
N, M = map(int, input().split())
relation = [[] for i in range(N)]
stack = []
result = [0 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[b - 1].append(a - 1)

for i in range(N):
    visited = [False] * N
    stack.append(i)
    visited[i] = True

    # dfs
    while stack:
        value = stack.pop()
        result[i] += 1

        length = len(relation[value])
        for j in range(length):
            if not visited[relation[value][j]]:
                stack.append(relation[value][j])
                visited[relation[value][j]] = True

answer = []
max_value = max(result)
for i in range(N):
    if result[i] == max_value:
        print(i + 1, end=" ")