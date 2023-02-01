
S = input()

S = list(S)

ans_list = []

for i in range(1,len(S)+1):

    for j in range(len(S)):

        elem = S[j:j+i]
        if len(elem) == i:
            ans_list.append(''.join(elem))


ans_list = list(set(ans_list))

print(len(ans_list))
