import sys
input = sys.stdin.readline
#1차시도
#예제 1번 답만 가능함 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if not visited[nx][ny] and arr[nx][ny] > 4:
                visited[nx][ny] = True
                dfs(nx,ny)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#입력
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input().split)))

visited = [[False] * N for _ in range(N)] #방문여부를 위한 배열 - False로 초기화
count = 0
# 현재 count 값이랑 계산된 count 값을 비교해서 현재가 클 때까지 반복해야함 
# while result > count: #count가 작으면 종료 

for i in range(N):
    for j in range(N):
        if arr[i][j] > 4 and not visited[i][j]: #배열의 값이 N이상이고 방문하지 않은
            visited[i][j] = True
            dfs(i, j)
            count += 1

print(count)
