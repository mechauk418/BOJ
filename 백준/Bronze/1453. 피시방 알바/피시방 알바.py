N = int(input())

N_list = list(map(int,input().split()))


M_list = list(set(N_list))

print( len(N_list) - len(M_list)  )