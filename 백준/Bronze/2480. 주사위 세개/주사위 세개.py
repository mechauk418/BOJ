S_list = list(map(int,input().split()))

S_list.sort()

if len(set(S_list)) == 1:
    ans = 10000 + 1000*S_list[0]
elif S_list[0] == S_list[1]:
    ans = 1000 + 100 * S_list[0]

elif S_list[1]==S_list[2]:
    ans = 1000 + 100 * S_list[1]
else:
    ans = max(S_list) * 100

print(ans)