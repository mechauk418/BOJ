
N = int(input())

N_list = list(map(int,input().split()))

DP = [0]
DP[0]=N_list[0]

for i in range(N-1):

    DP.append( max(DP[i] + N_list[i+1],N_list[i+1] ) )


print(max(DP))

