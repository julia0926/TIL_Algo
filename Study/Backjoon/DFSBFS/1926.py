from collections import deque

n, m = map(int, input().split()) #세로, 가로

paper = [list(map(int, input().split())) for _ in range(n)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(y, x):
    dq = deque()
    dq.append([y,x])
    paper[y][x] = 0
    count = 1
    while dq:
        py, px = dq.popleft()
        for dx, dy in direction:
            nx = px + dx
            ny = py + dy
            if 0<=nx<m and 0<=ny<n and paper[ny][nx] == 1:
                dq.append([ny, nx])
                paper[ny][nx] = 0
                count += 1
    return count

result = []
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            result.append(bfs(i, j))
if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)