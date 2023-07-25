import math, sys
sys.setrecursionlimit(10**6)

N = int(input())

sosu = [i for i in range(1,10)]

ans_list = []

sosulist = []

def is_prime_number(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def dfs(depth):

    if len(ans_list) != 0:

        if not is_prime_number(int(''.join(map(str,ans_list)))):
            return

    if depth==N:

        sosulist.append(int(''.join(map(str,ans_list))))

        return

    for i in range(9):
        ans_list.append(sosu[i])
        dfs(depth+1)
        ans_list.pop()

dfs(0)

for i in sosulist:
    print(i)