from collections import deque


N=int(input())

card_list = [ i for i in range(1,N+1)]

card = deque(card_list)

waste_card = []

while len(card) != 1:
    waste = card.popleft()
    waste_card.append(waste)

    if len(card) == 1:
        break

    waste = card.popleft()
    card.append(waste)

waste_card.append(card[0])

print(' '.join(map(str,waste_card)))