import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())

def fact(n):

    result = 1

    for i in range(2,n+1):
        result = (result*i) % 1000000007

    return result


def col(n, k):
    if (k == 0):
        return 1

    if (k == 1):
        return n

    result = col(n, k // 2)
    if (k % 2 == 0):
        return result * result % 1000000007
    else:
        return result * result * n % 1000000007


top = fact(n)
bottom = fact(n - k) * fact(k) % 1000000007
answer = top * col(bottom, 1000000007 - 2) % 1000000007
print(answer)