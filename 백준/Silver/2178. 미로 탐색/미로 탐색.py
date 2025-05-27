from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        a, b = dq.popleft()
        for dx, dy in [(0, 1), (1, 0 ), (-1, 0), (0, -1)]:
            nx = a + dx
            ny = b + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                dq.append((nx, ny))
                


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

print(graph[n-1][m-1])