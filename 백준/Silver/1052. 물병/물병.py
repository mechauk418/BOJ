N,K = map(int,input().split())

cnt = 0

while True:

    if bin(N).count('1') > K:
        N +=1
        cnt +=1

    else:

        break

print(cnt)