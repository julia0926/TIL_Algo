import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())  # 방의 크기
now_x, now_y, dir = map(int, input().rstrip().split())  # 로봇 청소기 r, c와 방향 d
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dq = deque()
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

def bfs(x, y, d):
    dq.append((x, y, d))  # 위치, 방향
    graph[x][y] = 2
    count = 1

    while dq:
        a, b, c = dq.popleft()
        nd = c
        cleaned = False  # 주변을 청소했는지 여부를 나타내는 변수

        for i in range(4):
            if nd == 0:
                nd = 3
            else:
                nd -= 1

            nx = a + direction[nd][0]
            ny = b + direction[nd][1]

            # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 존재
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 2
                dq.append((nx, ny, nd))
                cleaned = True
                break

        if not cleaned:  # 주변을 청소하지 못했을 경우
            # 후진하기
            back_c = (c + 2) % 4
            back_x = a + direction[back_c][0]
            back_y = b + direction[back_c][1]

            if 0 <= back_x < n and 0 <= back_y < m and graph[back_x][back_y] != 1:
                dq.append((back_x, back_y, c))  # 후진한 위치와 방향을 큐에 추가
            else:
                return count

    return count

res = bfs(now_x, now_y, dir)
print(res)
