from collections import deque

t = int(input())

for i in range(t):

    n,m = map(int,input().split())

    n_list = list(map(int,input().split()))

    index_list = []
    ans_list = []

    for i in range(len(n_list)):

        index_list.append((n_list[i],i))


    q = deque(index_list)
    q2 = deque(n_list)

    while len(q)>1:

        elem = q.popleft()
        elem2 = q2.popleft()

        if elem2 < max(q2):
            q2.append(elem2)
            q.append(elem)

        else:
            ans_list.append(elem)

    ans_list += q


    for i in range(n):

        if ans_list[i][1] == m:

            print(i+1)

