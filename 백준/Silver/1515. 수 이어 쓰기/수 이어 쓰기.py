

n = input()

ans = 0

while True:

    ans+=1

    num = str(ans)

    while len(num) > 0 and len(n) > 0:

        if num[0] == n[0]:
            n = n[1:]
        num = num[1:]


    if n=='':
        print(ans)
        break


