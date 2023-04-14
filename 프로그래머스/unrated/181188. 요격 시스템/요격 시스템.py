
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1]))

    max_num = -400000

    for i in targets:
        if max_num > i[0]:
            continue
        else:
            answer +=1
            max_num = i[1]-0.5


    return answer