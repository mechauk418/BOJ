
N,d,k,c = map(int,input().split())

susi = []

max_ans = 0

for i in range(N):

    susi.append(int(input()))

for i in range(N):

    if i <= N-k:
        temt = set(susi[i:i+k])
    else:
        temt = set(susi[i:])
        temt.update(susi[:(i+k)%N])
    temt.add(c)
    max_ans = max(max_ans, len(temt))

print(max_ans)