def check_str(string):
    if len(string)==1:
        return True

    left = string[: len(string) // 2]
    right = string[ (len(string) // 2)+1:]

    if len(string)==3:
        if string == '000':
            return True
        elif string[1] == '1':
            return True
        else:
            return False

    if string[len(string)//2] == '1':
        if check_str(left) and check_str(right):
            return True
        else:
            return False

    if string[len(string)//2] == '0':
        if '1' not in left and '1' not in right:
            return True

def ischeck(n):
    return (n & (n-1)) ==0

def solution(numbers):
    answer = []

    for i in numbers:
        bin_num = bin(i)[2:]
        while not ischeck(len(bin_num)+1):
            bin_num = '0' + bin_num

        if check_str(bin_num):
            answer.append(1)
        else:
            answer.append(0)

    return answer
