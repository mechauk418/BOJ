
def solution(storey):
    answer = 0

    storey = str(storey)

    q = list(storey)
    q = list(map(int,q))

    while len(q)>1:
        now = q.pop()

        if 0<= now <5:
            answer += now
        elif 5<now<=9:
            answer += 10-now
            q[-1] +=1
            if q[-1] == 10:
                if len(q) > 1:
                    q[-2] += 1
                    q[-1] = 0
                elif len(q) == 1:
                    q.insert(0, 1)
                    q[-1] = 0

        elif now == 5:
            if q[-1]>=5:
                answer += now
                q[-1] += 1
                if q[-1]==10:
                    if len(q)>1:
                        q[-2]+=1
                        q[-1]=0
                    elif len(q)==1:
                        q.insert(0,1)
                        q[-1]=0

            elif q[-1]<5:
                answer +=now

    if 0 <= q[0] <= 5:
        answer += q[0]
    elif 5 < q[0] <= 9:
        answer += 10 - q[0]+1


    return answer