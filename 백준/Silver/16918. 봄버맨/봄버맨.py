import sys
input = sys.stdin.readline
from collections import deque
def bomberMan(r, c, grid, n):
    row, col = r, c

    def location_bomb():
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'O':
                    bomb.append((i, j))
    #3단계
    def full_bomb():
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 'O':
                    grid[i][j] = 'O'
    #4단계
    def boom():
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while bomb:
            x, y = bomb.popleft()
            grid[x][y] = '.'
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny] == 'O':
                    grid[nx][ny] = '.' #폭탄 설치
    #1단계 폭탄 설치
    for i in range(row):
        grid[i] = list(grid[i])
    n -= 1 #2단계 아무것도 하지 않음

    while n:
        #폭탄 위치 저장
        bomb = deque()
        location_bomb()

        #폭탄 설치
        full_bomb()
        n -= 1
        if n == 0:
            break
        #폭팔
        boom()
        n -= 1
    

    for gd in grid:
        print(''.join(gd))

    

            

    #0채우고 폭팔 반복

r, c, n = map(int, input().rstrip().split())
grid = [input().rstrip() for _ in range(r)]

bomberMan(r, c, grid, n)