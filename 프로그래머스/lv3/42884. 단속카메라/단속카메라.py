def solution(routes):
    answer = 0

    routes.sort(key=lambda x:(x[1]))

    max_num = -40000

    for i in routes:
        if max_num >= i[0]:
            continue
        else:
            answer+=1
            max_num = i[1]


    return answer