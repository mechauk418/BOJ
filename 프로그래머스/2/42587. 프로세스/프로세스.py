from collections import deque
def solution(priorities, location):
    pri_dq = deque(priorities)
    while len(pri_dq) > 0:


        check_num = pri_dq.popleft()

        big_list = [ i for i in pri_dq if i>check_num ]

        if len(big_list) >0:
            pri_dq.append(check_num)
            location = location-1

        else:
            location = location+1



    ans = location +1

    return ans