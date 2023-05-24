from bisect import bisect_left

N,M = map(int,input().split())

S = list(map(int,input().split()))

S.sort()
zeroidx = bisect_left(S,0)

S_minus = S[:zeroidx]
S_plus = S[zeroidx:]


ans  = 0
ans_list = []

for i in range(len(S_minus)):
    if i%M == 0:
        ans_list.append(abs(S_minus[i]))

S_plus.sort(reverse=True)

for i in range(len(S_plus)):
    if i%M == 0:
        ans_list.append(S_plus[i])


print(2*sum(ans_list) - max(ans_list))