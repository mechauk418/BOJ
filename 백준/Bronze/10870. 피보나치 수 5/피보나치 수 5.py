

n = int(input())


def fibo(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n > 1:

        return fibo(n-2)+fibo(n-1)


print(fibo(n))