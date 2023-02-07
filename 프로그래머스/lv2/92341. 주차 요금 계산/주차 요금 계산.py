from datetime import datetime
import math
def solution(fees, records):
    answer = []
    park = []
    real_rec = []
    time_table = dict()
    score = dict()

    for rec in records:
        time,number,IO = rec.split()
        elem = (time,number,IO)
        real_rec.append(elem)

    for rec in real_rec:
        if rec[1] not in park and rec[2]=='IN':
            park.append(rec[1])
            time_table[rec[1]] = rec[0]
        elif rec[1] in park:
            park.remove(rec[1])
            time_dif = datetime.strptime(rec[0],'%H:%M') - datetime.strptime(time_table[rec[1]],'%H:%M')
            time_dif = int(time_dif.seconds/60)
            if rec[1] not in score:
                score[rec[1]] = time_dif
            else:
                score[rec[1]] += time_dif

    if len(park) != 0:
        for t in park:
            time_dif = datetime.strptime('23:59','%H:%M') - datetime.strptime(time_table[t],'%H:%M')
            time_dif = int(time_dif.seconds/60)
            if t not in score:
                score[t] = time_dif
            else:
                score[t] += time_dif

    score_key = list(score.keys())
    score_key.sort()
    for i in score_key:
        if score[i] <= fees[0]:
            answer.append(fees[1])
        else:
            ans = fees[1] + math.ceil((score[i]-fees[0]) / fees[2]) * fees[3]
            answer.append(ans)

    return answer