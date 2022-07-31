
T=int(input())

for i in range(T):
    N=int(input())
    N_list = list(map(int,input().split()))
    
    N_list.sort()
    
    print(f'#{i+1} {" ".join(map(str,N_list))}')