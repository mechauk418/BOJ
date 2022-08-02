while True:
    S = input()
    ans = ''
    if S == '.':
        break
    for i in S:
        if i in ['(',')','[',']']:
            ans += i


    while True:

        ans_new = ans.replace('()','')
        ans = ans_new
        ans_new = ans.replace('[]', '')
        ans = ans_new

        if '()' not in ans and '[]' not in ans:
            break


    if len(ans) == 0:
        print('yes')
    else:
        print('no')