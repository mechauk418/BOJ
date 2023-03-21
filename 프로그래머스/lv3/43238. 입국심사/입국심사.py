def solution(n, times):
    min_t=times[0]
    max_t=times[0]*n
    while(1):
        count=0
        mid=(min_t+max_t)//2
        for i in times:
            count+=(mid//i)
        if(count>=n):
            max_t=mid
        elif(count<n):
            min_t=mid
        if(min_t==max_t-1):
            answer=max_t
            break


    return answer