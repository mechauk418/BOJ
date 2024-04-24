from itertools import combinations, product
from bisect import bisect_left
from pprint import pprint

def solution(dice: list):
    dices = []
    largest_wins = 0
    answer_dices = []
    origin_indices = set(range(len(dice)))

    for indices in list(combinations(range(len(dice)), len(dice) // 2)):
        dices.append(([dice[index] for index in indices],
                      [dice[index] for index in origin_indices - set(indices)]))

    pprint(dices)

    for a_dices, b_dices in dices:
        a_sums = [sum(p) for p in product(*a_dices)]
        b_sums = sorted([sum(p) for p in product(*b_dices)])
        wins = sum([bisect_left(b_sums, a_sum) for a_sum in a_sums])
        if largest_wins < wins:
            largest_wins = wins
            answer_dices = a_dices

    answer = [dice.index(answer_dice) + 1 for answer_dice in answer_dices]
    return answer