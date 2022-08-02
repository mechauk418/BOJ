import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    pad1 = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    pad2 = list(map(int,sys.stdin.readline().split()))
    pad2.reverse()

    dictionary = dict.fromkeys(pad1)

    for j in range(M):
        chk = pad2.pop()
        if chk in dictionary:
            print(1)
        else:
            print(0)

