
N = int(input())

A_list = list(map(int,input().split()))

M = int(input())

M_list = list(map(int,input().split()))

A_list.sort()

def binary(array, target ,start,end):

    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return mid

    elif array[mid] >target:
        return binary(array,target,start,mid-1)

    else:
        return binary(array,target,mid+1,end)



for i in M_list:

    if binary(A_list,i,0,N-1) == None:
        print(0)
    else:
        print(1)