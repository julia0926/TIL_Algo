from collections import deque

m, n = map(int, input().split())
tomato = []
dq = deque()
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))

def bfs():
    while dq:
        a, b = dq.popleft()
        for dx, dy in direction:
            nx = a + dx
            ny = b + dy
            
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[a][b] + 1
                dq.append((nx, ny))
bfs()
ans = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(tomato[i]))

print(ans-1)