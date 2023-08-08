def solution(elements):
    answer = 0
    sumlist = set()
    n = len(elements)
    elements = elements + elements[:-1]

    for i in range(1,n+1):
        for j in range(n):
            temt = elements[j:j+i]
            sumlist.add(sum(temt))
    answer = len(sumlist)
    return answer