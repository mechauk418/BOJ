def solution(sequence, k):
    sum_ = 0
    right = 0
    result = []
    for left in range(len(sequence)):
        while right < len(sequence) and sum_ < k:
            sum_ += sequence[right]
            right += 1

        if sum_ == k:
            if not result:
                result = [left, right - 1]
            else:
                result = result if result[1] - result[0] <= (right - 1) - left else [left, right - 1]

        sum_ -= sequence[left]

    return result