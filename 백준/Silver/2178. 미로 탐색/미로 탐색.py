import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
graph = list(list(map(int, input().rstrip())) for _ in range(n))
dq = deque()
visited = [[False] * m for _ in range(n)]
def bfs(x, y):
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        dx, dy = dq.popleft()
        for dirx, diry in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = dirx + dx
            ny = diry + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[dx][dy] + 1
                dq.append((nx, ny))
    return graph[n-1][m-1]

res = bfs(0, 0)
print(res)