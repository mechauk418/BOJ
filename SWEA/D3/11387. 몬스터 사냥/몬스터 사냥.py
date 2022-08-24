
T = int(input())

for t in range(1,T+1):
    sum_damage = 0
    D,L,N = map(int,input().split())
    for i in range(N):
        damage = D*(1+(i*L*0.01))
        sum_damage += damage
    print(f'#{t} {int(sum_damage)} ')

