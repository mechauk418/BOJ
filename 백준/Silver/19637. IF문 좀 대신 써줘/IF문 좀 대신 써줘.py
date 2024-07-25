import sys
from bisect import bisect_left

n,m = map(int,input().split())

input = sys.stdin.readline

standard = []
score_list = []

for i in range(n):

    name, power = input().split()

    power = int(power)

    standard.append(name)
    score_list.append(power)


for i in range(m):

    score = int(input())

    idx = bisect_left(score_list,score)

    print(standard[idx])