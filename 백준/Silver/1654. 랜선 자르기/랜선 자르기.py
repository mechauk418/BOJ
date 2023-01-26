K,N = map(int,input().split())


line = [ int(input()) for _ in range(K) ]

start = 1
end = max(line)

while start <= end:

    mid = (start + end)//2
    ans = 0

    for i in line:
        ans += i//mid

    if ans >= N:
        start = mid+1

    else:
        end = mid-1

print(end)



