
T = int(input())

for t in range(1,T+1):


    N = int(input())

    for i in range(1,10):
        if N%i == 0:
            if i<10 and N//i < 10:
                print(f'#{t} Yes')
                break
    else:
        print(f'#{t} No')

