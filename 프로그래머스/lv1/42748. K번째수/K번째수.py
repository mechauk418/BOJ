def solution(array, commands):
    answer = []
    
    for com in commands:
        i,j,k = com[0],com[1],com[2]
        
        ans = array[i-1:j]
        ans.sort()
        answer.append(ans[k-1])
        
        
    return answer