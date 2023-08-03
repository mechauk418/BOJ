from collections import defaultdict

def solution(topping):
    answer = 0

    chul = defaultdict(int)
    brother = set()

    for i in topping:
        chul[i]+=1

    for i in topping:
        brother.add(i)
        chul[i] -=1
        if chul[i]==0:
            del chul[i]
        if len(brother) == len(chul):
            answer +=1

    print(answer)

    return answer