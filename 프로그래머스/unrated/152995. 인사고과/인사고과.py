
def solution(scores):
    answer = 1

    oneho = scores[0]
    oneho_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    threshold = 0

    for score in scores:
        if oneho[0] < score[0] and oneho[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if oneho_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
            
    return answer