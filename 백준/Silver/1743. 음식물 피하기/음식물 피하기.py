import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().rstrip().split())
arr = [['.'] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().rstrip().split())
    arr[r-1][c-1] = '#'

def bfs(xx, yy):
    dq = deque()
    dq.append((xx, yy))
    arr[xx][yy] = '.'
    count = 1

    while dq:
        x, y = dq.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == '#':
                dq.append((nx, ny))
                arr[nx][ny] = '.' #방문 처리
                count += 1
    return count

result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            result.append(bfs(i, j))

print(max(result))