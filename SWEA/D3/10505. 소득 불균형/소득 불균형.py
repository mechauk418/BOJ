T = int(input())

for i in range(T):
    N = int(input())
    income_list = list(map(int,input().split()))
    income_avg = sum(income_list) / len(income_list)
    ans = len([ i for i in income_list if i <= income_avg  ])
    print(f'#{i+1} {ans}' )

