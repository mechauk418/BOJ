def solution(plans):
    answer = []
    temt = []
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1].split(':')[0]) * 60 + int(plans[i][1].split(':')[1])
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x:(x[1]))

    while plans:

        if len(plans) >1:
            title1,start1,pt1 = plans[0]
            title2, start2, pt2 = plans[1]
            et1 = start1 + pt1
            et2 = start2 + pt2

            if et1 > start2:
                temt.append([et1 - start2, title1])
                plans.pop(0)
            else:
                answer.append(title1)
                plans.pop(0)
                diff = start2 - et1
                while temt:
                    if temt[-1][0] <= diff:  # 중단된 작업 다시 시작
                        diff -= temt[-1][0]
                        answer.append(temt.pop()[1])
                    else:
                        temt[-1][0] -= diff
                        break
        else:
            answer.append(plans.pop(0)[0])

    answer = answer + list(map(lambda x : x[1], temt[::-1]))

    return answer