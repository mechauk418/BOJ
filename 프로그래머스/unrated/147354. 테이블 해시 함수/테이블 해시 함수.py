
def solution(data, col, row_begin, row_end):
    answer = 0
    # 정렬
    data = sorted(data, key = lambda x: [x[col - 1], -x[0]])

    for i in range(row_begin,row_end+1):
        sums = 0
        for j in data[i-1]:
            sums += (j % i)
        
        answer ^= sums

    return answer