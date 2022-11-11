import sys
sys.setrecursionlimit(100000) #없으면 recursion error 발생

y, x, k = map(int, input().split())
visited = [[False] * x for _ in range(y)]
#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 1


def dfs(cy, cx, cnt):
    visited[cy][cx] = True
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < x and 0 <= ny < y and not visited[ny][nx]:
            visited[ny][nx] = True
            cnt = dfs(ny, nx, cnt+1)
    return cnt


for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for l in range(x1, x2):
            visited[j][l] = True

res = []
for i in range(y):
    for j in range(x):
        if not visited[i][j]:
            res.append(dfs(i, j, cnt))

print(len(res))
res.sort()
for i in res:
    print(i ,end=' ')
