import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().rstrip().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v,w))

start, mid, end = map(int, input().rstrip().split())

def dijkstra(st, ed, md):
    dist = defaultdict(list)
    q = [(0, st)] #가중치, 시작, 경로
    while q:
        cost, node = heappop(q)
        if node not in dist:
            dist[node] = cost
            for next_node, next_cost in graph[node]: #인접 노드 방문
                if next_node == md: #인접노드가 안 거쳐야할 노드라면 무시
                    continue
                pass_cost = next_cost + cost
                heappush(q, (pass_cost, next_node))

    return dist[ed]
                
xy_dist = dijkstra(start, mid, 0)
yz_dist = dijkstra(mid, end, 0)
not_pass_dist = dijkstra(start, end, mid)
answer = []
if not xy_dist or not yz_dist:
    answer.append(-1)
else:
    answer.append(xy_dist+yz_dist)
if not not_pass_dist:
    answer.append(-1)
else:
    answer.append(not_pass_dist)
print(*answer)