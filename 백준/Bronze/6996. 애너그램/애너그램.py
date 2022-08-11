N = int(input())

for i in range(N):
    A,B = input().split()
    list_A = list(A)
    list_B = list(B)
    list_A.sort()
    list_B.sort()
    if list_A==list_B:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')