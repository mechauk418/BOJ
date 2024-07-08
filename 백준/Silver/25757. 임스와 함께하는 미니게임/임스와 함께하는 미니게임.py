
n,game = input().split()

n = int(n)

players = []

for i in range(n):

    player = players.append(input())


players = list(set(players))



if game == 'Y':
    number = 1
elif game=='F':
    number = 2
else:
    number = 3

ans = len(players)//number

print(ans)


