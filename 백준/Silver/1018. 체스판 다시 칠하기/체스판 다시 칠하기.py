
N,M = map(int,input().split())

c_list = [ list(input()) for _ in range(N) ]


def chess(c_list):

    check1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    check2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

    max_cnt1 = 999
    max_cnt2 = 999

    for i in range(N-7):
        for j in range(M-7):
            check1_cnt = 0
            check2_cnt = 0
            check_list =  [ row[j:j+8] for row in c_list[i:i+8]  ]


            for a in range(8):
                for b in range(8):
                    if check_list[a][b] != check1[a][b]:
                        check1_cnt+=1
                    if check_list[a][b] != check2[a][b]:
                        check2_cnt+=1


            if check1_cnt <= max_cnt1:
                max_cnt1 = check1_cnt

            if check2_cnt <= max_cnt2:
                max_cnt2 = check2_cnt


    print(min(max_cnt1,max_cnt2))



chess(c_list)