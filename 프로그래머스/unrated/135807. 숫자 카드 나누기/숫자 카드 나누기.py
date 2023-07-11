import math

def gcd(array):
    ans = 0
    for i in range(len(array)):
        ans = math.gcd(ans,array[i])

    return ans


def solution(arrayA, arrayB):
    answer = 0

    gcdA = gcd(arrayA)
    gcdB = gcd(arrayB)

    if gcdA > gcdB:
        for i in arrayB:
            if i % gcdA == 0:
                answer = 0
                break
        else:

            answer = gcdA

    elif gcdB > gcdA:
        for i in arrayA:
            if i % gcdB == 0:
                answer = 0
                break

        else:
            answer = gcdB


    return answer