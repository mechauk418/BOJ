import sys

S=[]

max_score_list = []

for i in range(5):
    score = list(map(int,sys.stdin.readline().split()))
    max_score = sum(score)
    S.append(score)
    max_score_list.append(max_score)

max_score_index = max_score_list.index(max(max_score_list)) + 1

print(max_score_index, max(max_score_list))