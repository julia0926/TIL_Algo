#https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq
def findCheapestPrice(n, flights, src, dst, k): #총 노드 개수, 경로, 시작, 도착, k개 이내 경유
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    
    queue = [(0, src, k)] #가격, 정점, 남은 경유지수

    while queue:
        price, node, left_k = heapq.heappop(queue)
        if node == dst: #목적지에 도착했다면
            return price
        
        if left_k >= 0: #경유지 횟수 제한되어있으므로
            for v, w in graph[node]: #인접한 노드 방문
                alt = price + w #갱신 가격
                heapq.heappush(queue, (alt, v, left_k-1))
    
    return -1



