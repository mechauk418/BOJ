text_list = []

while True:
    text = input()
    if text == '고무오리 디버깅 시작':
        continue
    if text == '문제':
        text_list.append(text)
    if text == '고무오리':
        if len(text_list) == 0:
            text_list.append('문제')
            text_list.append('문제')
        else:
            text_list.pop()

    if text == '고무오리 디버깅 끝':
        break

if len(text_list) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')