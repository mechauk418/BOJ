
def solution(n, costs):
    answer = 0

    costs.sort(key= lambda x:(x[2]))

    island = set([costs[0][0]])

    while len(island) != n:
        for i, cost in enumerate(costs):
            if cost[0] in island and cost[1] in island:
                continue
            if cost[0] in island or cost[1] in island:
                island.update([cost[0],cost[1]])
                answer+=cost[2]
                costs[i] = [-1,-1,-1]
                break

    print(answer)

    return answer