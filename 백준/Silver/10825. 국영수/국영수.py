import sys
N = int(input())

S=[]

for i in range(N):
    name, kor, eng, math = sys.stdin.readline().split()

    kor = int(kor)
    eng = int(eng)
    math = int(math)

    S.append((name, kor, eng, math))


S.sort(key=lambda x:( -x[1],x[2],-x[3],x[0] ))

for i in S:
    print(i[0])