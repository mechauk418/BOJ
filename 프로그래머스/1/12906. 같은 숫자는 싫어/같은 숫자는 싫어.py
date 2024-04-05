
def solution(arr):
    answer = [arr[0]]

    for i in arr:

        if answer[-1] != i:
            answer.append(i)

    return answer


print(solution([1,1,3,3,0,1,1]))