
N = int(input())

def hanoi(n,a,b,c):

    ans = []

    if n==1:

        ans.append([a,c])

        return ans


    if n==2:

        ans.append([a, b])
        ans.append([a, c])
        ans.append([b, c])

        return ans

    if n>=3:

        ans = hanoi(n-1,a,c,b) + [[a,c]] + hanoi(n-1,b,a,c)

        return ans

print(len(hanoi(N,1,2,3)))



for i in hanoi(N,1,2,3):
    print(*i)


