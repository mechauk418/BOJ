import sys
input = sys.stdin.readline

n, x = map(int, input().split())
if (not (1 <= x <= n <= 250000)):
    exit()
li = list(map(int, input().split()))

if max(li) == 0:
    print("SAD")
else:
    li_num = sum(li[0:x])
    value = li_num
    cnt = 1
    for i in range(x, n):
        value -= li[i-x]
        value += li[i]
        if value > li_num:
            li_num = value
            cnt = 1
        elif value == li_num:
            cnt += 1
    print(li_num)
    print(cnt)