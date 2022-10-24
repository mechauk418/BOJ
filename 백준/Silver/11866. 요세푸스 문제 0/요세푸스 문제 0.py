from collections import deque

N,K = map(int,input().split())


num_list = [ i for i in range(1,N+1)]


num_list = deque(num_list)

ans_list = []



while num_list:

    for i in range(K-1):

        k = num_list.popleft()
        num_list.append(k)

    ans = num_list.popleft()
    ans_list.append(ans)

print('<',end='')

for i in ans_list:
    print(i, end='')
    if i != ans_list[len(ans_list)-1]:

        print(',', end=' ')
print('>',end='')
