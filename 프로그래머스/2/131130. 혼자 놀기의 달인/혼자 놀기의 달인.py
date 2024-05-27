
def solution(cards:list):
    ans=[]

    cards.insert(0,0)


    for i in range(1,len(cards)):
        visited = [i]
        now = i
        while True:
            if cards[now] in visited:
                break
            visited.append(cards[now])
            now = cards[now]

        visited.sort()
        if visited not in ans:
            ans.append(visited)
    temt = []
    for i in ans:
        temt.append(len(i))
    
    temt.sort(reverse=True)
    
    if len(ans)==1:
        answer=0
    else:
        answer = temt[0]*temt[1]

    return answer