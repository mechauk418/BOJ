import sys

X = int(sys.stdin.readline().strip())

count = 0

while True:

    if len(str(X)) == 1:
        break


    X = sum(list(map(int,list(str(X)))))

    count+=1


print(count)

if X in [3,6,9]:
    print('YES')
else:
    print('NO')


