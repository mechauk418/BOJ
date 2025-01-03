N = int(input())
List = list(map(int,input().split()))
DP= [[0 for _ in range(21)] for _ in range(N+1)]

for i in range(N):
    if i==0:
        DP[i][List[0]] = 1
    else:
        for j in range(21):
            if DP[i-1][j]:
                if 0<=j+List[i]<=20 :
                    DP[i][j+List[i]] += DP[i-1][j]
                if 0<=j-List[i]<=20 :
                    DP[i][j-List[i]] += DP[i-1][j]


print(DP[N-2][List[N-1]])