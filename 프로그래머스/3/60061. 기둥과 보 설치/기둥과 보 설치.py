def check_build(answer):
    for x, y, a in answer:
        if a == 0:

            if (y != 0 and
                [x, y - 1, 0] not in answer and
                [x - 1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        else:

            if ([x, y - 1, 0] not in answer and
                [x + 1, y - 1, 0] not in answer and
                ([x - 1, y, 1] not in answer or
                 [x + 1, y, 1] not in answer)):
                return False
    return True
 
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not check_build(answer):
                answer.append([x, y, a])
        elif b == 1:
            answer.append([x, y , a])
            if not check_build(answer):
                answer.remove([x, y, a])
 
    answer.sort(key= lambda x : (x[0], x[1], x[2]))
    return answer