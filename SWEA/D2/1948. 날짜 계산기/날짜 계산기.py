

T = int(input())
for t in range(1,T+1):

    mon_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]


    a_month,a_day,b_month,b_day = map(int,input().split())

    a_date = sum ( mon_day[0:a_month] ) + a_day
    b_date = sum ( mon_day[0:b_month] ) + b_day

    ans = b_date - a_date +1


    print(f'#{t} {ans}'  )