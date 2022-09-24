


n = int(input())
num_list = []
signs = []

imp = True
count = 1

for i in range(n):
    num = int(input())
    while count <= num:
        num_list.append(count)
        signs.append('+')
        count += 1
    if num_list[-1] == num:
        num_list.pop()
        signs.append('-')
    else:
        imp = False
if imp == False:
    print('NO')
else:
    for i in signs:
        print(i)