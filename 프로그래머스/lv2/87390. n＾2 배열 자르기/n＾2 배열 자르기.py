def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n
        b = i%n
        if a<b: a,b =b,a
        answer.append(a+1)
    
    return answer