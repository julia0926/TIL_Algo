from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order_graph = [0] * (n+1) #방문순서
depth_graph = [-1] * (n+1) #시작노드부터 깊이

def bfs():
    depth = 0
    order = 1
    dq = deque()
    dq.append((start, depth))
    visited[start] = True
    order_graph[start] = order

    while dq:
        now_node, now_depth = dq.popleft()
        depth_graph[now_node] = now_depth

        for adj in sorted(graph[now_node]):
            if not visited[adj]:
                visited[adj] = True
                dq.append((adj, now_depth+1))
                order += 1
                order_graph[adj] = order

bfs()
result = 0
for a, b in zip(order_graph, depth_graph):
    result += (a*b)
print(result)