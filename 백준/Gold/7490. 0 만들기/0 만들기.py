from itertools import product

T = int(input())

for t in range(T):


    N = int(input())

    graph = [ i for i in range(1,N+1)]

    B = [' ','+','-']

    B_Per = list(product(B,repeat = N-1))


    for i in B_Per:
        ans = str(graph[0])

        for j in range(len(i)):
            if i[j]=='+' or i[j]=='-':
                ans += i[j]
            else:
                ans += ''
            ans += str(graph[j+1])

        check_num = eval(ans)

        if check_num == 0:

            for k in range(len(i)):
                print(graph[k],end='')
                print(i[k], end='')
            print(graph[-1])

    print()