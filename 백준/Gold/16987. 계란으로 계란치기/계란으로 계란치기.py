n = int(input())

egg = []

for i in range(n):
    s,w = map(int,input().split())

    egg.append([s,w])

visited = [False] * n

def dfs(start):

    if start==n:
        cnt=0
        for i,j in egg:
            if i<=0:
                cnt+=1

        return cnt

    if egg[start][0]<=0:
        return dfs(start+1)



    for i in range(n):

        if i==start:
            continue
        if egg[i][0]>0:
            break
    else:
        return dfs(start+1)

    answer = 0

    for i in range(n):
        if i==start:
            continue
        if egg[i][0]<=0:
            continue

        egg[i][0] -= egg[start][1]
        egg[start][0] -= egg[i][1]
        
        answer = max(answer,dfs(start+1))

        egg[i][0] += egg[start][1]
        egg[start][0] += egg[i][1]

    return answer

print(dfs(0))