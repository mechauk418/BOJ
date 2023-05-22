
G = int(input())

left = 1
right = 2

ans = []

while True:

    if right ** 2 - (right-1)**2 > 100000:
        break

    if right ** 2 - left**2 < G:
        right +=1
        continue

    elif right ** 2 - left**2 >G:
        left +=1
        continue

    elif (right ** 2 - left**2) ==G:
        ans.append(right)
        right += 1
        continue

if ans:
    for i in ans:
        print(i)
else:
    print(-1)