
p,m = map(int,input().split()) # 플레이어 수, 방의 정원

room = []

info = []

for i in range(p):

    level, nick = input().split()
    level = int(level)

    info.append([level,nick])


for lv,ni in info:
    check = False

    for i in range(len(room)):
        if len(room[i][1])==m:
            continue

        if room[i][0] - 10 <= lv <= room[i][0]+10:
            check = True
            room[i][1].append([lv,ni])
            break

    if not check:
        room.append([lv,[[lv,ni]]])

for i in range(len(room)):
    if len(room[i][1])==m:
        print('Started!')

        temt = sorted(room[i][1], key=lambda x:x[1])
        for j in range(m):
            print(*temt[j])
    else:
        print('Waiting!')
        temt = sorted(room[i][1], key=lambda x:x[1])
        for j in range(len(temt)):
            print(*temt[j])
