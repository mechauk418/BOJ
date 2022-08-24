TC = int(input())

for i in range(TC):
    S = input()

    S_check = list(S)
    S_check.sort()

    if len(set(S_check))==2 and S_check[0]==S_check[1] and S_check[1]!=S_check[2]:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No') 