import sys, bisect

T=int(sys.stdin.readline())

for i in range(T):
    N=int(sys.stdin.readline())
    S=[]
    for j in range(N):
        Sc_list=list(map(int,sys.stdin.readline().split()))
        S.append(Sc_list)

    S.sort()
    S2 = [S[i][1] for i in range(N)]
    Lis=[S2[0]]
    st=Lis[0]

    for k in range(N):
        if st>S2[k]:
            Lis.append(S2[k])
            st=Lis[-1]


    print(len(Lis))