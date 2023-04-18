n, m = map(int, input().split())
left = [0] + list(map(int, input().split()))
top = [0] + list(map(int, input().split()))

board = [top] + list([0] * (m+1) for _ in range(n))

for i in range(n+1):
    for j in range(m+1):
        if i != 0 and j == 0:
            board[i][j] = left[i]
        #위, 아래 값 비교
        elif i != 0 and j != 0:
            board[i][j] = 0 if board[i-1][j] == board[i][j-1] else 1
                
print(board[n][m])
# print(left)