from itertools import product


N,M = map(int,input().split())

# 4 2


N_list = [ i for i in range(1,N+1)]


a = list(product(N_list, repeat = M))

for i in a:
    print(*i)