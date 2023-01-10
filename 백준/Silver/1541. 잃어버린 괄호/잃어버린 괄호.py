


S = input().split('-')

S_list = []

for i in S:
    K = i.split('+')
    K = list(map(int,K))
    S_list.append(sum(K))

ans_list = []

for i in range(len(S_list)):

    if i==0:
        continue

    S_list[i] = -S_list[i]

ans = sum(S_list)
print(ans)