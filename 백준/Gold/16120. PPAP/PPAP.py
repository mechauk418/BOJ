import sys

S = sys.stdin.readline().rstrip()
if S == 'PPAP' or S == 'P':
    print('PPAP')
else:
    stack = []

    for i in S:
        stack.append(i)

        if ''.join(stack[-4:]) == 'PPAP':
            stack.pop()
            stack.pop()
            stack.pop()

    if ''.join(stack) == 'PPAP' or ''.join(stack) == 'P':
        print('PPAP')
    else:
        print('NP')

