
N = int(input())

S = []

for i in range(N):
    S.append(float(input()))

for i in range(1,N):
    S[i] = max(S[i],S[i]*S[i-1])

ans = max(S)

print('%0.3f'%ans)