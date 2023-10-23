
def solution(N, number):
    if number == 1:
        return 1
    answer = -1

    DP = []

    for i in range(1,9):
        numbers = set()
        numbers.add(int(str(N)*i))

        for j in range(i-1):
            for a in DP[j]:
                for b in DP[-j-1]:
                    numbers.add(a+b)
                    numbers.add(a - b)
                    numbers.add(a * b)

                    if b != 0:
                        numbers.add(a/b)

        if number in numbers:
            return i

        DP.append(numbers)

    return answer


print(solution(5,12))