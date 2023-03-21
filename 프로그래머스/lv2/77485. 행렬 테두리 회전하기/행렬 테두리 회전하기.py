def solution(rows, columns, queries):
    answer = []

    num_list = [ i for i in range(1,rows*columns+1)]
    graph = []
    for i in range(rows):
        graph.append(num_list[i*columns:(i+1)*columns])


    for q in queries:

        x1,y1,x2,y2 = q

        rev_list = []

        for i in range(y1,y2):

            rev_list.append((x1,i))

        for i in range(x1,x2):

            rev_list.append((i,y2))

        for i in range(y2,y1,-1):

            rev_list.append((x2,i))

        for i in range(x2,x1,-1):

            rev_list.append((i,y1))

        value_list = []
        for i in rev_list:
            value = graph[i[0]-1][i[1]-1]
            value_list.append(value)


        answer.append(min(value_list))

        elem = rev_list.pop(0)
        rev_list.append(elem)

        for i in range(len(rev_list)):
            graph[rev_list[i][0]-1][rev_list[i][1]-1] = value_list[i]


    return answer