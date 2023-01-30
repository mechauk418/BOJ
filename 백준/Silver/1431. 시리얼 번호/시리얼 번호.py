
N = int(input())

G_list = []

for _ in range(N):

    G = list(input())

    sum_num = 0

    for g in G:
        if g.isdigit():
            sum_num+= int(g)

    G_list.append( (''.join(G),len(G),sum_num   ) )


G_list.sort(key=lambda x:(x[1],x[2],x[0]))

for i in G_list:
    print(i[0])