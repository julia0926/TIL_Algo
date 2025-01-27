import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) #노드, 간선개수, 메세지 보내고자 하는 도시
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # x->y z 비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #시작값 가기 위한 최단경로 0
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 더 거리가 짧다면 무시
            continue
        for node in graph[now]: #인접한 노드들에 대해서
            cost = dist + node[1]
            if cost < distance[node[0]]: #최단 경로라면 갱신
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))