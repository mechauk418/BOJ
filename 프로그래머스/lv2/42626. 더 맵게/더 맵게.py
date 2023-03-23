import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    while len(scoville)>1:

        elem1 = heapq.heappop(scoville)

        if elem1 <K:
            elem2 = heapq.heappop(scoville)
            mix = elem1 + (elem2 *2)
            heapq.heappush(scoville,mix)
            if mix < K and len(scoville)==1:
                answer = -1
                return answer
            cnt+=1
        else:
            break

    answer = cnt

    return answer