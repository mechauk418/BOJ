
def danzo(number):
    number_string = str(number)
    for k in range(len(number_string) - 1):
        if number_string[k] > number_string[k+1]:
            return False
        
    return True


T = int(input())

for t in range(1,T+1):
    max_num = 0
    N = int(input())

    N_list = list(map(int,input().split()))

    for i in range(N-1):
        for j in range(i+1,N):
            num = N_list[i] * N_list[j]
            if danzo(num):
                max_num = max(max_num,num)

    if max_num == 0:
        max_num = -1

    print(f'#{t} {max_num}')
