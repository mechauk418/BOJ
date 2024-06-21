
T = int(input())

for t in range(T):


    n = int(input())

    coin = list(map(int,input().split()))

    m = int(input())

    DP=[0]*(m+1)

    DP[0]=1

    for i in coin:
        for j in range(1,m+1):
            if j>=i:
                DP[j]+=DP[j-i]


    print(DP[m])