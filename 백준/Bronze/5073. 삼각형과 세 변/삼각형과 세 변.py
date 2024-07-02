

while True:

    number = list(map(int,input().split()))

    if number == [0,0,0]:
        break

    number.sort()

    if number[0]+number[1] <= number[2]:
        print('Invalid')
    elif number[0]==number[2]:
        print('Equilateral')
    elif number[0]<number[1]<number[2]:
        print('Scalene')
    else:
        print('Isosceles')


