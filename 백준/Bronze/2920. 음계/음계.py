S=input().split()
K = ['1', '2', '3', '4', '5', '6', '7', '8']
reK = sorted(K,reverse=True)
if S == ['1', '2', '3', '4', '5', '6', '7', '8']:
    print('ascending')
elif S == reK:
    print('descending')

else:
    print('mixed')