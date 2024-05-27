import heapq
from collections import defaultdict

def solution(n, paths:list, gates:list, summits:list):
    answer = []
    graph = defaultdict(list)
    for a,b,c in paths:
        graph[a].append((c,b))
        graph[b].append((c,a))
    summits.sort()
    summits_set = set(summits)

    INF = int(1e9)

    def dij():
        pq = []
        visited = [INF]*(n+1)

        for gate in gates:
            heapq.heappush(pq,(0,gate))
            visited[gate]=0

        while pq:
            intensity,node = heapq.heappop(pq)

            if node in summits_set or intensity>visited[node]:
                continue

            for w,n_node in graph[node]:
                new_intensity = max(intensity,w)
                if new_intensity < visited[n_node]:
                    visited[n_node] = new_intensity
                    heapq.heappush(pq,(new_intensity,n_node))

        min_intensity = [0, 10000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        return min_intensity


    return dij()