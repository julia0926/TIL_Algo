import sys 
sys.setrecursionlimit(100000)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def dfs(x, y, k):
    visited[x][y] = True #방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and area[nx][ny] > k and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, k)


min_val = min(map(min, area))
max_val = max(map(max, area))

answer = []
#최소 값 이하도 생각해야 하는 이유는, 어쨌든 그것도 모든 칸이 안전영역이기 때문에 1개라고 침
#만약 최대 값이 1이라면 1개로도 정해 줘야 함 !? 나의 피셜 
for k in range(max_val+1):
    visited = list([False for _ in range(N)] for _ in range(N))
    count = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > k and not visited[i][j]: #여기도 방문처리 해줘야 함!!!!! 
                dfs(i, j, k)
                count += 1
    answer.append(count)

print(answer)