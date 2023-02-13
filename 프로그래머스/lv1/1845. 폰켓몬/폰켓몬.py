
def solution(nums):

    N = len(nums)

    nums_set = list(set(nums))

    if len(nums_set) <= (N/2):
        answer = len(nums_set)
    else:
        answer = int(N/2)


    return answer