
W_list = [ int(input()) for _ in range(10) ]
K_list = [ int(input()) for _ in range(10) ]


W_list.sort(reverse=True)
K_list.sort(reverse=True)

print( sum(W_list[0:3]),sum(K_list[0:3])         )