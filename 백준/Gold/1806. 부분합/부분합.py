import sys

N,S = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split()))

sum_num = arr[0]

left, right = 0,0

ans = 10000000

while True:

    if sum_num < S:
        right +=1
        if right == N:
            break

        sum_num += arr[right]
    else:
        sum_num -= arr[left]
        ans = min(ans,right-left+1)
        left +=1

if ans != 10000000:
    print(ans)
else:
    print(0)