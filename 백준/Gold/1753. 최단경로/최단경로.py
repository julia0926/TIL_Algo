import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
start = int(input().rstrip())
INF = 1e9

graph = defaultdict(list)
dist = defaultdict(list)

#경로값 지정
for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w)) #인접 정점, 가중치

#최단경로 찾기
def shortest_path():
    q = [(0, start)] #소요시간, 정점

    while q:
        time, now = heappop(q)
        if now not in dist:
            dist[now] = time
            for adj, adj_time in graph[now]:
                cost = time + adj_time
                heappush(q, (cost, adj))
shortest_path()

for i in range(1, V+1):
    if i not in dist.keys():
        print("INF")
    else:
        print(dist[i])
