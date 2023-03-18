import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드 ,간선
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) #a->b까지 c 비용
    graph[a].append((b,c))

#방문 안한 노드 중 거리가 가장 짧은 것
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) #거리, 노드
    distance[start] = 0
    
    while queue:
        dist, node = heapq.heappop(queue) #최단 거리 꺼내기 
        if distance[node] < dist: #현재 길이가 더 길면 무시 -> 갱신하지 않음
            continue
        for i in graph[node]: #현재노드와 연결된 노드들 
            cost = dist + i[1] 
            if cost < distance[i[0]]: #거쳐가는 비용이 더 짧다면
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
