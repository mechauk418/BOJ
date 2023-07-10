
def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    graph =[  [ 0 for _ in range(M+1) ] for _ in range(N+1)]

    for s in skill:

        if s[0]==1:
            dgree = -s[5]
        else:
            dgree = s[5]
        graph[s[1]][s[2]] += dgree
        graph[s[3]+1][s[2]] -= dgree
        graph[s[1]][s[4]+1] -= dgree
        graph[s[3]+1][s[4]+1] += dgree

    for i in range(N+1):
        for j in range(1,M+1):
            graph[i][j] += graph[i][j-1]

    for j in range(M+1):
        for i in range(1,N+1):
            graph[i][j] += graph[i-1][j]


    for i in range(N):
        for j in range(M):
            board[i][j]+=graph[i][j]
            if board[i][j]>0:
                answer +=1
                
    return answer