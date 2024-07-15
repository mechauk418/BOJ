n = int(input())
m = int(input())
lights = list(map(int, input().split()))
last,heights = lights[0],lights[0]

for i in range(1,len(lights)):
    tmp = abs(last-lights[i])
    
    if tmp % 2 == 0:
        tmp = tmp//2
    else:
        tmp = (tmp//2) + 1  

    heights = max(heights, tmp)

    last = lights[i]

heights = max(heights, abs(n-lights[len(lights)-1]))

print(heights)