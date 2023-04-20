def solution(sequence):
    sequence = [val * (-1 if idx % 2 else 1) for (idx, val) in enumerate(sequence)]

    for i in range(len(sequence) - 1):
        sequence[i + 1] += sequence[i]

    return max(abs(max(sequence)), abs(min(sequence)), max(sequence) - min(sequence))