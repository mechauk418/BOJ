T = int(input())

for i in range(T):
    S = input()

    while True:
        S_new = S.replace('()','')
        S = S_new

        if '()' not in S:
            break
    if len(S) == 0:
        print('YES')
    else:
        print('NO')