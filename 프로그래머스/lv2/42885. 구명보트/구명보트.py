
def solution(people, limit):
    answer = 0

    people.sort()
    
    start = 0
    end = len(people) -1
    
    while start<end:
        if people[end] + people[start] <= limit:
            start+=1
            answer+=1
            
        end -=1
        
    answer = len(people)-answer

    return answer