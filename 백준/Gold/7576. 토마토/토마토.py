from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
dq = deque()
graph = []
for i in range(m):
    g = list(map(int, input().strip().split()))
    for j in range(n):
        if g[j] == 1:
            dq.append((i, j))
    graph.append(g)

def bfs():
    visited = [[False] * n for _ in range(m)]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    while dq:
        a, b = dq.popleft()
        visited[a][b] = True
        for dx, dy in direction:
            nx = a + dx
            ny = b + dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 0:
                dq.append((nx,ny))
                graph[nx][ny] = graph[a][b] + 1

bfs()
result = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit(0)
    result = max(result, max(g))
print(result-1)
