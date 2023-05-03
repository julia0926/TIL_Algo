import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
blind = []
graph = []
direction = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    arr = input().rstrip()
    blind.append(arr.replace('R', 'G'))
    graph.append(arr)

def bfs(arr, start):
    dq = deque()
    dq.append(start)
    while dq:
        a, b = dq.popleft()
        for dx, dy in direction:
            nx = a + dx
            ny = b + dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == arr[a][b]:
                dq.append((nx, ny))
                visited[nx][ny] = True

result = []
#일반 사람
visited = [[False] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(graph, [i,j])
            ans += 1
result.append(ans)

visited = [[False] * n for _ in range(n)]
ans2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(blind, [i,j])
            ans2 += 1
result.append(ans2)
print(*result)
