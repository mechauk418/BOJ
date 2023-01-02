import copy
from itertools import permutations
import copy
def solution(k, dungeons):
    answer = ''

    dungeons_per = list(permutations(dungeons,len(dungeons)))

    max_cnt = 0

    for i in dungeons_per:
        cnt=0
        p = copy.deepcopy(k)
        for j in i:

            if p>=j[0]:
                p = p-j[1]
                cnt +=1

        if cnt >= max_cnt:
            max_cnt = cnt
            
    answer = max_cnt

    return answer

