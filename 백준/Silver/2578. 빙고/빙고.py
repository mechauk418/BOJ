
graph = []
call_number = []

for i in range(5):
    S = list(map(int, input().split()))
    graph.append(S)

for i in range(5):
    K = list(map(int, input().split()))
    call_number.append(K)

call_list = []

for i in range(5):
    for j in range(5):
        call_list.append(call_number[i][j])

def check_bingo(number):

    cnt = 0

    for i in range(5):
        if number[i] == [0,0,0,0,0]:
            cnt += 1

        if [ number[0][i], number[1][i], number[2][i], number[3][i], number[4][i]] == [0,0,0,0,0]:
            cnt+=1

    if [ number[0][0], number[1][1], number[2][2], number[3][3], number[4][4]] == [0,0,0,0,0]:
        cnt+=1

    if [ number[0][4], number[1][3], number[2][2], number[3][1], number[4][0]] == [0,0,0,0,0]:
        cnt+=1

    return cnt

ans_list = []

for k in range(25):
    for i in range(5):
        for j in range(5):
            if call_list[k] == graph[i][j]:
                graph[i][j] = 0

    if check_bingo(graph) >= 3:
        ans_list.append(k)
        break




print(ans_list[0]+1)



