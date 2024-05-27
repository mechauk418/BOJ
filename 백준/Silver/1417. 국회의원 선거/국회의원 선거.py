import heapq

n = int(input())

dasom = int(input())
cnt=0
other = []
max_other = []

if n==1:
    print(0)
else:

    for i in range(n-1):
        temt = int(input())
        other.append(temt)
        heapq.heappush(max_other,(-temt,temt))
    
    while True:
    
        if dasom>max_other[0][1]:
            break
    
        else:
            minus_pyo,pyo = heapq.heappop(max_other)
            dasom+=1
            cnt+=1
            pyo-=1
            heapq.heappush(max_other,(-pyo,pyo))
    
    print(cnt)