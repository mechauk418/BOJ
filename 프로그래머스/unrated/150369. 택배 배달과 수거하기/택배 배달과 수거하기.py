def solution(cap, n, deliveries, pickups):
    answer = 0
    # 역순으로 누적합
    for i in range(n-2, -1, -1):
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
    k = 0
    for i in range(n-1, -1, -1):
        while deliveries[i] > cap*k or pickups[i] > cap*k:
            answer += (i+1)*2
            k += 1
    return answer