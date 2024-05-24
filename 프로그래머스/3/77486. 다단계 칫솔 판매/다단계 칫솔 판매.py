def solution(enroll, referral, seller, amount):
    answer = []
    n = len(enroll)
    idx_dict = dict()
    benefit = dict()
    benefit['-']=0
    for i in range(len(enroll)):
        benefit[enroll[i]]=0
        idx_dict[enroll[i]]=referral[i]

    def ben(start,price):

        if start=='-':
            benefit[start] += price
            return
        if price * 0.1>=1:
            benefit[start]+=price-int(price*0.1)
            ben(idx_dict[start],int(price*0.1))
        else:
            benefit[start] += price

    for i in range(len(amount)):
        ben(seller[i],amount[i]*100)


    for i in enroll:
        answer.append(benefit[i])


    return answer