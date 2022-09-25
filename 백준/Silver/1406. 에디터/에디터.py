import sys
from collections import deque

S = sys.stdin.readline().rstrip()

stack = deque(S)
stack_right = []
stack_right = deque(stack_right)

N = int(sys.stdin.readline())

for i in range(N):

    S = sys.stdin.readline().rstrip().split()


    if S[0] == 'P':
        stack.append(S[1])

    elif S[0] == 'L':
        if not stack:
            continue
        L = stack.pop()
        stack_right.appendleft(L)

    elif S[0] == 'D':
        if not stack_right:
            continue
        D = stack_right.popleft()
        stack.append(D)

    elif S[0] == 'B':
        if not stack:
            continue
        else:
            stack.pop()


print(''.join(stack) + ''.join(stack_right))