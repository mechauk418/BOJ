N = int(input())

S = list(map(int, input().split()))

DP = [1 for i in range(N)]
DP[0] = 1

for i in range(1, N):
    for j in range(i):

        if S[i] > S[j]:
            DP[i] = max(DP[i], DP[j] + 1)

ans = max(DP)
ans_list = []

print(max(DP))


while True:

    index = DP.pop()
    value = S.pop()

    if index == ans:
        ans_list.append(value)
        ans -= 1

    if ans == 0:
        break

print(*ans_list[::-1])
