n = int(input())
board = list(list(input()) for _ in range(n))
result = -1

def calculate():
    global board, result
    row = [row for row in board]
    col = list(zip(*board))
    max_c = 0
    bef = '-'
    for arr in row+col:
        count = 0
        # print("arr >>", arr)
        for ch in arr:
            if ch == bef:
                count += 1
            else:
                count = 1
            bef = ch
            max_c = max(max_c, count)
    # print(max_c, result)
    result = max(max_c, result)

for i in range(n):
    for j in range(n):
        #인접한지 체크
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = i + dx
            ny = j + dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny] != board[i][j]:
                    board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                    calculate()
                    board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(result)