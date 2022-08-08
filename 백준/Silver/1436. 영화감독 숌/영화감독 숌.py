
N = int(input())

N_list = [ i for i in range(5000000) if '666' in str(i)   ]

print(N_list[N-1])