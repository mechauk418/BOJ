import sys

S = []

M = int(sys.stdin.readline().strip())

for i in range(M):

    com = sys.stdin.readline().strip()

    if com == 'all':
        S = [ i for i in range(1,21)]
        continue

    elif com == 'empty':
        S = []
        continue

    else:

        com,num = com.split()

        num = int(num)

        if com == 'add':
            if num not in S:

                S.append(num)

        elif com == 'remove':
            if num in S:
                S.remove(num)

        elif com == 'check':

            if num in S:
                print(1)
            else:
                print(0)

        elif com == 'toggle':

            if num in S:
                S.remove(num)
            else:
                S.append(num)






