X = int(input())
N = int(input())

ab_list = []
sum_ab = 0
for i in range(N):

    a,b = map(int,input().split())
    sum_ab += a*b


if X == sum_ab:
    print('Yes')
else:
    print('No')



