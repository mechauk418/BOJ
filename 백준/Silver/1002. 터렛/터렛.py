
T = int(input())

for _ in range(T):

    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    dis = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
        continue

    if abs(r1-r2) == dis or r1+r2 == dis:
        print(1)
    elif abs(r1-r2) < dis < r1+r2:
        print(2)
    else:
        print(0)