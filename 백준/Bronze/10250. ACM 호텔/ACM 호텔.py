import sys

T=int(sys.stdin.readline())

for i in range(T):
    H,W,N=map(int,sys.stdin.readline().split())

    if N%H==0:
        ans1 = N//H
        ans2 = H*100
    else:
        ans1 = (N // H) + 1
        ans2 = (N%H)*100
    

    ans3 = ans1+ans2
    print(ans3)