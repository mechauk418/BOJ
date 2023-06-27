def solution(e, starts):
    dp = [0] * (e + 1)

    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            dp[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        dp[i**2]+=1


    dp_div = [0] * (e + 1)
    max_count = 0
    for idx in range(e, 0, -1):
        if max_count <= dp[idx]:
            max_count = dp[idx]
            dp_div[idx] = idx
        else:
            dp_div[idx] = dp_div[idx + 1]

    return [dp_div[start] for start in starts]