N = int(input())
c = list(map(int, input().split()))
k = int(input())

index = N // k
arr = []

for i in range(0,N,index):
    arr = c[i:i+index]
    arr.sort()
    print(*arr,end=' ')