
T = int(input())

for t in range(T):

    S = input()

    for i in range(1,len(S)):

        if S[0:i] == S[i:2*i]:
            print(f'#{t+1} {len(S[0:i])}')
            break
