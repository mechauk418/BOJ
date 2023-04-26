
def list_div(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

def solution(picks, minerals):
    answer = 0
    sum_gok = sum(picks)

    if len(minerals) > sum_gok * 5:
        minerals = minerals[:sum_gok*5]

    min_5 = list_div(minerals,5)
    mine_list = []
    for i in min_5:
        sum_ = 0
        for j in i:
            if j=='stone':
                sum_ += 1
            elif j=='iron':
                sum_ += 5
            else:
                sum_ +=25

        mine_list.append([i,sum_])

    mine_list.sort(key=lambda x:(-x[1]))

    dia,ir,st = picks

    while dia > 0:
        if mine_list:
            elem = mine_list.pop(0)
            for i in elem[0]:
                answer +=1
        dia -=1

    while ir > 0:
        if mine_list:
            elem = mine_list.pop(0)
            for i in elem[0]:
                if i == 'diamond':
                    answer += 5
                else:
                    answer +=1

        ir -= 1

    while st > 0:
        if mine_list:
            elem = mine_list.pop(0)
            for i in elem[0]:
                if i == 'diamond':
                    answer += 25
                elif i == 'iron':
                    answer +=5
                else:
                    answer +=1
        st -= 1


    return answer