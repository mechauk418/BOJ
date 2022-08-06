
def rev(S,N):

    S_reverse = S[::-1]
    rev_list = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rev_list[i][j] = S_reverse[j][i]

    return rev_list

def rev180(S,N):

    S_reverse = S[::-1]
    rev_list = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            rev_list[i][j] = S_reverse[i][j]

    for i in range(len(rev_list)):
        rev_list[i].reverse()

    return rev_list

def rev270(S,N):

    S_reverse = S[::-1]
    rev_list = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            rev_list[i][j] = S_reverse[j][i]

    rev_list.reverse()
    for i in range(len(rev_list)):
        rev_list[i].reverse()

    return rev_list


T=int(input())

for k in range(T):

    N=int(input())

    N_list = []
    for i in range(N):
        N_line = list(map(int,input().split()))
        N_list.append(N_line)


    print(f'#{k+1}')
    for i in range(N):
        print(  (''.join(map(str, rev(N_list,N)[i]))) , ''.join(map(str, rev180(N_list,N)[i])) ,''.join(map(str, rev270(N_list,N)[i])))



