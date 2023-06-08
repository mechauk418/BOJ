
N = int(input())

S = [ input() for _ in range(N) ]

S.sort(key=len)
cnt = 0


for i in range(N):
    check = False

    for j in range(i+1,N):

        if S[i]==S[j][0:len(S[i])]:
            check=True
            break

    if not check:

        cnt+=1

print(cnt)