import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().rstrip().split())
graph = []
dq = deque()
for i in range(n):
    gh = list(map(int, input().rstrip().split()))
    for j in range(m):
        if gh[j] == 1: dq.append((i, j))
    graph.append(gh)

#output : 모두 익을 때 최소 날짜 

def bfs():
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False] * m for _ in range(n)]
    
    while dq:
        a, b = dq.popleft()
        visited[a][b] = True
        for dx, dy in direction:
            nx = a + dx
            ny = b + dy
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and not visited[nx][ny]:
                dq.append((nx, ny))
                graph[nx][ny] = graph[a][b] + 1
bfs()
res = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit(0)
    res = max(res, max(g))

print(res-1)