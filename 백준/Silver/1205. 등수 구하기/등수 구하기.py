
n,new_score,p = map(int,input().split())

if n==0:
    print(1)
else:

    rank = list(map(int,input().split()))

    if n==p and new_score <= rank[-1]:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if rank[i]<=new_score:
                res = i+1
                break

        print(res)

