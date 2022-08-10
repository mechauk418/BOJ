
N = int(input())

ans_dict = {}
count_dict = {}

for i in range(N):
    cow,road = map(int,input().split())
    if cow not in ans_dict:
        ans_dict[cow] = road
        count_dict[cow] = 0

    else:
        if ans_dict[cow] == road:
            continue
        else:
            count_dict[cow] +=1
            ans_dict[cow] = road


print(sum(count_dict.values()))
