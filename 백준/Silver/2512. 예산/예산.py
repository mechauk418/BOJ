

N = int(input())


N_list = list(map(int,input().split()))

M = int(input())
ans = 0
start = 1
end = max(N_list)

while start <= end:

    mid = (start+end)//2

    sum_M = 0

    for i in N_list:

        if i > mid:
           sum_M += mid
        else:
            sum_M += i


    if M>=sum_M:
        ans = mid
        start = mid +1
    else:
        end = mid-1


print(ans)