import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
graph = list(list(map(int, input().rstrip().split())) for _ in range(n))
dq = deque()

def bfs(x, y):
    dq.append((x, y))
    graph[x][y] = 0 #방문처리
    count = 1
    while dq:
        now_x, now_y = dq.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = now_x + dx
            ny = now_y + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                dq.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

area, count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            area = max(bfs(i, j), area)
            count += 1


print(count)
print(area)

