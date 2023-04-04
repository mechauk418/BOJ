from itertools import combinations

N = int(input())

nums = list(map(int,input().split()))

N_list = [ i for i in range(1,N+1)]

case_list = []

for i in range(1,(N//2)+1):
    first = list(combinations(N_list,i))
    for j in first:
        last = list(set(N_list) - set(j))
        case_list.append( (list(j),last) )


graph = [ [] for _ in range(N+1)]

for i in range(1,N+1):

    temt = list(map(int,input().split()))

    adja = temt.pop(0)

    for j in temt:
        if i not in graph[j]:
            graph[j].append(i)
            graph[j].sort()
        if j not in graph[i]:
            graph[i].append(j)
            graph[i].sort()

# 123   456

def dfs(x,visited,elem):

    visited[x] = True
    for i in graph[x]:
        if not visited[i] and i in elem:
            dfs(i,visited,elem)

ans = 99999999

for case in case_list:

    first = case[0]
    last = case[1]

    visited_first = [ False for _ in range(N+1) ]
    visited_last = [False for _ in range(N + 1)]

    dfs(first[0],visited_first,first)
    dfs(last[0], visited_last, last)

    check = False

    for i in first:
        if not visited_first[i]:
            check = True

    for i in last:
        if not visited_last[i]:
            check = True

    if check:
        continue

    sum_first = 0
    sum_last = 0

    for i in first:
        sum_first += nums[i-1]

    for i in last:
        sum_last += nums[i-1]

    ans_check = abs(sum_first - sum_last)

    ans = min(ans,ans_check)


if ans == 99999999:
    print(-1)
else:
    print(ans)