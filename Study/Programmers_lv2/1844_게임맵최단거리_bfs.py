from collections import deque

def bfs(x, y, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row, col = len(maps), len(maps[0])
    dq = deque()
    dq.append([x, y])

    while dq:
        a, b = dq.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0<=nx<row and 0<=ny<col and maps[nx][ny] == 1:
                maps[nx][ny] = maps[a][b] + 1
                dq.append([nx, ny])
    return maps[-1][-1]


def solution(maps):
    result = bfs(0, 0, maps)
    if result == 1: return -1
    else: return result


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	))