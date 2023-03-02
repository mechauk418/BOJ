from collections import deque

def trans(begin,after):
    count = 0
    for i in range(len(begin)):
        if begin[i]==after[i]:
            count+=1

    if count == len(begin)-1:
        return True
    else:
        return False

def solution(begin, target, words):

    if target not in words:
        return 0

    q = deque([(begin,0)])
    cnt = 0
    while q:
        now,cnt = q.popleft()
        if now == target:
            return cnt

        for i in words:
            if trans(now,i):
                q.append((i,cnt+1))

    answer = 0

    return answer