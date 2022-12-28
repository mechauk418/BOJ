from itertools import permutations

N = int(input())
A_list = list(map(int,input().split()))
plus,minus,multiple,divide = map(int,input().split())

B_list = ['+']*plus + ['-']*minus + ['x']*multiple + ['//']*divide

per = permutations(B_list,len(B_list))
per = list(set(per))
ans = A_list[0]
ans_list = []
for k in per:
    for i in range(1,len(A_list)):
        if k[i-1] == '+':
            ans = ans + A_list[i]
        elif k[i-1] == '-':
            ans = ans - A_list[i]
        elif k[i-1] == 'x':
            ans = ans * A_list[i]
        elif k[i-1] == '//':
            if ans < 0:
                ans = -((-ans) // A_list[i])
            else:
                ans = ans // A_list[i]
    ans_list.append(ans)
    ans = A_list[0]

print(max(ans_list))
print(min(ans_list))