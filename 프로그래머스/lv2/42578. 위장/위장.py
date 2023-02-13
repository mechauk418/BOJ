import math

def solution(clothes):
    answer = 0

    clothes_dict = dict()

    for i in clothes:
        if i[1] not in clothes_dict:
            clothes_dict[i[1]] = 1
        else:
            clothes_dict[i[1]] +=1

    type = list(clothes_dict.values())
    ans_list = []
    for i in type:
        ans_list.append(i+1)
        
    answer = math.prod(ans_list) -1


    return answer