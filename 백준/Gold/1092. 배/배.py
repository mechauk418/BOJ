N = int(input())

Crane_list = list(map(int,input().split()))

M = int(input())

Box_list = list(map(int,input().split()))


Crane_list.sort(reverse=True)

Box_list.sort(reverse=True)

if Box_list[0]>Crane_list[0]:
    print(-1)

else:
    time = 0

    while Box_list:

        if not Box_list:
            break

        for i in Crane_list:

            for j in Box_list:

                if i>=j:
                    Box_list.remove(j)

                    break

        time+=1

    print(time)