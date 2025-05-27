from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(tomatos):
    dq = deque(tomatos)
    while dq:
        x, y = dq.popleft()
        for dx, dy in [(0, 1), (1, 0 ), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

tomatos = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomatos.append((i, j))

bfs(tomatos)



def solution():
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
        result = max(result, max(graph[i]))
    if result == 1:
        return 0
    else:
        return result-1

print(solution())