
def solution(triangle):

    dp = []

    for i in range(1,len(triangle)+1):
        t = [0]*i
        dp.append(t)

    dp[0][0] = triangle[0][0]

    for i in range(len(triangle)):
        if i==0:
            continue

        for j in range(i+1):
            if j==0:
                dp[i][j] =dp[i-1][0] + triangle[i][0]
            elif j==i:
                dp[i][j] =dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

    answer = max(dp[-1])

    return answer