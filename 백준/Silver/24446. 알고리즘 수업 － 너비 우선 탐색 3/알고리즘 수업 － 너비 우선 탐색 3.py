from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# result = [0] * (n + 1)

visited = [False for _ in range(n+1)]
result = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    depth = 0
    dq = deque()
    dq.append((start, depth))
    visited[start] = True

    while dq:
        now_node, now_depth = dq.popleft()
        result[now_node] = now_depth
        for next in graph[now_node]:
            if not visited[next]:
                visited[next] = True
                dq.append([next, now_depth+1])
                
bfs()
for r in result[1:]:
    print(r)