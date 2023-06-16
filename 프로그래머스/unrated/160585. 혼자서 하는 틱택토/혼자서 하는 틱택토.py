
def solution(board):
    answer = 1
    O_tic = False
    X_tic = False
    O_cnt = 0
    X_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                O_cnt+=1
            if board[i][j]=='X':
                X_cnt+=1
                

    if 'OOO' in board:
        O_tic = True
    for i in range(3):
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            O_tic = True

    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        O_tic = True
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        O_tic = True

    if 'XXX' in board:
        X_tic = True
    for i in range(3):
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            X_tic = True
            
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        X_tic = True
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        X_tic = True

    if O_tic and X_tic:
        answer = 0
    if O_cnt >= X_cnt + 2:
        answer = 0
    if X_cnt > O_cnt:
        answer = 0
    if O_tic and (X_cnt == O_cnt):
        answer = 0
    if X_tic and (O_cnt > X_cnt):
        answer = 0

    return answer