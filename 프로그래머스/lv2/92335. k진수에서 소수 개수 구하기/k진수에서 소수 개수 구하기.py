def sosu(n):

    check = [ i for i in range(2, int(n**0.5)+1)]

    for i in check:
        if n%i==0:
            return False

    return True


def solution(n, k):
    result = ''
    while True:
        remain = n%k
        n = n//k
        result+=str(remain)
        if n<k:
            result+=str(n)
            break

    result = result[::-1]

    check_num_list = result.split('0')
    real_list = []
    for check in check_num_list:
        if len(check):
            real_list.append(int(check))

    answer = 0
    for num in real_list:
        if sosu(num) and num !=1:
            answer+=1

    return answer