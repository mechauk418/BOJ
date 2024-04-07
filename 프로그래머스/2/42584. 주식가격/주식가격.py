def solution(prices):
    answer = []
    n=len(prices)
    for i in range(n):
        cnt=0
        for j in range(i+1,n):
            if prices[j]<prices[i]:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)
    return answer