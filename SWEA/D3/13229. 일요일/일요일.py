
T = int(input())

for t in range(1,T+1):
    S_list = ['SUN','MON','TUE','WED','THU','FRI','SAT','SUN_NEXT']

    S = input()

    for i in range(7):
        if S_list[i] == S:
            print(f'#{t} {7-i}')





