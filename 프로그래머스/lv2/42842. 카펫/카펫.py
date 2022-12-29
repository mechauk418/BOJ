def solution(brown, yellow):
    
    
    sq = brown + yellow # 전체 갯수
    
    sq_list = []
    
    for i in range(3,(sq//2)+1):
        if sq%i == 0:
            sq_list.append((i,int(sq/i)))
    
    for i in sq_list:
        if (i[0]-2) * (i[1]-2) == yellow:
            answer = [i[1],i[0]]
            break
    
    
    return answer