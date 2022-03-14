from collections import deque


direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, 1], [1, -1], [-1, -1], [1, 1]]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        a, b = dq.popleft()
        for dx, dy in direction:
            nx = dx + a
            ny = dy + b
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                dq.append((nx, ny))

ans = []  

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    visited = [list(False for _ in range(w)) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result += 1
    print(result)

