board = [list(map(int, input().split())) for _ in range(19)]
direction = [[1,0], [1,1],[0, 1],[-1, 1]] #하, 우하, 우, 우상
n = 19

def solution():
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    count = 1 #여기서 부터 시작!


                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    
                    while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == board[i][j]:
                        count += 1
                        #6개 알 이상이 연속적으로 놓였는지 체크
                        if count == 5:
                            if 0 <= nx + dx < n and 0 <= ny + dy < n and board[nx][ny] == board[nx+dx][ny+dy]:
                                break
                            if 0 <= i - dx < n and 0 <= j - dy < n and board[nx][ny] == board[i-dx][j-dy]:
                                break
                            return board[i][j], i+1, j+1
                        nx += dx
                        ny += dy
    return 0, -1, -1

color, x, y = solution()
if not color:
    print(color)
else:
    print(color)
    print(x, y)