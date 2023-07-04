from collections import Counter

def solution(k, tangerine):

    A = dict(Counter(tangerine))
    B = list(A.values())
    B.sort()
    temt = 0
    cnt=0
    while True:
        C = B.pop()
        cnt+=1
        temt += C
        if temt >= k:
            break


    return cnt