n, m = map(int,input().split())
icebox = [list(map(int,input())) for _ in range(n)]
print(icebox)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    # if x < 0 or y < 0 or x >= n or y >= m: 범위에 벗어나면 바로 종료
    #     return False
    if icebox[x][y] == 0 and (0 <= x < n) and (0 <= y < m):
        icebox[x][y] = 1 #방문처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)
