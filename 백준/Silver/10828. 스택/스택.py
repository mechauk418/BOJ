import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):

    Command = sys.stdin.readline().rstrip()

    if Command == 'pop':
        if not stack:
            print(-1)
            continue
        print(stack.pop())


    elif Command == 'size':
        print(len(stack))
    elif Command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif Command == 'top':
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack[-1])

    elif 'push' in Command:
        push_num = Command.split()[1]
        stack.append( push_num )

