from collections import deque


game = [list(input()) for _ in range(8)]
visited = [[False] * 8 for _ in range(8)]

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [-1, 1, 1, -1, 0, 0, -1, 1]

def bfs(n, m):
    dq = deque([n, m])
    while dq:
        num = dq.popleft()
        x, y = num
        if x == 0 and y == 7: #끝에 도달했으면 1
            return 1
        elif game[x][y] == "#": #장벽이라면 다시 
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if not visited[nx][ny]:
                




print(bfs(7, 0))