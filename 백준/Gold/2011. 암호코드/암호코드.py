listN = list(map(int,input()))

len = len(listN)

DP = [0]*(len+1)

DP[0]=1
DP[1]=1

if listN[0]==0:
    print(0)
else:

    for k in range(1,len):

        i = k+1

        if listN[k] > 0:
            DP[i] += DP[i-1]

        if 10 <= listN[k] + listN[k-1]*10 <= 26:
            DP[i] += DP[i - 2]

    print(DP[len]%1000000)