
def solution(answers):
    list_1 = [1,2,3,4,5]*2000
    list_2 = [2,1,2,3,2,4,2,5]*1250
    list_3 = [3,3,1,1,2,2,4,4,5,5]*1000

    ans_len = len(answers)

    list_1_check = list_1[0:ans_len]
    list_2_check = list_2[0:ans_len]
    list_3_check = list_3[0:ans_len]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(ans_len):
        if list_1_check[i] == answers[i]:
            cnt1+=1
        if list_2_check[i] == answers[i]:
            cnt2+=1
        if list_3_check[i] == answers[i]:
            cnt3+=1

    cnt_list = [cnt1,cnt2,cnt3]

    max_cnt = max(cnt1,cnt2,cnt3)
    answer = []

    for i in range(3):
        if cnt_list[i]==max_cnt:
            answer.append(i+1)

    return answer
