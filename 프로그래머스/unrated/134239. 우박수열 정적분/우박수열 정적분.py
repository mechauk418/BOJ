
def solution(k, ranges):
    answer = []

    kroot = [k]

    checknum = k

    while checknum != 1:

        if checknum%2==0:
            checknum = checknum/2
        else:
            checknum=checknum*3 +1

        kroot.append(checknum)

    area = []
    for i in range(len(kroot)-1):
        area.append((kroot[i+1] + kroot[i])/2  )

    for i in ranges:
        if len(kroot)-1 + i[1] >= i[0]:
            answer.append(sum(area[i[0]:len(kroot)-1 + i[1]]))

        else:
            answer.append(-1)

    return answer