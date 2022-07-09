A,B,C=map(int,input().split())

if B>=C:
    print(-1)


else:
    S = C - B
    D = (A // S) + 1
    print(D)
