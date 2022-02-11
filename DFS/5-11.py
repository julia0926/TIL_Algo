from collections import deque


n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue #범위 벗어나면 무시
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                dq.append((nx, ny))

    return miro[n-1][m-1]

print(bfs(0, 0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111