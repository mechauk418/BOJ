from collections import deque

def search(d1,d2,n_plus_one):
    set_d2 = set(d2)
    for i in d1:
        if n_plus_one - i in set_d2:
            d1.remove(i)
            d2.remove(n_plus_one-i)
            return True

    return False


def solution(coin, cards):
    answer = 0
    n = len(cards)
    hands = cards[:(n//3)]
    deck = deque(cards[(n//3):])
    select_card = []

    cnt = 1
    while coin>=0 and deck:

        select_card.append(deck.popleft())
        select_card.append(deck.popleft())

        if search(hands,hands,n+1):
            pass

        elif coin>=1 and search(hands,select_card,n+1):
            coin-=1

        elif coin>=2 and search(select_card,select_card,n+1):
            coin-=2

        else:
            break
        cnt+=1
    return cnt