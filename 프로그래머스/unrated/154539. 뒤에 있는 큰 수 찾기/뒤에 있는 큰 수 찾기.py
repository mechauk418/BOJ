def solution(numbers):

    q = []

    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while q and numbers[q[-1]] < numbers[i]:
            answer[q.pop()] = numbers[i]
        q.append(i)

    return answer