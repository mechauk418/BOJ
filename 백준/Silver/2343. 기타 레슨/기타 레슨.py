
N,M = map(int,input().split())

N_list = list(map(int,input().split()))

num = sum(N_list)

start = 0
end = 10000000

result = num

while start<=end:

    mid = (start+end)//2

    if mid<max(N_list):
        start = mid+1

        continue

    cnt=1
    tmp=0

    for i in range(len(N_list)):

        if tmp + N_list[i] <= mid:
            tmp += N_list[i]

        else:
            tmp = N_list[i]
            cnt+=1


    if cnt<=M:
        end = mid-1

        result = min(result,mid)

    else:
        start = mid+1

print(result)