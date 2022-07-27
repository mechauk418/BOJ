
T=int(input())

rank_list = ['1','A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for i in range(T):
    score_list = []
    N,K = map(int,input().split())
    for j in range(N):
        K_list = []
        K_list_index=list(map(int,input().split()))

        score = 0.35 * K_list_index[0] + 0.45 * K_list_index[1] + 0.2 * K_list_index[2]

        score_list.append(score)

        if j == K-1:
            score_K = score
    score_list.sort(reverse=True)

    front = score_list.index(score_K) # front = 앞에있는 사람 수

    rank =  (front // int(N/10)) +1

    print(f'#{i+1} {rank_list[rank]}')


