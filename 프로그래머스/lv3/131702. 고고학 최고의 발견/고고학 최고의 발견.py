from copy import deepcopy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def rotate(x, y, lst, rt) :
    length = len(lst)
    for k in range(5) :
        ax, ay = x + dx[k], y + dy[k]
        if -1 < ax < length and -1 < ay < length :
            lst[ay][ax] = ( lst[ay][ax] + rt ) % 4

def solution(clockHands):
    answer = float('inf')
    length = len(clockHands)
    
    for i in range(4 ** length) :
        tmp = 0
        tmp_clock = deepcopy(clockHands)
        for j in range(length) :
            rt = i % 4 ** ( j + 1 ) // 4 ** j
            if rt == 0 :
                continue
                
            rotate(j, 0, tmp_clock, rt)
            tmp += rt
        
        for y in range(1, length) :
            for x in range(length) :
                if tmp_clock[y-1][x] == 0 :
                    continue
                rt = 4 - tmp_clock[y-1][x]
                rotate(x, y, tmp_clock, rt)
                tmp += rt
        if sum(tmp_clock[-1]) == 0 : 
            answer = min(answer, tmp)
        
    return answer