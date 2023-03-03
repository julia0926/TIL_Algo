from collections import defaultdict
import heapq

def networkDelayTime(times, N, K): #시간, 전체노드개수, 시작노드 
    graph = defaultdict(list)
    #출발지, 도착지, 소요시간
    for u, v, w in times:
        graph[u].append((v, w)) #도착지, 소요시간

    Q = [(0, K)]
    dist = defaultdict(list)

    #우선순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist: #dist에 존재하지 않으면 갱신, 존재한다면 새로운값은 이미 더 긴값이므로 갱신 필요 없음
            dist[node] = time
            for v, w in graph[node]: #인접한 노드들 확인 
                alt = time + w
                heapq.heappush(Q, (alt,v)) #거쳐간 값, 노드
        
    if len(dist) == N:
        return max(dist.values())
    return -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))