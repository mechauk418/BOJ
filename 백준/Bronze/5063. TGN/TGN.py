import sys

T = int(input())

for i in range(T):
    r,e,c = map(int,sys.stdin.readline().split())

    if r < e-c:
        print('advertise')
    elif r == e-c:
        print('does not matter')
    else:
        print('do not advertise')

