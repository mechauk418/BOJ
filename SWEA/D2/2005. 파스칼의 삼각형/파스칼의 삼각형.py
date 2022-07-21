import itertools

T=int(input())

for k in range(T):
    N = int(input())
    print(f'#{k+1}')
    print(1)
    for i in range(N-1):
        S_list=[0]*(i+1)
        for j in range(i+2):
            result = list(itertools.combinations((S_list),j))
            print(len(result), end=' ')
        print()


