
T = int(input())

for t in range(T):

    p = list(input())

    n = int(input())

    arr = list(input().lstrip('[').rstrip(']').split(','))

    if arr == ['']:
        arr = []


    front = 1
    error = False

    for com in p:

        if com == 'R':
            front = 1-front

        elif com == 'D':
            if len(arr)==0:
                error = True
                break
            else:
                if front:
                    arr.pop(0)
                else:
                    arr.pop(-1)

    if error:
        print('error')
    else:
        if front:
            print( '[' + ','.join(arr)+']')
        else:
            arr.reverse()
            print( '[' + ','.join(arr)+']')