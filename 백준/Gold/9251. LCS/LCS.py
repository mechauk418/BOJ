
S1 = input().strip().upper()

S2 = input().strip().upper()

len1 = len(S1)
len2 = len(S2)


DP = [[0]*(len2 +1) for _ in range(len1+1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[-1][-1])