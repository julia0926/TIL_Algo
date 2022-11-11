from re import L


n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input())))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0 #각 단지수의 개수

def dfs(x, y):
    global cnt
    arr[x][y] = 0 #방문처리
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            dfs(nx, ny)
    
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)
            
print(len(result))
for i in sorted(result):
    print(i)