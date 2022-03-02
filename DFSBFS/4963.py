from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
result = []
def bfs(board, x, y):
    dq = deque()
    dq.append((x, y))
    board[x][y] += 1 #방문처리
    while dq:
        val = dq.popleft()
        #print(val)
        a, b = val[0], val[1]
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny] == 1:
                dq.append([nx, ny])
                board[nx][ny] = 0



while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    board = []
    # 입력 
    for _ in range(h):
        board.append(list(map(int, input().split())))
    cnt = 0
    #print(board[3][4])
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1: #땅이라면 
                bfs(board, i, j)
                cnt += 1
    print(cnt)
    
    
    
