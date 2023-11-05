from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
cb = deque(list(map(int, sys.stdin.readline().split())))
robot = deque([0] * n)
res = 0

while True:
    cb.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and cb[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                cb[i + 1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and cb[0] >= 1:
        robot[0] = 1
        cb[0] -= 1
    res += 1
    if cb.count(0) >= k:
        break

print(res)