N_list = []
for _ in range(10):
    N=int(input())
    N_list.append(N)
ans = 0
dif_min = 1000000
for i in range(len(N_list)):
    score = sum(N_list[:i+1])
    dif = abs(score - 100)
    if dif <= dif_min:
        dif_min = dif
        ans = score
    else:
        break

print(ans)