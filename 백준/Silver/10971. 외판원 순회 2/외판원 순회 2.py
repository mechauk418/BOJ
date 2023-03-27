
N = int(input())

W = [ list(map(int,input().split())) for _ in range(N) ]
S = [i for i in range(N) ]

route = []

min_ans = 99999999

def solve(depth,N):

    global min_ans

    if depth == N:


        ans = 0

        for i in range(N-1):
            if W[route[i]][route[i+1]]==0:
                ans = 99999999
                break
            ans+=W[route[i]][route[i+1]]
        if W[route[-1]][route[0]] != 0:
            ans += W[route[-1]][route[0]]
        else:
            ans = 99999999

        if ans < min_ans:
            min_ans = ans


        return


    for i in range(N):
        if i not in route:
            route.append(i)
            solve(depth+1,N)
            route.pop()


solve(0,N)

print(min_ans)
