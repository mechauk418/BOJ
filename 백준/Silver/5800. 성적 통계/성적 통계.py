K = int(input())

for k in range(K):
    S = list(map(int,input().split()))
    max_score = max(S[1:])
    min_score = min(S[1:])

    Score = S[1:]
    Score.sort()
    max_Lg = 0
    for i in range(len(Score)-1):
        lg = Score[i+1]-Score[i]
        if lg > max_Lg:
            max_Lg = lg


    print(f'Class {k+1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {max_Lg}')