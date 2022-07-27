A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

sum_A=0
sum_B=0

for i in range(10):
    if A_list[i] > B_list[i]:
        sum_A += 3
    elif A_list[i] == B_list[i]:
        sum_A += 1
        sum_B += 1
    else:
        sum_B += 3

A_list.reverse()
B_list.reverse()

print(sum_A,sum_B)

if sum_A>sum_B:
    print('A')

elif sum_A == sum_B:
    for i in range(10):
        if A_list[i] > B_list[i]:
            print('A')
            break
        elif A_list[i] < B_list[i]:
            print('B')
            break
    else:
        print('D')


else:
    print('B')