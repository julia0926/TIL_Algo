import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, k):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if not visited[nx][ny] and arr[nx][ny] > k:
                visited[nx][ny] = True
                dfs(nx,ny, k)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

final = 0

for k in range(max(map(max, arr))): #arr배열 전체 중 최대값 만큼 반복 
    count = 0 
    visited = [[False] * N for _ in range(N)] #방문여부를 위한 배열 - False로 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]: #배열의 값이 N이상이고 방문하지 않은
                dfs(i, j, k)
                count += 1
    final = max(final, count)
    print(k)

print(final)

