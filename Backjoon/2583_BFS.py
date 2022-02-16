from collections import deque
m, n, k = map(int, input().split())
visited = [[False] * n for _ in range(m)]
#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 1


def bfs(cy, cx, cnt):
    visited[cy][cx] = True
    dq = deque()
    dq.append((cy, cx))

    while dq:
        now = dq.popleft()
        y, x = now[0], now[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny, nx))
                cnt += 1     
    return cnt


for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for l in range(x1, x2):
            visited[j][l] = True

res = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            res.append(bfs(i, j, cnt))

print(len(res))
res.sort()
print(*res)
# for i in res:
#     print(i ,end=' ')
