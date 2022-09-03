
T = int(input())

for t in range(1,T+1):

    K = int(input())
    K = K-1
    ans = 0
    while K>0:
        if K % 2 ==1:
            K = (K-1)//2
        else:
            if K % 4 == 0:
                ans = '0'
                break
            elif K % 4 != 0 and K % 2 == 0:
                ans = '1'
                break
                
    print(f'#{t} {ans}')

