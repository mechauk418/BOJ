n = int(input())

ans = 0
for i in range(n):
    inp = input()
    stack = []
    for j in inp:
        if len(stack) == 0:
                stack.append(j)
        else:
            if j == "A":           
                if stack[-1] == "B":
                    stack.append(j)
                elif stack[-1] == "A":
                    stack.pop()
            elif j == "B":
                if stack[-1] == "A":
                    stack.append(j)
                elif stack[-1] == "B":
                    stack.pop()
    if len(stack)==0:
        ans+=1

print(ans)