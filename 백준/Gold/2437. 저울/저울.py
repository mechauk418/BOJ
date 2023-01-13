import sys

N = int(input())

N_list = list(map(int,sys.stdin.readline().split()))

N_list.sort()


start = 1

while True:

    if N==1 or N_list[0] != 1 :
        print(1)
        break


    check_num = sum ( N_list[:start] )+1

    if check_num < N_list[start]:
        print(check_num)
        break

    start +=1

    if start == len(N_list):
        print(sum(N_list)+1)
        break

