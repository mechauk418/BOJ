import sys
input = sys.stdin.readline

prevPrize,prize = (500,300,200,50,30,10),(512,256,128,64,32)
prevFes = [0] + [prevPrize[i] for i in range(6) for _ in range(i+1)]
fes = [0] + [prize[i] for i in range(5) for _ in range(2**i)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a >= len(prevFes):
        a = 0
    if b >= len(fes):
        b = 0
    print((prevFes[a] + fes[b])*10000)