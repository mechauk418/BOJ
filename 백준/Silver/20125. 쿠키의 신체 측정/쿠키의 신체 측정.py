
n = int(input())

graph = [ list(input()) for _ in range(n) ]

search=False

leftarm,rightarm,leftleg,rightleg = 0,0,0,0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='*':
            head = [i,j]
            heart = [i+1,j]
            search = True
            break

    if search:
        break

weist_len = 0

for i in range(head[0],n):

    if graph[i][head[1]]=='_':
        weist = [i-1,head[1]]
        break
    weist_len += 1


print(heart[0]+1,heart[1]+1)


for i in range(heart[1]):
    if graph[heart[0]][i]=='*':
        leftarm+=1

for i in range(heart[1]+1,n):
    if graph[heart[0]][i]=='*':
        rightarm+=1

for i in range(weist[0]+1,n):

    if graph[i][weist[1]-1]=='*':
        leftleg+=1

    if graph[i][weist[1]+1]=='*':
        rightleg+=1

print(leftarm,rightarm,weist_len-2,leftleg,rightleg)

