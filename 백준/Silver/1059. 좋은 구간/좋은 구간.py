
L = int(input())

S = list(map(int,input().split()))

n = int(input())

S.sort()

A = B = answer = 0

for i in range(len(S)):
    if n < S[i]:
        A = S[i - 1]
        B = S[i]
        break

if n < S[0]:
    for i in range(1, n + 1):
        for j in range(n, S[0]):
            if i == j:
                continue
            else:
                answer += 1

else:
    for i in range(A + 1, n + 1):
        for j in range(n, B):
            if i == j:
                continue
            answer += 1

print(answer)