
def comb(arr,n):

    result = []

    if n>len(arr):

        return result

    if n==1:

        for i in arr:
            result.append([i])

    elif n>1:

        for i in range(len(arr) - n + 1):

            for j in comb(arr[i+1:],n-1):
                result.append( [arr[i]] +j )

    return result





while True:

    N_list = list(map(int,input().split()))

    N = N_list.pop(0)

    if N==0:
        break

    for i in comb(N_list, 6):
        print(*i)
    print()
