from itertools import permutations

def solution(numbers):

    num_list = list(numbers)

    per_list = []

    for i in range(1,len(numbers)+1):
        per_list += list(permutations(num_list,i))

    num_list = [  int(''.join(i)) for i in per_list]

    num_list = list(set(num_list))

    if 0 in num_list:
        num_list.remove(0)
        
    if 1 in num_list:
        num_list.remove(1)


    ans_list = []
    for i in num_list:
        check = True

        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                check = False
                break
        if check:
            ans_list.append(i)

    answer = len(ans_list)
    return answer