from collections import deque



def solution(progresses, speeds):
    day_list = []
    ans_list = []
    k=0
    for i in progresses:
        p_num = ((100 - i) % speeds[k])
        if p_num == 0:
            day = ((100 - i) // speeds[k])
        else:
            day = ((100 - i) // speeds[k])+1
        day_list.append( day )
        k+=1

    day_dq = deque(day_list)

    check_list = []

    while True:
        check_num = day_dq.popleft()

        # 5 10 1 1 20 1

        if len(check_list) == 0:
            check_list.append(check_num)
            continue

        if check_num > check_list[0]:
            ans_list.append(len(check_list))
            check_list = [check_num]
        else:
            check_list.append(check_num)

        if len(day_dq) == 0:
            ans_list.append(len(check_list))
            break

    return ans_list



