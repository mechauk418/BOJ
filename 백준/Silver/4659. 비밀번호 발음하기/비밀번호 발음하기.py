


# a e i o u 포함

# 모음3개 or 자음3개 x

# 연속인 글자는 ee와 oo만 허용

while True:

    password = input()

    if password=='end':
        break

    pwlist = list(password)
    cnt = 0
    moum = 0
    jaum = 0

    prev = ''
    case2 = False
    case3 = False
    for i in pwlist:

        if i in 'aeiou':
            moum+=1
            jaum=0
            cnt+=1
        else:
            jaum+=1
            moum=0

        if moum >= 3 or jaum >= 3:
            case3 = True

        if i == prev:
            if i not in 'eo':
                case2=True

        prev = i

    if cnt==0:
        print(f'<{password}> is not acceptable.')
        continue

    if case2 or case3:
        print(f'<{password}> is not acceptable.')
        continue

    print(f'<{password}> is acceptable.')
