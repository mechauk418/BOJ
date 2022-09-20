from itertools import combinations


N,M = map(int,input().split())

# 4 2


N_list = [ i for i in range(1,N+1)]


a = list(combinations(N_list, M))

for i in a:
    print(*i)