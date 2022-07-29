
T = int(input())

for k in range(1,T+1):

    N=int(input())

    ans_list = []

    for i in [50000,10000,5000,1000,500,100,50,10]:
        AE = N // i
        N = N % i
        ans_list.append(AE)
    print(f'#{k}')
    print(' '.join(map(str,ans_list)))

