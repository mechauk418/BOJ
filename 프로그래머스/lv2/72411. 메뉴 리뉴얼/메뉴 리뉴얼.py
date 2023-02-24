from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:

        com = []

        for ord in orders:
            ord = sorted(ord)
            if len(ord) >= num:
                com+=list(combinations(ord,num))

        com = list(set(com))

        max_count = 0
        temt = []
        for c in com:

            count = 0
            for o in orders:
                check = True
                for i in range(num):
                    if c[i] not in o:
                        check = False
                if check:
                    count+=1

            if count>=2:
                if count >= max_count:
                    max_count = count
                    temt.append((c,count))

        temt.sort(key=lambda x:(-x[1]))

        for t in temt:
            if t[1]==temt[0][1]:
                answer.append(''.join(t[0]))
    answer.sort()
    return answer