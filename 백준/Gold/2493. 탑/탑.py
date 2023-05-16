
N = int(input())

N_list = list(map(int,input().split()))

stack = []

ans = []

for i in range(N):
    while stack:

        if stack[-1][1] > N_list[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()

    if not stack:
        ans.append(0)
    stack.append([i,N_list[i]])

print(' '.join(map(str,ans)))
