

C,R = map(int,input().split()) # 7 6

K = int(input())

ans_list = []
t = 1

if K>C*R:
    print(0)

elif K==C*R and C%2==1 and R%2==1:
    print( (C//2)+1,(R//2)+1   )

else:

    for j in range(int(min(C,R)//2)):
        for i in range(t,R):
            ans_list.append((t,i))

        for i in range(t,C):
            ans_list.append((i,R))

        for i in range(R,t,-1):
            ans_list.append((C,i))

        for i in range(C,t,-1):
            ans_list.append( (i,t) )

        R=R-1
        C=C-1
        t=t+1

    if R-t==0:
        for u in range(C-R+1):
            ans_list.append( ( t+u,t ) )

    if C-t==0:
        for x in range(R-C+1):
            ans_list.append((t,t+x) )

    print(*ans_list[K-1])