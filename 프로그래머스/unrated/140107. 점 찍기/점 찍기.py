import math

def solution(k, d):
    cnt=0

    for i in range(0,d+1,k):
        y = math.floor(math.sqrt(d**2-i**2))
        cnt+=(y//k)+1


    return cnt
