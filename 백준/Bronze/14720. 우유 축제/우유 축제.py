import collections

N = int(input())

N_list = list(map(int,input().split()))

N_deque = collections.deque(N_list)

cnt = 0
check = 0
for i in range(N):

    milk_num = N_deque.popleft()
    if milk_num == check:
        cnt+=1
        check +=1
        if check == 3:
            check = 0

print(cnt)

