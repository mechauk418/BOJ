import sys
from collections import Counter
N,M = map(int,sys.stdin.readline().split())

S_list = list(map(int,sys.stdin.readline().split()))


sum_list = [0]

temt = 0

for i in S_list:
    temt += i

    sum_list.append(temt%M)

sum_cnt = Counter(sum_list)

ans = 0
for i in range(M):
    ans += int((sum_cnt[i] * (sum_cnt[i]-1)) / 2)

print(ans)