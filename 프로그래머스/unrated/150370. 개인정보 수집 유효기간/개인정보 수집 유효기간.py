def solution(today, terms, privacies):
    # 약관 종류: terms[0][0], terms[1][0], ...
    # 약관 유효기간: terms[0][2], terms[1][2], ...

    # 개인정보 약관 종류: privacies[i][-1]
    # ymd = (privacies[i].split()[0].split('.'))        개인정보 년, 달, 일
    result = []

    for i in range(len(privacies)):
        today_y = int(today[0:4])                       # 오늘
        today_m = int(today[5:7])
        today_d = int(today[8:])

        y, m, d = (privacies[i].split()[0]).split('.')  # 개인정보
        y = int(y)
        m = int(m)
        d = int(d)

        for j in range(len(terms)):
            if terms[j][0] == privacies[i][-1]:
                d += int(terms[j][2:]) * 28 - 1

        if d > 28:
            m += d//28
            d = d % 28
            if d == 0:
                m -= 1
                d = 28
                if m == 0:
                    y -= 1
                    m = 12
            if m > 12:
                y += m // 12
                m = m % 12
                if m==0:
                    m=12
                    y -= 1

        if today_y > y:
            result.append(i+1)
            continue
        elif today_y == y and today_m > m:
            result.append(i+1)
            continue
        elif today_y == y and today_m == m and today_d > d:
            result.append(i+1)
    return result