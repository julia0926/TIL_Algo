import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().rstrip().split())
graph = defaultdict(list)

for _ in range(m):
    u,v,w = map(int, input().rstrip().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(st):
    q = [(0, st)]
    dist = defaultdict(list)

    while q:
        cost, node = heappop(q)
        if node not in dist:
            dist[node] = cost
            for next_node, next_cost in graph[node]:
                total_cost = cost + next_cost
                heappush(q, (total_cost, next_node))
    return dist

start, end = map(int, input().rstrip().split()) #출발, 도착
P = int(input().rstrip()) #적어도 한개의 정점을 반드시 거침
mid_path = list(map(int, input().rstrip().split())) #서로 다른 중간 정점

result = []
dist_start = dijkstra(start)
dist_end = dijkstra(end)

for mid in mid_path:
    a = dist_start[mid]
    b = dist_end[mid]
    if b: result.append(a+b)

if not result:
    print(-1)
else:   
    print(min(result))