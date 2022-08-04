T = int(input())

for t in range(T):

    N,M = map(int,input().split())

    S_list = [  list(map(int,input().split())) for _ in range(N)]

    cnt = 0

    for k in range(N):
        for i in range(N-1,0,-1):
            for j in range(M):
                if S_list[i][j] == 0 and S_list[i-1][j] ==1:
                    S_list[i][j] = 1
                    S_list[i-1][j] = 0
                    cnt+=1

    print(cnt)