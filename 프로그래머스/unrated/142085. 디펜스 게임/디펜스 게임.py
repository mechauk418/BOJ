import heapq
from collections import deque
def solution(n, k, enemy):
    answer = 0
    score = 0
    score_cnt = 0
    if k>=len(enemy):
        return len(enemy)

    front = enemy[:k]
    back = enemy[k:]
    heapq.heapify(front)
    back = deque(back)
    while True:
        if not back:
            return len(enemy)
        elem = heapq.heappop(front)
        wave = back.popleft()
        if wave>=elem:
            score += elem
            heapq.heappush(front,wave)

        elif wave<elem:
            score+=wave
            heapq.heappush(front,elem)

        if score>n:
            break
        score_cnt+=1

    answer = score_cnt+k

    return answer