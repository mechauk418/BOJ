
k = int(input())

S = list(map(str,input().split()))

visited = [0]*10
max_ans = ''
min_ans = ''

array = []

def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j

def solve(idx,x):

    global max_ans,min_ans

    if idx == k+1:
        if len(min_ans)==0:
            min_ans = x
        else:
            max_ans = x

        return


    for i in range(10):
        if visited[i]==0:
            if (idx==0 or check(x[-1],str(i),S[idx-1]  )):
                visited[i]=True
                solve(idx+1,x+str(i))
                visited[i]=False


solve(0,'')
print(max_ans)
print(min_ans)