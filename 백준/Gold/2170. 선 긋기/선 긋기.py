import sys

N = int(sys.stdin.readline())

input_list = []

line = []

for i in range(N):

    a,b = map(int,sys.stdin.readline().split())

    input_list.append((a,b))

input_list.sort()

start = input_list[0][0]
end = input_list[0][1]
ans = 0
for i in input_list:

    if i==(start,end):
        continue

    if end>=i[1]:
        continue

    elif i[0]<=end<i[1]:

        end = i[1]

    elif i[0] > end:
        ans+= end-start

        start= i[0]
        end=i[1]


ans += end-start

print(ans)