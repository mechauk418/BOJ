from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    start = 0
    break_number = len(discount)-9
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    while True:
        s = discount[start:start+10]
        s_dict = defaultdict(int)
        for i in range(len(s)):
            s_dict[s[i]]+=1

        if want_dict==s_dict:
            answer +=1

        start+=1
        if start==break_number:
            break

    return answer