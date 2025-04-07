import heapq

t = int(input())

for _ in range(t):

    ans = 0

    k = int(input())

    num_list = list(map(int,input().split()))

    heapq.heapify(num_list)

    while True:

        num1 = heapq.heappop(num_list)
        num2 = heapq.heappop(num_list)

        num3 = num1+num2

        ans+=num3

        heapq.heappush(num_list,num3)

        if len(num_list)==2:
            break


    ans+=num_list[0]+num_list[1]

    print(ans)
