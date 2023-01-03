from collections import deque
import copy
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    k = 600000
    sum_total = sum(queue1)+sum(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    while queue1 and queue2 and k:
        
        k-=1

        if sum_total%2 == 1:
            return -1

        if sum_q1 > sum_q2:
            t = queue1.popleft()
            queue2.append(t)
            answer+=1
            sum_q1-=t
            sum_q2+=t

        elif sum_q1 < sum_q2:
            t = queue2.popleft()
            queue1.append(t)
            answer += 1
            sum_q2-=t
            sum_q1+=t

        else:
            return answer

    return -1
