def solution(sizes):

    max_len = []
    min_len = []

    for i in range(len(sizes)):

        sizes[i] = [ max(sizes[i][0],sizes[i][1]), min(sizes[i][0],sizes[i][1])  ]
        max_len.append(sizes[i][0] )
        min_len.append(sizes[i][1])

    max_num = max(max_len)
    max_num2 = max(min_len)


    answer = max_num*max_num2

    return answer
