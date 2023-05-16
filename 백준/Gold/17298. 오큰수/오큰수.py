
N = int(input())

N_list = list(map(int,input().split()))

N_list = N_list[::-1]

stack = []

ans = []

for i in range(N):
    while stack:

        if stack[-1] > N_list[i]:
            ans.append(stack[-1])
            break
        else:
            stack.pop()

    if not stack:
        ans.append(-1)
    stack.append(N_list[i])

ans = ans[::-1]

print(' '.join(map(str,ans)))
