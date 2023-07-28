import sys
sys.setrecursionlimit(10**6)


N = int(input())


def dfs(depth,N):

    for i in range(1,(depth//2+1)):
        if array[-i:] == array[-2*i:-i]:
            return -1

    if depth==N:
        for i in range(N):
            print(array[i],end='')
        return 0

    for i in range(1,4):
        array.append(i)
        if dfs(depth+1,N) ==0:
            return 0
        array.pop()


array = []
dfs(0,N)