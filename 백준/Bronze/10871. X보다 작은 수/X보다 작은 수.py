N,X=map(int,input().split())

S_list = list(map(int,input().split()))

ans_list = [i for i in S_list if i<X]

print(' '.join(map(str,ans_list)))