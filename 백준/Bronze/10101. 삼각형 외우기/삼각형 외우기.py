def tri(x,y,z):
    if x==60 and y == 60 and z ==60:
        print('Equilateral')
    elif x+y+z != 180:
        print('Error')
    elif x+y+z == 180 and (x!=y) and (y!=z) and (x!=z):
        print('Scalene')
    else:
        print('Isosceles')

x = int(input())
y = int(input())
z = int(input())

tri(x,y,z)