#https://www.acmicpc.net/problem/1012
from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y): #가로, 세로
    dq = deque([(x, y)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<= nx < n and 0 <= ny < m and bachu[nx][ny] == 1:
                dq.append((nx, ny))
                bachu[nx][ny] = 0 # 방뭉처리 
    return 1

for _ in range(t): #테스트 케이스
    m, n, k = map(int, input().split()) #가로, 세로 
    bachu = [[0] * m for _ in range(n)] #가로 -> 세로
    for _ in range(k):
        가로, 세로 = map(int, input().split())
        bachu[세로][가로] = 1

    result = 0
    for i in range(n): #세로
        for j in range(m): #가로
            if bachu[i][j] == 1:
                result += bfs(i, j)
    
    print(result)
