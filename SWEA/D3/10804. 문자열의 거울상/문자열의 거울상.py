T = int(input())

for k in range(1,T+1):

    S = input()

    S_grab = S[::-1]
    ans = ''

    for i in S_grab:
        if i == 'b':
            ans += 'd'
        elif i == 'd':
            ans += 'b'
        elif i == 'p':
            ans += 'q'
        else:
            ans += 'p'

    print(f'#{k} {ans}')
