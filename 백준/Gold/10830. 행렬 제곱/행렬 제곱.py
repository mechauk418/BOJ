
n,b = map(int,input().split())

graph = []

for i in range(n):

    graph.append(list(map(int,input().split())))


def mtp(arr1, arr2):
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                answer[i][j] += (arr1[i][k] * arr2[k][j])%1000
    return answer

def twice(x,n):

    if n==1:
        return x
    temt = twice(x,n//2)
    if n%2==0:
        return mtp(temt,temt)
    else:
        return mtp(mtp(temt,temt),x)


ans = twice(graph,b)

for i in range(n):
    for j in range(n):
        ans[i][j]=ans[i][j]%1000

for i in ans:
    print(*i)