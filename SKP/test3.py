'''
1: 꽃 심는방법잇음
0: 심을수 없음
2: 캐릭터 시작 
'''
import sys
sys.setrecursionlimit(10000)

def solution(boards):
    direction = [[0,1], [1,0], [0, -1], [-1,0]]
    row, col = len(boards[0]), len(boards[0][0])
    def dfs(x, y):
        for dx, dy in direction: #상하좌우 움직일 방향 정하기 
            nx = x + dx
            ny = y + dy

            if 0<=nx<row and 0<=ny<col and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                dfs(nx,ny)

    dig_count = 0
    for board in boards:
  
        board = [list(map(int, board[i])) for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                dig_count = board[i].count(1)

                if board[i][j] == 2:
                    board[i][j] = 1
                    dfs(i,j)
        result = []
        for i in range(row):
            if 1 in board[i]:
                result.append(1)
        
    
    return result

solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]])
# solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]])