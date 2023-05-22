import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = []

for i in range(N):
    A.append(int(input()))

A.sort()

left = 0
right = 0

ans = 9999999999

while left < N and right < N:
    temt = A[right] - A[left]
    if temt == M:
        ans=M
        break
    if temt<M:
        right +=1
        continue

    left+=1
    ans = min(ans,temt)

print(ans)

#  1 2 7 10 16 25