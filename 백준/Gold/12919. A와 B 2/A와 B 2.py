import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
S_A = S.count('A')
S_B = S.count('B')
count = len(T) - len(S)
T_list = [T]

while count:
    count+=-1
    temt = []

    for t in T_list:
        if t[-1]=='A':
            T_1 = t[:-1]
            temt.append(T_1)
        if t[0]=='B':
            T_2 = t[::-1][:-1]
            temt.append(T_2)

    temt = list(set(temt))
    T_list = temt

    if len(T_list) == 0:
        print(0)
        break

    if len(T_list[0]) == len(S):

        if S in T_list:
            print(1)
            break
        else:
            print(0)
            break

