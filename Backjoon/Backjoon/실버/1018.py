# 실버5 :체스판 다시 칠하기 https://www.acmicpc.net/problem/1018

m, n = map(int, input().split())
board = list(input() for _ in range(m))

for i in range(m-7):
    for j in range(n-7):
        cnt = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[y][x] != 'W':
                        cnt += 1
                    



