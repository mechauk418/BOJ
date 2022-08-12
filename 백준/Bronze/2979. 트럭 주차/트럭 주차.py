A,B,C = map(int,input().split())

truck = []

for i in range(3):
    park_time = list(map(int,input().split()))
    truck.append(park_time)

last_time = max(map(max,truck))
time_table = [0] * (last_time+1)

for i in truck:

    for j in range(i[0],i[1]):

        time_table[j] += 1

sum = 0

for i in time_table:
    if i ==1:
        sum += A
    elif i ==2:
        sum += 2*B
    elif i ==3:
        sum += 3*C

print(sum)
