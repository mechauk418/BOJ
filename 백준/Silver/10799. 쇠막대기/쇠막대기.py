
S = input()

stack = []

cnt = 0

S = S.replace( '()', '5' )

for i in S:
    if i == '(':
        stack.append(i)

    elif i == '5':
        cnt += len(stack)

    elif i == ')':
        cnt += 1
        stack.pop()

print(cnt)

